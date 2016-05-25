def palindrome(str):
    str = str.replace(" ", "")
    str = str.lower()
    return str[::-1] == str


def main():
    word = input("Write in a word:")
    palindrome(word)


if __name__ == '__main__':
    main()
