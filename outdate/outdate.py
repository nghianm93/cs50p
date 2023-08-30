import re

month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


def parse_date(input_str):
    if input_str.startswith('"') and input_str.endswith('"'):
        output_str = input_str[1:-1]
    else:
        output_str = input_str
    final_str = "".join(output_str.split())
    date_pattern = r"(\d{1,2})[/\s](\d{1,2})[/\s](\d{4})"
    comma_pattern = re.compile(r",")
    match_comma = bool(comma_pattern.search(final_str))
    match = re.match(date_pattern, final_str)
    if match:
        month, day, year = map(int, match.groups())
        if int(month) <= 12 and int(day) <= 31:
            return f"{year:04d}-{month:02d}-{day:02d}"
        else:
            return None

    for idx, month_name in enumerate(month_names, start=1):
        if month_name in final_str:
            month = idx
            match = re.search(r"(\d{1,2})[,\s]*(\d{4})", final_str)
            if match and match_comma:
                day, year = map(int, match.groups())
                if int(day) <= 31:
                    return f"{year:04d}-{month:02d}-{day:02d}"
                else:
                    return None

    return None


def main():
    while True:
        user_input = input("Date: ")
        formatted_date = parse_date(user_input)

        if formatted_date:
            print(formatted_date)
            break


if __name__ == "__main__":
    main()
