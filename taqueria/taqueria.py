menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}




def main():
    order = []

    while True:
        try:
            item = capitalize_words(input("Item: "))

            if item in menu:
                order.append(item)
                total_cost = sum(menu[item] for item in order)
                print(f"Total: ${total_cost:.2f}")
            elif item == "":
                continue
            else:
                continue

        except EOFError:
            break

def capitalize_words(input_str):
    words = input_str.split()
    cap_words = [word.capitalize() for word in words]
    return " ".join(cap_words)


main()
