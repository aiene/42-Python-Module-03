import sys


def main():
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        print(f"Accessing file: {sys.argv[1]}")
        f = open(sys.argv[1], 'r')
    except IndexError:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    except (IOError, PermissionError) as e:
        print(f"Error opening file: {sys.argv[1]}: ", e)
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
    try:
        f = open(sys.argv[1], "w")
        content = content.replace("\n", "#\n")
        f.write(content)
        print(f"{content}")
    except (IOError, PermissionError) as e:
        print(f"Error opening file: {sys.argv[1]}: ", e)
        return
    print()
    f.close()
    new_file_name = str(input("Enter new file name (or empty): "))
    if new_file_name:
        try:
            f = open(new_file_name, "w")
            f.write(content)
            print(f"Saving data to '{new_file_name}'")
        except (IOError, PermissionError):
            return
        f.close()
        print(f"Data saved in file '{new_file_name}'")
    else:
        print("Not saving data")


if __name__ == "__main__":
    main()
