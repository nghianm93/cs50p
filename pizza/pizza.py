import sys
import os.path
from tabulate import tabulate

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
        print("Usage: python pizza.py <file.csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print("File not found.")
        sys.exit(1)

    with open(file_path, 'r') as file:
        pizza_data = [line.strip().split(',') for line in file]

    headers = pizza_data[0]
    data = pizza_data[1:]
    table = tabulate(data, headers=headers, tablefmt='grid')
    print(table)

if __name__ == "__main__":
    main()
