def main():
    camel_case = input("camelCase: ")
    snake_case = convert_to_snake_case(camel_case)
    print(f"snake_case: {snake_case}")


def convert_to_snake_case(camel_case):
    snake_case = []
    for char in camel_case:
        if char.isupper():
            snake_case.append('_' + char.lower())

        else:
            snake_case.append(char)
        print(snake_case)

    return ''.join(snake_case)


if __name__ == "__main__":
    main()
