import inflect


def main():
    p = inflect.engine()
    names = []
    try:
        while True:
            name = input("Name: ")
            if name:
                names.append(name)
    except EOFError:
        pass

    if names:
        if len(names) == 1:
            print(f"Adieu, adieu, to {names[0]}")
        elif len(names) == 2:
            joined_names = ''.join(names[:-1])
            last_name = names[-1]
            print(f"Adieu, adieu, to {joined_names} and {last_name}")
        else:
            joined_names = ', '.join(names[:-1])
            last_name = names[-1]
            last_name = f"and {last_name}"
            print(f"Adieu, adieu, to {joined_names}, {last_name}")

if __name__ == "__main__":
    main()

