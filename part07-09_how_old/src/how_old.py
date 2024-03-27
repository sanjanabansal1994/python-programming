# Write your solution here
from datetime import datetime, timedelta

day= int(input("Day: "))
mnth= int(input("Month: "))
yr= int(input("Year: "))
millennium_day= datetime(1999,12,31)
diff= millennium_day - datetime(yr,mnth,day)
if diff.days<0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f'You were {diff.days} days old on the eve of the new millennium.')