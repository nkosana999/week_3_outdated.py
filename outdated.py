def main():
    months = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12
    }
    while True:
        date = input("Date: ").lower()
        date_list = date.replace(" ","/").split("/")
        
        if len(date_list) == 3:
            month = date_list[0].strip(',.!')
            day = date_list[1].strip(',.!')
            year = date_list[2].strip(',.!')

            if month in months:
                try:
                    if (1 <= int(day) <= 31 and 1000 <= int(year) <= 9999):
                        print(f"{year}-{months[month]:02}-{int(day):02}")
                        break
                    else:
                        continue

                except KeyError:
                    continue
            else:
                try:
                    if(1 <= int(day) <= 31 and 1<= int(month) <= 12 and 1000 <= int(year) <= 9999):
                        print(f"{year}-{int(month):02}-{int(day):02}")
                        break
                    else:
                        continue

                except ValueError:
                    continue

        else:
            continue

main()