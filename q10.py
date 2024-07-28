import calendar

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

month_name = input("Enter a month name: ")
month_index = months.index(month_name) + 1

year = int(input("Enter a year: "))

days_in_month = calendar.monthrange(year, month_index)[1]

print(f"Number of days in {month_name} {year}: {days_in_month}")
