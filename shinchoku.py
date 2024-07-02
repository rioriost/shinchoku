#!/usr/bin/env python3

from datetime import datetime
import time
import argparse


def main():
    parser = argparse.ArgumentParser(description = "Display the rest of year")
    parser.add_argument("--duration", "-d",
        type = float,
        default = 1.0,
        help = "Duration to display (default: 1.0)")

    args = parser.parse_args()

    while True:
        now = datetime.now()
        year_start = datetime.fromisoformat("{}-01-01T00:00:00".format(now.year))
        year_end = datetime.fromisoformat("{}-01-01T00:00:00".format(now.year + 1))
        d_year_start = now - year_start
        d_year_end = year_end - now
        total = year_end - year_start
        print("Passed    : {}, {:.6f}%".format(d_year_start, d_year_start / total * 100))
        print("Remaining : {}, {:.6f}%".format(d_year_end, d_year_end / total * 100))
        print("\33[3A")
        time.sleep(args.duration)

if __name__ == "__main__":
    main()
