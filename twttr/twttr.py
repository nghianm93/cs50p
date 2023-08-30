def main():
    input_text = input("Input: ")
    text_without_vowels = remove_vowels(input_text)
    print(f"Output: {text_without_vowels}")


def remove_vowels(text):
    vowels = "aeiouAEIOU"
    without_vowels = ''.join([char for char in text if char not in vowels])
    return without_vowels


if __name__ == "__main__":
    main()
