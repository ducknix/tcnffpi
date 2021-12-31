#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# π

import sys
import argparse

from mpmath import mp
from threading import Thread


class Parameters(argparse.ArgumentParser):
    def __init__(self) -> None:

        super(Parameters, self).__init__(
            usage="%(prog)s [options]",
            description="Turkish Citizen number finder from π digits",
            prog="./tcnffpi"
        )

        self.add_argument(
            "--digits",
            dest="digit",
            metavar="N",
            help="Number of π digits to be processed",
            action="store",
            default=1000
        )

        self.add_argument(
            "--threads",
            dest="threads",
            metavar="N",
            help="An integer for the number of threads",
            action="store",
            default=2
        )

        self.add_argument(
            "--output",
            dest="output_dir",
            metavar="DIR",
            help="Path to write found results",
            action="store",
            default=False
        )

        self.add_argument(
            "--quiet",
            dest="quiet",
            help="The program runs silently",
            action="store_true",
            default=False
        )

    def get_args(self) -> dict:
        return self.parse_args().__dict__


def check_national_identifer(id: int) -> bool:
    id = str(id)

    first = id[:-2]
    last = id[-2:]

    def check_1(id: str) -> bool:
        x = 0
        y = 0

        for i in [0, 2, 4, 6, 8]:
            x += int(id[i])

        for j in [1, 3, 5, 7]:
            y += int(id[j])

        x *= 7

        return ((x - y) % 10 == int(id[9]))

    def check_2(id: str) -> bool:
        x = 0

        for i in range(0, 10):
            x += int(id[i])

        return x % 10 == int(id[-1])

    if (len(id) < 11 or len(id) > 11):
        return False

    elif (id[0] == "0"):
        return False

    elif not(check_1(id) and check_2(id)):
        return False

    else:
        return True


def search_in_digits(digits: int, fs: bool, quiet: bool) -> int:

    for i in range(len(digits)):
        x = (digits[i: i+11])
        if (len(x) < 11):
            break

        if (check_national_identifer(x)):
            if (fs):
                with open(fs, "a") as file:
                    file.write(x + "\n")
            if (not quiet):
                print("Found: %s" % x)


def simple_function(pi, x, y, z, i):
    search_in_digits(pi[x:y], z, i)


def main() -> int:
    args = Parameters().get_args()

    output = args["output_dir"]
    thread = int(args["threads"])
    digits = int(args["digit"])
    quiet = args["quiet"]

    thargs = [0]
    thlist = []

    if (thread < 1 or thread > 4):
        raise Exception("The number of threads can be at most 4, at least 1")

    # Generate PI Digits
    mp.dps = digits + 1
    mp.dps = mp.dps + (11 - mp.dps % 11)
    π = str(mp.pi).split(".")[1]

    for i in range(1, thread+1):
        thargs.append((digits // thread * i) + (digits % i))

    for i in range(len(thargs)):
        try:
            args = (π, thargs[i], thargs[i+1], output, quiet)
            thlist.append(Thread(None, target=simple_function, args=args))

        except IndexError:
            break

    for i in thlist:
        i.start()
        i.join()

    return 0


if __name__ == "__main__":
    # sen giderken adımlarını sayarım, heyhat!
    sys.exit(main())
