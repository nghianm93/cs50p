def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def split_string(s):
    if len(s) <= 2:
        return s, ""
    return s[:2], s[2:]


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False


    if s.isalnum():
        p1, p2 = split_string(s)

        if p1[-1].isdigit():
            return False

        if p2[0].isdigit() and p2[-1].isalpha():
            return False

        if p2[0].isdigit() and p2[0] == "0":
            return False

        if p2[0].isdigit() and len(p2) > 3:
            for i, char in enumerate(p2):
                if i != 0 and char.isdigit():
                    return False


        return True

    return False


if __name__ == "__main__":
    main()
