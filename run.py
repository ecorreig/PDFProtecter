import argparse
import os
from setPasswords import SetPasswords
from tqdm import tqdm
import logging


def run():
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_dir", required=True, help="Input directory file")
    parser.add_argument("-m", "--mother_password", default=None, help="Owner Password")
    parser.add_argument(
        "-l", "--pass_len", default=16, type=int, help="Password length"
    )
    args = parser.parse_args()

    # logs
    logger = logging.getLogger("pdf_protector")
    logging.basicConfig(level=logging.NOTSET)
    logger.info(
        f" > Protecting files in directory {args.input_dir} with {args.pass_len} "
        f"characters long passwords."
    )

    all_dirs = []
    for root, dirs, files in os.walk(args.input_dir):
        all_dirs.append([os.path.join(root, a) for a in dirs])

    logger.info(f" > Parsing {len(all_dirs) - 1} directories...")

    for dirname in tqdm([item for sublist in all_dirs for item in sublist]):
        pwd_setter = SetPasswords(dirname, args.mother_password, args.pass_len)
        pws = pwd_setter.set_multiple_passwords()
        if pws:
            pwd_setter.export_passwords(pws)

    logger.info(f"Done.")


if __name__ == "__main__":
    run()
