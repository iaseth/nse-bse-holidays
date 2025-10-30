import json

from tabulate import tabulate



with open("holidays.json") as f:
	jo = json.load(f)
	holidays = jo['holidays']


for year in range(2018, 2026):
	holidays_in_year = [h for h in holidays if str(year) in h[0]]
	out_file = f"{year}.md"

	with open(out_file, "w") as f:
		f.write(f"# Stock Market Holidays in {year}\n\n")
		f.write(tabulate(holidays_in_year, tablefmt="github", headers=["Date", "Holiday"]))
		f.write("\n\n")
	print(f"Saved: {out_file} ({len(holidays_in_year)} holidays)")

