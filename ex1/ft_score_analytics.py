#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    if argc == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    list_args = []
    for args in sys.argv[1:]:
        try:
            list_args.append(int(args))
        except ValueError:
            print(f"Invalid parameter: {args}")
    players = len(list_args)
    if players == 0:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    else:
        print(f"Scores processed: {list_args}")
        print(f"Total players: {len(list_args)}")
        print(f"Total score: {sum(list_args)}")
        print(f"Average score: {sum(list_args) / len(list_args)}")
        print(f"High score: {max(list_args)}")
        print(f"Low score: {min(list_args)}")
        print(f"Score range: {max(list_args) - min(list_args)}")


if __name__ == "__main__":
    main()
