
def parse_input(file):
	reports = []
	for line in file:
		report = line.split()
		report = list(map(int, report))
		reports.append(report)

	return reports

def is_safe(report):
	safe = True
	contains_positive = False
	contains_negative = False
	diffs = [report[i] - report[i + 1] for i in range(0, len(report) - 1)]
	for number in diffs:
		if number == 0:
			safe = False
			continue
		if abs(number) > 3:
			safe = False
			continue
		if number < 0:
			contains_negative = True
		if number > 0:
			contains_positive = True
		if contains_positive and contains_negative:
			safe = False
			continue

	return safe

def part_1(reports):
	safe_count = 0
	for report in reports:
		if is_safe(report):
			safe_count += 1

	return safe_count

def part_2(reports):
	safe_count = 0
	for report in reports:
		if is_safe(report):
			safe_count += 1
		else:
			safe = False
			for i in range(0, len(report)):
				report_try = report.copy()
				del report_try[i]
				if is_safe(report_try):
					safe = True
					continue

			if safe:
				safe_count += 1

	return safe_count
