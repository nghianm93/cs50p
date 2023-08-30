import sys
import csv

def main():
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py <input.csv> <output.csv>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        with open(input_filename, 'r') as input_file:
            reader = csv.reader(input_file)
            header = next(reader)
            if header != ['name', 'house']:
                print("Input file does not have the expected format.")
                sys.exit(1)

            with open(output_filename, 'w', newline='') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(['first', 'last', 'house'])

                for row in reader:
                    full_name = row[0].strip('"')
                    last_name, first_name = full_name.split(', ')
                    writer.writerow([first_name, last_name, row[1]])

        print(f"Converted data written to '{output_filename}'")

    except FileNotFoundError:
        print("Input file not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
