def main():
    grocery_items = {}

    while True:
        try:
            item = input().strip().title()

            if item in grocery_items:
                grocery_items[item] += 1
            else:
                grocery_items[item] = 1

        except EOFError:
            break

    sorted_items = sorted(grocery_items.items(), key=lambda x: x[0])

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()
