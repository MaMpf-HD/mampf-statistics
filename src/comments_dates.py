from datetime import datetime

import scienceplots  # pylint: disable=unused-import
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from figure_beauty import MAMPF_DARK_BLUE, set_size
import db_dump_parser as p

plt.style.use(["science"])
OUT_FILE = "./out/comments-dates.pdf"

parser = p.DbDumpParser()


def plot_dates(dates):  # pylint: disable=redefined-outer-name
    plt.figure(figsize=set_size())
    plt.hist(dates, bins=80, color=MAMPF_DARK_BLUE, ec="white", lw=0.5)

    plt.gca().figure.autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
    plt.gca().xaxis.set_minor_locator(ticker.NullLocator())

    plt.tick_params(axis="x", colors="white", labelcolor="black")
    plt.xlabel("Date (YYYY-MM-DD)")
    plt.ylabel("Number of comments/posts created")
    plt.title(r"Comments \& posts creation dates")
    plt.savefig(OUT_FILE)
    print(f'💾 Plot saved to "{OUT_FILE}"')


if __name__ == "__main__":
    comments_dates = parser.table_column("commontator_comments", "created_at")
    posts_dates = parser.table_column("thredded_posts", "created_at")
    creation_dates = comments_dates + posts_dates
    creation_dates = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f") for date in creation_dates]
    plot_dates(creation_dates)
