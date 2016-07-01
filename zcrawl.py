import argparse
import log
import download
import findlatest
import io
import traceback


def parse_argument():
    parser = argparse.ArgumentParser(
        prog='Zadolba.li crawler',
        usage='Zadolba.li crawler [-h] [--thread-n n], [--start], [--end], [--log], [--least] ...',
        description='Download pages from zadolba.li site.'
    )
    parser.add_argument(
        '--log',
        default='error',
        help='Log level.',
        choices=['critical', 'error', 'debug'],
        dest='log_level'
    )
    subparsers = parser.add_subparsers(dest='command')
    parser_update = subparsers.add_parser('update')
    parser_range = subparsers.add_parser('range')
    parser_range.add_argument(
        '--thread-n',
        type=int,
        default=40,
    )
    parser_range.add_argument(
        '--start',
        type=int,
        default=1,
    )
    parser_range.add_argument(
        '--end',
        type=int,
        default=findlatest.get_latest(),
    )
    return parser.parse_args()


def bt_str(bt):
    out = io.StringIO()
    traceback.print_tb(bt, file=out)
    return out.getvalue()


def main():
    args = parse_argument()
    log.config(log.level(args.log_level))
    try:
        if args.command == 'update':
            download.lost_packages()
        elif args.command == 'range':
            download.start_working(files=(range(args.start, args.end+1)),
                                   threads=args.thread_n)
    except KeyboardInterrupt:
        log.debug('Forced crawler to stop...')
    except Exception:
        log.critical(bt_str(traceback))


if __name__ == '__main__':
    main()
