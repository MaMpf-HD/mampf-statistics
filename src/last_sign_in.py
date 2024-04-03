from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import scienceplots
from figure_beauty import set_size
plt.style.use(["science", "ieee"])

CSV_FILE = '../data/last-sign-in-dates.csv'


def get_dates_from_file():
    all_dates = []
    total_count = 0

    with open(CSV_FILE, 'r', encoding='utf-8') as data:
        data.readline()  # skip header

        for line in data:
            total_count += 1
            line = line.split(',')
            date = line[1]
            if date != '':
                all_dates.append(date)

    return all_dates, total_count


def plot_dates(dates):
    plt.figure(figsize=set_size())
    plt.hist(dates, bins=40, color='#223e62', ec='white', lw=0.6)

    plt.gca().figure.autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
    plt.gca().xaxis.set_minor_locator(ticker.NullLocator())

    plt.tick_params(axis='x', colors='white', labelcolor='black')
    # plt.xticks(rotation=10)
    plt.xlabel("Date (YYYY-MM-DD)")
    plt.ylabel("Number of users with last sign in at that date")
    plt.title("Last sign in dates")
    plt.savefig("./last-sign-in-dates.pdf")


dates, total_count = get_dates_from_file()
print(f'Total count: {total_count}')
print(f'Number of dates (that are not NULL): {len(dates)}')
dates = [datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f') for date in dates]

oldest_date = min(dates)
newest_date = max(dates)
print(f'Oldest date: {oldest_date}')
print(f'Newest date: {newest_date}')

plot_dates(dates)
