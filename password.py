import string
import random
import argparse


class Generate:
    parser = argparse.ArgumentParser(
        description='A program to generate a random password.')
    parser.add_argument("-l", "--length",
                        help='Please enter a number to determine the \
                            length of your password. The default lengh is 10.',
                        type=int)
    args = parser.parse_args()

    def __init__(self):
        self.special_char = "!@#$%^&*()_-"
        self.password_length = 0

    def generate_password(self, length):
        chars = string.ascii_letters + string.digits + self.special_char
        password = ''.join(random.choice(chars) for _ in range(length))
        return password

    def main(self):
        if self.args.length is None:
            self.password_length = 10
        else:
            temp_holder = self.args.length
            self.password_length = temp_holder

        rand_password = self.generate_password(self.password_length)
        print(f"Generated Password: {rand_password}")


if __name__ == "__main__":
    generate = Generate()
    generate.main()
