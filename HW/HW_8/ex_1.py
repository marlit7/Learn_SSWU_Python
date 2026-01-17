import calendar
import locale
from functools import wraps


def translate(language):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_locale = locale.setlocale(locale.LC_TIME)
            locale.setlocale(locale.LC_TIME, language)
            days = func(*args, **kwargs)
            locale.setlocale(locale.LC_TIME, current_locale)
            return days
        return wrapper
    return decorator


def short_form(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        days = func(*args, **kwargs)
        return list(calendar.day_abbr)
    return wrapper


@translate("de_DE.utf8")
@short_form
def get_data():
    return list(calendar.day_name)


if __name__ == '__main__':
    print(get_data())
