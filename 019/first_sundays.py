#!/usr/bin/env python

# Had a day counter from Udacity course cs101
# so gonna use that:

def isLeap(year):
    ''' Returns bool -- does what it says on the tin '''
    # Not a century
    if year%4==0 and year%100!=0:
        return True
    # Appropriate century
    if year%100==0 and year%400==0:
        return True
    return False

def nextDay(year, month, day):
    months=(31,28,31,30,31,30,31,31,30,31,30,31)
    """Simple version: assume every month has 30 days"""
    if day==28 and month==2:
        if isLeap(year): return year, month, day+1
    if day<months[month-1]:
         return year, month, day+1
    else:
        if month<12:
            return year, month+1, 1
        else:   
            return year+1, 1, 1 

def isBefore(year1, month1, day1, year2, month2, day2):
    if year1<year2:
        return True
    elif year1==year2:
        if month1 < month2:
            return True
        if month2==month1:
            return day1<day2
    return False
        
def firstSundaysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # Check correct order of dates:
    assert isBefore(year1,month1,day1,year2,month2,day2), "No time travel!"

    # Gregorian error:
    if isBefore(year1,month1,day1,1582,10,15):
        print '''Your date goes back to before the start of 
        the Gregorian calendar, results might be off.'''
    
    today=(year1,month1,day1)
    incounter=0
    counter=0
    while not isBefore(year2,month2,day2-1, *today):
        # tuples get unpacked picky in 2.7 so need the -1
        today=nextDay(*today)
        incounter+=1
        if incounter%7==0 and today[2]==1:
            counter+=1
    return counter

# 5th Jan 1901 is the first Sunday of the century
print firstSundaysBetweenDates(1901,1,5,2000,12,31)
