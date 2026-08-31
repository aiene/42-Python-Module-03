#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input("Enter new coordinates as floats in format "
                           "'x,y,z': ").split(',')
        if len(user_input) != 3:
            print("Invalid syntax")
            continue
        try:
            try_value = user_input[0]
            x = float(try_value)
            try_value = user_input[1]
            y = float(try_value)
            try_value = user_input[2]
            z = float(try_value)
            return(x, y, z)
        except ValueError as e:
            print(f"Error on parameter: '{try_value}'", e)


def main():
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    set1 = get_player_pos()
    print(f"Got a first tuple: {set1}")
    print(f"It includes: X:{set1[0]}, Y:{set1[1]}, Z:{set1[2]}")
    center_distance = math.sqrt((0-set1[0])**2 +
                                (0-set1[1])**2 + (0-set1[2])**2)
    print(f"Distance to center: {center_distance}")
    print()
    set2 = get_player_pos()
    distance = math.sqrt(((set1[0] - set2[0])**2) +
                         ((set1[1] - set2[1])**2) + (set1[2] - set2[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()
