

def secure_archive(filename: str, action: str, content: str = "") -> tuple:
    try:
        if action != 'r' and action != 'w':
            return(False, "Error in parameter: Action can be only 'r' or 'w'.")

        with open(filename, action) as file:
            if action == 'r':
                content = file.read()
                return(True, content)

            file.write(content)
            return (True, "Content successfully written to file")

    except Exception as e:
        return (False, f"{e}")


def main():
    print(
        "=== Cyber Archives Security ===\n\n"
        "Using 'secure_archive' to read from a nonexistent file:"
        )
    print(secure_archive("/not/existing/file", "r"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/passwd", "w"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "r")
    print(result)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("archive.txt", "w", result[1]))


if __name__ == '__main__':
    main()
