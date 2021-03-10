#   Holiday Checker
#   By Ben Apacible
#   This script will tell you if it is a public holiday in Brisbane, Australia
#   Except Easter.
#   Easter is dead to me.

import time

# Grab the date today
Day = time.strftime("%a")
Date = time.strftime("%d")
Month = time.strftime("%m")
DateMonth = Date+Month

#Define Weekends and what they mean
Weekend = ["Sat", "Sun"]
MovedToMonday = "The day off has been moved to Monday"
BadEnd = "The day off is today, the weekend."

#Holidays that are always on the same date each year
FixedHolidays = [
          "New Year's Day"
        , "Australia Day"
        , "ANZAC Day"
        , "Christmas Day"
        , "Boxing Day"]
FixedHolidates = ["0101", "2601", "2504", "2512", "2612"]
DayOffMoves = ["0101", "2601", "2512", "2612"]

#Holidays that have a floating date, except Easter.
ChangingHolidays = [
          "Labour Day"
        , "Queen's Birthday"
        , "Ekka Wednesday"]
MonthsOfChangers = ["05", "08", "08"]

if DateMonth in FixedHolidates:
    Index = FixedHolidates.index(DateMonth)
    print("It is " + FixedHolidays[Index])
    if (Day in Weekend) and (DateMonth in DayOffMoves):
        print(MovedToMonday)
    elif (Day in Weekend):
        print(BadEnd)
    else:
        print("Day off!")

elif Month in MonthsOfChangers:
    Index = MonthsOfChangers.index(Month)
    if (Month == "05") and (Day == "Mon") and ("01" <= Date <= "07"):
        print ("It is " + ChangingHolidays[0])
    elif (Month == "08") and (Day == "Mon") and ("08" <= Date <= "14"):
        print ("It is " + ChangingHolidays[1])
    elif (Month == "08") and (Day == "Wed") and ("08" <= Date <= "14"):
        print ("It's probably " + ChangingHolidays[2] +
                ". If there's 5 Wednesdays this month, then maybe it's next week!")

elif Day in Weekend:
    print("No holiday today, but at least it's the weekend")

elif Day not in Weekend:
    print("No holiday today.  Go to work.")

