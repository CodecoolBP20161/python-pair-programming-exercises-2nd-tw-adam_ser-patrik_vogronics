import datetime


def years(age):
    old = int(datetime.datetime.now().year) - int(age) + 100
    return old


def main():
    name = input("What is your name?: ")
    age = input("How old are you?: ")
    years(age)
    print(name + str(" you will be 100 years old in ") + str(int(
     datetime.datetime.now().year) - int(age) + 100))
    return


if __name__ == '__main__':
    main()
