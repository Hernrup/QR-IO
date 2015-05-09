import sys
import time
import logging as log
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os
import ftplib
import argparse


class FtpSyncer():
    def __init__(self, username, password, host='localhost', port=21):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def upload_file(self, file):
        log.info('uploading {}'.format(file))
        ftp = ftplib.FTP()
        ftp.connect(self.host, self.port)
        ftp.login(self.username, self.password)
        ftp.cwd('scripts3')
        fo = open(file, 'rb')
        ftp.storbinary('STOR {}'.format(os.path.basename(file)), fo)
        fo.close()
        ftp.quit()

    def sync_files(self, files):
        for f in files:
            self.upload_file(f)


class UploadHandler(PatternMatchingEventHandler):

    def __init__(self, patterns, ftp):
        super(UploadHandler, self).__init__(patterns, None, False, False)
        self.ftp = ftp
        self.pattern = ['*QR*.py']

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
        self.ftp.upload_file(event.src_path)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


def start_watch(ftp, watch):
    setup_logging()
    watched_files = ["QR-IO.py"]
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sl4a')
    ftp.sync_files([os.path.join(path, f) for f in watched_files])

    if not watch:
        return

    log.info('started watch for {}'.format(path))
    observer = Observer()
    observer.schedule(UploadHandler(watched_files, ftp), path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def setup_logging():
    log.basicConfig(level=log.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%H:%M:%S')


def parse_args():
    parser = argparse.ArgumentParser(description='Sync files with device')
    parser.add_argument('-u', help='ftp username',
                        default='qpy3')
    parser.add_argument('-p', help='ftp password',
                        default='qpy3')
    parser.add_argument('-s', help='ftp server',
                        default='localhost')
    parser.add_argument('-o', help='ftp port',
                        default=2121)
    parser.add_argument('-w', action='store_true', help='watch',
                        default=False)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    ftp = FtpSyncer(username=args.u, password=args.p,
                    host=args.s, port=args.o)
    start_watch(ftp, args.w)

