import json
from datetime import datetime, date

from tabulate import tabulate



class Holiday:
	def __init__(self, date_str, name):
		self.date = datetime.strptime(date_str, "%Y-%m-%d").date()
		self.name = name

		self.year = self.date.year
		self.formatted = self.date.strftime("%d %B %Y")
		self.date_str = str(self.date)
		self.month_str = self.date.strftime("%B")
		self.weekday_str = self.date.strftime("%A")

	@property
	def cols(self):
		return [self.month_str, self.date_str, self.weekday_str, self.name]

	def __repr__(self):
		return f"Holiday ({self.formatted})"


with open("holidays.json") as f:
	jo = json.load(f)
	holidays = [Holiday(date_str, name) for date_str, name in jo['holidays']]


def main():
	for year in range(2018, 2026):
		holidays_in_year = [holiday.cols for holiday in holidays if year == holiday.year]
		out_file = f"{year}.md"

		with open(out_file, "w") as f:
			f.write(f"# Stock Market Holidays in {year}\n\n")
			f.write(tabulate(holidays_in_year, tablefmt="github", headers=["Month", "Date", "Day", "Holiday"]))
			f.write("\n\n")
		print(f"Saved: {out_file} ({len(holidays_in_year)} holidays)")


if __name__ == '__main__':
	main()
