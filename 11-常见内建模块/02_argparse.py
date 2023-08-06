import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='backup',
        description='Backup MySQL database.',
        epilog='Copyright(r), 2023'
    )

    parser.add_argument('outfile')
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default='3306', type=int)
    parser.add_argument('-u', '--user', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('--database', required=True)
    parser.add_argument('-gz', '--gzcompress', action='store_true' ,required=False, help='Compress backup files by gz.')

    args = parser.parse_args()

    print('parsed args:')
    print(f'outfile = {args.outfile}')
    print(f'host = {args.host}')
    print(f'port = {args.port}')
    print(f'user = {args.user}')
    print(f'password = {args.password}')
    print(f'database = {args.database}')
    print(f'gzcompress = {args.gzcompress}')

if __name__ == '__main__':
    main()
