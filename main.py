from faker import Faker

faker = Faker()


def main():
    print(f"Hi!, {faker.unique.first_name()}")


if __name__ == '__main__':
    main()
