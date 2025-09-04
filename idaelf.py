import lief
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extracts and adds symbols from IDBs to ELFs"
    )

    parser.add_argument("binary", type=str)

    parser.add_argument("idb", type=str)
