def main():
    print(validated(input("Ip: ")))


def validated(input_ip):
    temp = input_ip.split('.')

    if len(temp) != 4:
        return False

    for t in temp:
        if not t.isdigit():
            return False

        num = int(t)

        if num < 0 or num > 255:
            return False

    return True


if __name__ == '__main__':
    main()