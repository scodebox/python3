import calendar

day = {0: 'MONDAY',
	   1: 'TUESDAY',
	   2: 'WEDNESDAY',
	   3: 'THURSDAY',
	   4: 'FRIDAY',
	   5: 'SATURDAY',
	   6: 'SUNDAY'}

data = input().split()
print(day[calendar.weekday(int(data[2]), int(data[0]), int(data[1]))])
