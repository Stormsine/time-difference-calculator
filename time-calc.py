from datetime import datetime
from pytz import timezone

city_time_differences = {
    ("New York", "Tokyo"): datetime.timedelta(hours=13),
    ("New York", "London"): datetime.timedelta(hours=5),
    ("New York", "Sydney"): datetime.timedelta(hours=15),
    ("New York", "Paris"): datetime.timedelta(hours=6),
    ("New York", "Los Angeles"): datetime.timedelta(hours=3),
    ("Tokyo", "London"): datetime.timedelta(hours=9),
    ("Tokyo", "Sydney"): datetime.timedelta(hours=2),
    ("Tokyo", "Paris"): datetime.timedelta(hours=8),
    ("Tokyo", "Los Angeles"): datetime.timedelta(hours=16),
    ("London", "Sydney"): datetime.timedelta(hours=11),
    ("London", "Paris"): datetime.timedelta(hours=1),
    ("London", "Los Angeles"): datetime.timedelta(hours=8),
    ("Sydney", "Paris"): datetime.timedelta(hours=9),
    ("Sydney", "Los Angeles"): datetime.timedelta(hours=17),
    ("Paris", "Los Angeles"): datetime.timedelta(hours=9),
    ("Moscow", "Beijing"): datetime.timedelta(hours=5),
    ("Moscow", "Rio de Janeiro"): datetime.timedelta(hours=6),
    ("Moscow", "Cairo"): datetime.timedelta(hours=2),
    ("Beijing", "Rio de Janeiro"): datetime.timedelta(hours=11),
    ("Beijing", "Cairo"): datetime.timedelta(hours=6),
    ("Toronto", "Seoul"): datetime.timedelta(hours=14),
    ("Toronto", "Mexico City"): datetime.timedelta(hours=1),
    ("Toronto", "Berlin"): datetime.timedelta(hours=6),
    ("Seoul", "Mexico City"): datetime.timedelta(hours=15),
    ("Seoul", "Berlin"): datetime.timedelta(hours=8),
    ("Mexico City", "Berlin"): datetime.timedelta(hours=7),
    ("Melbourne", "Bangkok"): datetime.timedelta(hours=3),
    ("Melbourne", "Mumbai"): datetime.timedelta(hours=5),
    ("Melbourne", "Johannesburg"): datetime.timedelta(hours=6),
    ("Bangkok", "Mumbai"): datetime.timedelta(hours=1),
    ("Bangkok", "Johannesburg"): datetime.timedelta(hours=5),
    ("Mumbai", "Johannesburg"): datetime.timedelta(hours=3),
    ("Shanghai", "Chicago"): datetime.timedelta(hours=14),
    ("Shanghai", "Istanbul"): datetime.timedelta(hours=5),
    ("Shanghai", "Dubai"): datetime.timedelta(hours=5),
    ("Chicago", "Istanbul"): datetime.timedelta(hours=8),
    ("Chicago", "Dubai"): datetime.timedelta(hours=10),
    ("Istanbul", "Dubai"): datetime.timedelta(hours=2),
    ("Los Angeles", "Sydney"): datetime.timedelta(hours=17),
    ("Los Angeles", "Hong Kong"): datetime.timedelta(hours=15),
    ("Los Angeles", "Singapore"): datetime.timedelta(hours=16),
    ("Sydney", "Hong Kong"): datetime.timedelta(hours=3),
    ("Sydney", "Singapore"): datetime.timedelta(hours=3),
    ("Hong Kong", "Singapore"): datetime.timedelta(hours=0),
    ("Moscow", "New Delhi"): datetime.timedelta(hours=2),
    ("Moscow", "Bangalore"): datetime.timedelta(hours=2),
    ("Moscow", "Shenzhen"): datetime.timedelta(hours=5),
    ("Moscow", "Sao Paulo"): datetime.timedelta(hours=6),
    ("New Delhi", "Bangalore"): datetime.timedelta(hours=0),
    ("New Delhi", "Shenzhen"): datetime.timedelta(hours=2),
    ("New Delhi", "Sao Paulo"): datetime.timedelta(hours=8),
    ("Bangalore", "Shenzhen"): datetime.timedelta(hours=2),
    ("Bangalore", "Sao Paulo"): datetime.timedelta(hours=10),
    ("Shenzhen", "Sao Paulo"): datetime.timedelta(hours=11),
    ("Seoul", "Rio de Janeiro"): datetime.timedelta(hours=12),
    ("Seoul", "Mexico City"): datetime.timedelta(hours=14),
    ("Seoul", "Berlin"): datetime.timedelta(hours=8),
    ("Rio de Janeiro", "Mexico City"): datetime.timedelta(hours=2),
    ("Rio de Janeiro", "Berlin"): datetime.timedelta(hours=4),
    ("Mexico City", "Berlin"): datetime.timedelta(hours=7),
    ("Mumbai", "Bangkok"): datetime.timedelta(hours=1),
    ("Mumbai", "Johannesburg"): datetime.timedelta(hours=3),
    ("Mumbai", "Toronto"): datetime.timedelta(hours=10),
    ("Bangkok", "Johannesburg"): datetime.timedelta(hours=5),
    ("Bangkok", "Toronto"): datetime.timedelta(hours=12),
    ("Johannesburg", "Toronto"): datetime.timedelta(hours=6)
    # Add more city pairs and time differences as needed
}

def get_time_difference(city1, city2):
    key = (city1, city2)
    
    if key in city_time_differences:
        time_difference = city_time_differences[key]
        hours = time_difference.seconds // 3600
        seconds = time_difference.seconds % 3600
        return hours, seconds
    else:
        return "Time difference not defined for the specified cities."

if __name__ == "__main__":
    city1 = input("Enter the name of the first city: ")
    city2 = input("Enter the name of the second city: ")

    hours_diff, seconds_diff = get_time_difference(city1, city2)

    print(f"Time difference between {city1} and {city2}:")
    print(f"Hours: {hours_diff}, Seconds: {seconds_diff}")

