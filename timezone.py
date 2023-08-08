import pytz
from datetime import datetime, timedelta

def get_time_difference(timezone1, timezone2):
    tz1 = pytz.timezone(timezone1)
    tz2 = pytz.timezone(timezone2)
    
    now_tz1 = datetime.now(tz1)
    now_tz2 = datetime.now(tz2)
    
    time_difference = now_tz2 - now_tz1
    return time_difference

if __name__ == "__main__":
    print('the supported timezones by the pytz module:', pytz.all_timezones, '\n')
    
    timezone1 = input("Enter the name of the first timezone: ")
    timezone2 = input("Enter the name of the second timezone: ")

    if timezone1 in pytz.all_timezones and timezone2 in pytz.all_timezones:
        # Define fixed offsets for timezones (this example uses -10 and -4 hours)
        offset_tz1 = timedelta(hours=-10)
        offset_tz2 = timedelta(hours=-4)

        time_difference = offset_tz2 - offset_tz1
        
        hours_diff = time_difference.seconds // 3600
        minutes_diff = (time_difference.seconds % 3600) // 60

        print(f"Time difference between {timezone1} and {timezone2}:")
        print(f"Hours: {hours_diff}, Minutes: {minutes_diff}")
    else:
        print("Invalid timezone names. Please choose from the list of supported timezones.")
