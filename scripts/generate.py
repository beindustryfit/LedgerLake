"""Week 1: write a daily CSV of fake card transactions.

Run: python -m scripts.generate --day 2026-01-05 --rows 100
"""
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", required=True)
    parser.add_argument("--rows", type=int, default=100)
    args = parser.parse_args()
    out = Path("data/out") / f"{args.day}.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("transaction_id,customer_id,merchant,amount,currency,created_at\n")
    print(f"TODO week 1: write {args.rows} rows to {out}")


if __name__ == "__main__":
    main()
