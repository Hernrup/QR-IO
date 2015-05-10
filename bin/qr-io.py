#!/usr/bin/env python
import sys
from qrio_web import app
import logging as log
import argparse
from qrio_utils import upload, qr
from cherrypy import wsgiserver


def run_client(args):
    app.external_uri = args.external_uri
    from qrio_web import views
    if args.debug:
        app.run(debug=args.debug, port=args.port, host='0.0.0.0')

    else:
        d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
        server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', args.port), d)

        try:
            server.start()
        except KeyboardInterrupt:
            server.stop()


def generate_qr(args):
    print(qr.generate_qr_string(args.data))


def setup_parser():
    root_parser = argparse.ArgumentParser(description='QR-IO Service')
    sp = root_parser.add_subparsers()

    upload_parser = sp.add_parser('upload')
    upload.setup_argparse(upload_parser)

    io_parser = sp.add_parser('io')
    io_parser.set_defaults(func=run_client)
    io_parser.add_argument('-d', '--debug', help='debug', action='store_true',
                           default=False)
    io_parser.add_argument('-e', '--external-uri', help='External hostname',
                           default=None)
    io_parser.add_argument('-p', '--port', help='Port to listen to',
                           default=5000)

    qr_parser = sp.add_parser('qr')
    qr_parser.set_defaults(func=generate_qr)
    qr_parser.add_argument('-d', '--data', help='data', default='')

    return root_parser, root_parser.parse_args()


def setup_logging():
    log_instace = log.getLogger()
    log_instace.setLevel(log.DEBUG)


def main():
    setup_logging()
    parser, args = setup_parser()
    if hasattr(args, 'func'):
        args.func(args)
        return
    parser.print_help()

if __name__ == '__main__':
    main()

