from datetime import datetime

import scienceplots  # pylint: disable=unused-import
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from figure_beauty import MAMPF_DARK_BLUE, set_size
import db_dump_parser as p

plt.style.use(["science", "ieee"])
OUT_FILE = "./out/last-sign-in-dates.pdf"

parser = p.DbDumpParser()


def plot_dates(dates):  # pylint: disable=redefined-outer-name
    plt.figure(figsize=set_size())
    plt.hist(dates, bins=40, color=MAMPF_DARK_BLUE, ec="white", lw=0.6)

    plt.gca().figure.autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    # plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
    plt.gca().xaxis.set_minor_locator(ticker.NullLocator())

    plt.tick_params(axis="x", colors="white", labelcolor="black")
    # plt.xticks(rotation=10)
    plt.xlabel("Date (YYYY-MM-DD)")
    plt.ylabel("Number of users with last sign in at that date")
    plt.title("Last sign in dates")
    plt.savefig(OUT_FILE)
    print(f'💾 Plot saved to "{OUT_FILE}"')


if __name__ == "__main__":
    last_sign_ins = parser.table_column("users", "last_sign_in_at")
    print(f"Number of dates: {len(last_sign_ins)}")

    # Filter out NULL values
    last_sign_ins = [date for date in last_sign_ins if date is not None]
    print(f"Number of dates (that are not NULL): {len(last_sign_ins)}")

    dates = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f") for date in last_sign_ins]
    oldest_date = min(dates)
    newest_date = max(dates)
    print(f"Oldest date: {oldest_date}")
    print(f"Newest date: {newest_date}")

    plot_dates(dates)
