from datetime import date


def calculate_birthday_countdown(birthday):
    """
    Возвращает количество дней до будущего дня
    рождения или поздравляет с ним
    """
    today = date.today()
    next_birthday = get_birthday_for_year(birthday, today.year)
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    birthday_countdown = (next_birthday - today).days
    return birthday_countdown


def get_birthday_for_year(birthday, year):
    """
    Получает дату дня рождения для конкретного года.

    Ошибка ValueError возможна только в случае
    с високосными годами и ДР 29 февраля.
    В этом случае приравниваем дату ДР к 1 марта.
    """
    try:
        calculate_birthday = birthday.replace(year=year)
    except ValueError:
        calculate_birthday = date(year=year, month=3, day=1)
    return calculate_birthday
