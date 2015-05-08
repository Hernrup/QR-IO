import sys
import time
import logging as log
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import ftplib

def start_watch():
    log.basicConfig(level=log.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%H:%M:%S')
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sl4a')
    log.info('started watch for {}'.format(path))
    observer = Observer()
    observer.schedule(UploadHandler(), path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def upload_file(file):
    log.info('uploading {}'.format(file))
    ftp = ftplib.FTP()
    ftp.connect('192.168.34.10', 2121)
    ftp.login('qpy3', 'qpy3')
    ftp.cwd('scripts3')
    fo = open(file, 'rb')
    ftp.storbinary('STOR {}'.format(os.path.basename(file)), fo)
    fo.close()
    ftp.quit()


class UploadHandler(PatternMatchingEventHandler):
    patterns = ["*.py"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        log.info('{} {}'.format(event.src_path, event.event_type))
        upload_file(event.src_path)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

if __name__ == "__main__":
    start_watch()