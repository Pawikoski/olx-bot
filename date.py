from datetime import date


def format_date(string_date):
    d = string_date.lower()
    if "dzisiaj" in d:
        return date.today()
