from faker import Faker

faker = Faker()


def generate_massege() -> str:
    return f"Hi!, {faker.unique.first_name()}"
