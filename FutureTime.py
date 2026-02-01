import datetime

def main():
    # get current time
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    # ask the user for hours and minutes to add
    future_hours = int(input("Give me a number of hours: "))
    future_minutes = int(input("Give me a number of minutes: "))

    # compute future time using integer math:
    # add minutes, divide by 60 to get extra hours, remainder is the new minutes
    total_minutes = current_minute + future_minutes
    extra_hours = total_minutes // 60
    new_minute = total_minutes % 60

    # add hours and wrap around 24
    total_hours = current_hour + future_hours + extra_hours
    new_hour_24 = total_hours % 24

    # convert to 12-hour clock and AM/PM
    new_hour_12 = ((new_hour_24 + 11) % 12) + 1
   

    # output in 12-hour format "H:MM "
    print("The future time will be", f"{new_hour_12}:{new_minute:02d}")

if __name__ == '__main__':
    main()
