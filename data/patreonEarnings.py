import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

earnings_by_date = defaultdict(float)

with open("creator-analytics-detailed-earnings.csv") as file:
    reader = csv.DictReader(file)
    reader.fieldnames = [f.strip() for f in reader.fieldnames]

    for row in reader:
        print(f"\n{row['Member name']}")
        print(f"Member charge amount: {row['Member charge amount']}")
        print(f"Creator share: {row["Creator share"]}")
        print(f"Patreon share: {float(row["Member charge amount"]) - float(row["Creator share"])}")
        date = row["Date"].split()[0]
        earnings_by_date[date] += float(row["Creator share"])

dates = sorted(earnings_by_date.keys())
earnings = [earnings_by_date[d] for d in dates]

total_earnings = []
running = 0

for e in earnings:
    running += e
    total_earnings.append(running)

colors = plt.cm.plasma(np.array(total_earnings) / max(total_earnings))

plt.bar(dates, total_earnings, color=colors)

plt.xlabel("Date")
plt.ylabel("Daily Earnings (£)")

plt.xticks(rotation=90)
plt.yticks(np.arange(0, max(total_earnings) + 1, 1))

plt.tight_layout()
plt.show()
