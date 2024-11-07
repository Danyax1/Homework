def get_from_user():
    path = input("Enter the file path: ")
    mode = input("Enter the file mode (b/t): ")
    if mode == "b" or mode == "t":
        return path, mode
    else:
        print("Wrong mode")


def main():
    path, mode = get_from_user()
    try:
        f = open(path, f"{mode}r")
        f.close()
    except FileNotFoundError:
        print("File not found")
    else:
        count_lines = 0
        with open(path, f"{mode}r") as user_f:
            for _ in user_f.readlines():
                count_lines += 1
            print(count_lines)


if __name__ == '__main__':
    main()
