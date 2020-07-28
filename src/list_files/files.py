from argparse import ArgumentParser
import os


def list_files(root_path: str, file_extensions=True):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file_extensions:
                print(file)
            else:
                file_split = file.split('.')
                if len(file) > 1:
                    print(''.join(file_split[:-1]))
                else:
                    print(''.join(file_split))


if __name__ == "__main__":
    parser = ArgumentParser(
        description='Prints a list of files from a root path.'
    )
    parser.add_argument(
        'root_path', metavar='p', type=str, nargs='?',
        help='Root path from where to start the traversal.'
    )
    parser.add_argument(
        '--n', action='store_false',
        help='No file extensions'
    )
    args = parser.parse_args()

    list_files(args.root_path, file_extensions=args.n)
