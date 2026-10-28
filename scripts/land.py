"""Week 1: upload one day's CSV to MinIO at raw/transactions/dt=DAY/part-0.csv."""
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", required=True)
    args = parser.parse_args()
    print(f"TODO week 1: upload data/out/{args.day}.csv to bucket ledgerlake")


if __name__ == "__main__":
    main()
