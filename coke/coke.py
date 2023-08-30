def main():
    total_amount_due = 50
    amount_insert = 0

    while amount_insert < total_amount_due:
        coin = int(input("Insert Coin: "))

        if coin in [25, 10, 5]:
            amount_insert += coin
            amount_due = total_amount_due - amount_insert
            if amount_insert != total_amount_due:
                print(f"Amount Due: {amount_due}")
        else:
            print(f"Amount Due: {total_amount_due}")

    if amount_insert >= total_amount_due:
        change = amount_insert - total_amount_due
        print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()
