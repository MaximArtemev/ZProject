import argparse
import sys
import log
import clean
import os

HTML = '/home/max/PycharmProjects/FULL_DATA/HTML_DATA'


def parse_argument():
    parser = argparse.ArgumentParser(
        prog='Zadolba.li cleaner',
        usage='Zadolba.li cleaner [-h], [--start], [--end], [--all], [--log], [--least] ...',
        description='Clean pages from zadolba.li html pages.'
    )
    parser.add_argument(
        '--log',
        default='error',
        help='Log level.',
        choices=['critical', 'error', 'debug'],
        dest='log_level'
    )
    subparsers = parser.add_subparsers(dest='command')
    parser_all = subparsers.add_parser('all')
    parser_least = subparsers.add_parser('least')
    parser_range = subparsers.add_parser('range')
    parser_range.add_argument('--start', type=int, default=1)
    parser_range.add_argument('--end', type=int, default=0)
    return parser.parse_args()


def main():
    args = parse_argument()
    log.config(log.level(args.log_level))
    try:
        if args.command == 'all':
            clean.start_working(files=os.listdir(HTML))
        elif args.command == 'range':
            clean.start_working(files=[str(i) + '.txt' for i in range(args.start, args.end)])
        elif args.command == 'least':
            clean.lost_packages()
    except KeyboardInterrupt:
        log.debug('Forced cleaner to stop...')
    except Exception:
        _, value, traceback = sys.exc_info()
        log.critical('%s\n%s', value, traceback)


if __name__ == '__main__':
    main()
