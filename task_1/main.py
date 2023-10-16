from get_birthdays_per_week import get_birthdays_per_week
from users import generate_users_list

users_list = generate_users_list(100)

get_birthdays_per_week(users_list)
