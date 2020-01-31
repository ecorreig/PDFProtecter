import argparse
import os
from setPasswords import SetPasswords


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_dir', required=True,
                        help='Input directory file')
    parser.add_argument('-m', '--mother_password', default=None,
                        help='Owner Password')
    parser.add_argument('-l', '--password_length', default=16,
                        help='Password length')
    args = parser.parse_args()

    for root, dirs, files in os.walk(args.input_dir):
        all_dirs = [os.path.join(root, a) for a in dirs]
        for dirname in all_dirs:
            pwd_setter = SetPasswords(dirname, args.mother_password, args.password_length)
            pws = pwd_setter.set_multiple_passwords()
            if pws:
                pwd_setter.export_passwords(pws)

    print('Done!')


if __name__ == '__main__':
    main()
