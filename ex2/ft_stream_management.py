import sys


def main():
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        print(f"Accessing file: '{sys.argv[1]}'")
        f = open(sys.argv[1], 'r')
    except IndexError:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    except (IOError, PermissionError) as e:
        print(f"Error opening file: {sys.argv[1]}: ", e, file=sys.stderr)
        return
    print("---")
    print()
    try:
        content = f.read()
        print(f"{content}")
    except IOError:
        print("")
    f.close()
    print("---")
    print(f"File {sys.argv[1]} closed.")
    print()
    print("Transform data:")
    print("---")
    try:
        f = open(sys.argv[1], "w")
        content = content.replace("\n", "#\n")
        f.write(content)
        print(f"{content}")
    except (IOError, PermissionError) as e:
        print(f"[STDERR] Error opening file: '{sys.argv[1]}': ",
              e, file=sys.stderr)
        print("Data not saved.")
        return
    print()
    f.close()
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_file_name = sys.stdin.readline()
    if new_file_name.endswith("\n"):
        new_file_name = new_file_name[:-1]
    if new_file_name:
        print(f"Saving data to '{new_file_name}'")
        try:
            f = open(new_file_name, "w")
            f.write(content)
        except (IOError, PermissionError) as e:
            print(f"[STDERR] Error opening file: '{new_file_name}': ",
                  e, file=sys.stderr)
            print("Data not saved.")
            return
        f.close()
        print(f"Data saved in file '{new_file_name}'")
    else:
        print("Data not saved")


if __name__ == "__main__":
    main()
