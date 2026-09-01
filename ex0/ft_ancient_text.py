import sys


def main():
    print("=== Cyber Archives Recovery ===")
    try:
        print(f"Accessing file: {sys.argv[1]}")
    except IndexError:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    try:
        f = open(sys.argv[1], 'r')
    except IOError as e:
        print(f"Error opening file: {sys.argv[1]}: ", e)
        return
    try:
        r = f.read()
        print(f"{r}")
    except IOError:
        print("")
    f.close()
    print(f"File {sys.argv[1]} closed.")


if __name__ == "__main__":
    main()
