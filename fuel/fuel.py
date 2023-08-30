def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))

            if y == 0:
                fraction = input("Fraction: ")
                x, y = map(int, fraction.split('/'))
                continue

            if y < x:
                fraction = input("Fraction: ")
                x, y = map(int, fraction.split('/'))
                continue

            percentage = (x / y) * 100
            if percentage <= 1:
                result = "E"
            elif percentage >= 99:
                result = "F"
            else:
                result = round(percentage)

            if result == "E" or result == "F":
                print(result)
            else:
                print(f"{result}%")
            break

        except ValueError:
            print("Invalid input. Please enter a valid fraction (X/Y).")
        except ZeroDivisionError:
            print("Y cannot be 0. Please try again.")


if __name__ == "__main__":
    main()
