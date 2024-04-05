import scienceplots  # pylint: disable=unused-import
import matplotlib.pyplot as plt
from figure_beauty import MAMPF_DARK_BLUE, set_size
import db_dump_parser as p

plt.style.use(["science"])
OUT_FILE = "./out/email-hosts.pdf"

parser = p.DbDumpParser()


def plot_email_hosts(hosts):  # pylint: disable=redefined-outer-name
    plt.figure(figsize=set_size())

    # Pie chart
    labels = hosts.keys()
    sizes = hosts.values()
    max_size = max(sizes)

    # pylint: disable-next=unused-variable
    patches, texts, autotexts = plt.pie(  # type: ignore
        sizes,
        labels=labels,
        autopct=lambda pct: f"{pct:.1f}\\%" if pct > 2 else "",
        wedgeprops=dict(width=0.6, edgecolor=MAMPF_DARK_BLUE, linewidth=1.0, fill=False),
        labeldistance=1.0,
        startangle=-120,
        rotatelabels=True,  # Rotate the labels
        counterclock=False,  # Rotate the labels clockwise
    )

    def interp(x):
        minimum = 4
        return minimum + (10 - minimum) * x

    for i, t in enumerate(texts):
        count = list(sizes)[i]
        t.set_fontsize(interp(count / max_size))

    plt.title("MaMpf email hosts")
    plt.savefig(OUT_FILE)
    print(f'💾 Plot saved to "{OUT_FILE}"')


if __name__ == "__main__":
    emails = parser.table_column("users", "email")

    # Get part of mail after @
    emails = [email.split("@")[1] for email in emails]

    # Get number of occurrences
    email_counts = {}
    for email in emails:
        if email in email_counts:
            email_counts[email] += 1
        else:
            email_counts[email] = 1

    # Sort by number of occurrences
    email_counts = dict(sorted(email_counts.items(), key=lambda item: item[1], reverse=True))

    # Filter out small appearances, but aggregate them as "Other"
    other_count = 0
    for email, count in list(email_counts.items()):
        if count < 30:
            other_count += count
            del email_counts[email]
    email_counts["Other"] = other_count

    # Print
    for email, count in email_counts.items():
        print(f"{email}: {count}")

    # Plot
    plot_email_hosts(email_counts)
