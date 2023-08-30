import emoji

def emojize_text(text):
    emojized_text = emoji.emojize(text)
    return emojized_text

def main():
    user_input = input("Input: ")
    emojized_output = emojize_text(user_input)
    print("Output:", emojized_output)

if __name__ == "__main__":
    main()
