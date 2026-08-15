import requests
from collections import Counter
from datetime import datetime

url = f"https://api.github.com/users/Charlie-Edwards/events/public"
events = requests.get(url).json()

days = Counter()
for event in events:
    dt = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    days[dt.strftime("%A")] += 1

for day, count in days.most_common():
    pass

print("Most active:", days.most_common(1)[0])
print("Least active:", days.most_common()[-1])
