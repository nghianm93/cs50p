import sys
import os.path

def count_lines_of_code(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if line.strip() and not line.strip().startswith('#'):
                    count += 1
            return count
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.py'):
        print("Usage: python lines.py <file.py>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print("File not found.")
        sys.exit(1)

    lines_of_code = count_lines_of_code(file_path)
    print(f"Lines of code in '{file_path}': {lines_of_code}")

if __name__ == "__main__":
    main()
