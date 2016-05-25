import random
import string


def passwordgen():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*()?'
  size = random.randint(8,30)
  return ''.join(random.choice(chars) for x in range(size))


def main():
    passwordgen()
    print(passwordgen())
    return


if __name__ == '__main__':
    main()
