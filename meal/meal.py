def main():
    time = input("Enter the time (HH:MM): ")
    hours = convert(time)

    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()
