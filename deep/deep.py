def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

    if ans.lower().replace(" ", "") == "42" or ans.lower().replace(" ", "") == "forty-two" or ans.lower().replace(" ", "") == "fortytwo":
        print("Yes")
    else:
        print("No")

main()