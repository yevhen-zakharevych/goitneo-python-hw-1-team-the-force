from faker import Faker
from datetime import datetime

fake = Faker()


def generate_user():
    name = fake.name()
    birthday = fake.date_time_between(start_date=datetime(1960, 1, 1), end_date=datetime(2005, 1, 1))

    return {
        "name": name,
        "birthday": birthday
    }


def generate_users_list(length: int):
    return [generate_user() for i in range(length)]


if __name__ == "__main__":
    user_list = generate_users_list(1)
    print(user_list)

