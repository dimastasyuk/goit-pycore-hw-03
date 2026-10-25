from datetime import datetime, timedelta
import random
import re


# Task 1
def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - given_date).days
    except (ValueError, TypeError):
        return None


print(get_days_from_today("2023-01-01"))


# Task 2
def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1):
        return []

    numbers = []

    while len(numbers) < quantity:
        number = random.randint(min, max)

        if number not in numbers:
            numbers.append(number)

    numbers.sort()

    return numbers


happy_numbers = get_numbers_ticket(1, 49, 6)

print("Ваші щасливі номери:", happy_numbers)


# Task 3
def normalize_phone(phone_number):
    phone_number = re.sub(r"[^\d+]", "", phone_number)

    if phone_number.startswith("+"):
        return phone_number
    elif phone_number.startswith("380"):
        return "+" + phone_number
    else:
        return "+38" + phone_number


raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# Task 4
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Anna", "birthday": "1998.10.26"},
    {"name": "Mike", "birthday": "1990.10.28"},
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Список привітань на цьому тижні:", upcoming_birthdays)
