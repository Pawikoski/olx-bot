from datetime import datetime


def format_date(string_date):
    d = string_date.lower()
    if "dzisiaj" in d:
        return datetime.strftime(datetime.today(), "%d/%m/%Y")
    else:
        day, month, year = d.split(" ")

    return "/".join([day, month_number(month), year])


def month_number(month):
    match month:
        case "stycznia":
            return "01"
        case "lutego":
            return "02"
        case "marca":
            return "03"
        case "kwietnia":
            return "04"
        case "maja":
            return "05"
        case "czerwca":
            return "06"
        case "lipca":
            return "07"
        case "sierpnia":
            return "08"
        case "września":
            return "09"
        case "października":
            return "10"
        case "listopada":
            return "11"
        case "grudnia":
            return "12"
