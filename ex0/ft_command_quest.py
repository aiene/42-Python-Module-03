#!/usr/bin/env python3

import sys


def main():
    print("=== Command Quest ===")
    print(f"Program_name: {sys.argv[0]}")

    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(arguments)}")

        i = 1
        for argument in arguments:
            print(f"Argument {i}: {argument}")
            i += 1
    print(f"Total arguments: {len(sys.argv)}")
    print()


if '__main__' == __name__:
    main()
