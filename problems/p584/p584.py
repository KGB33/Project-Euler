# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 21:50:15 2018

@author: kelto
"""

"""
Birthday Problem Revisited
Problem 584
A long long time ago in a galaxy far far away, the Wimwians, inhabitants of
planet WimWi, discovered an unmanned drone that had landed on their planet.
On examining the drone, they uncovered a device that sought the answer for the
 so called "Birthday Problem". The description of the problem was as follows:

If people on your planet were to enter a very large room one by one, what will
 be the expected number of people in the room when you first find 3 people with
 Birthdays within 1 day from each other.

The description further instructed them to enter the answer into the device and
 send the drone into space again. Startled by this turn of events, the Wimwians
 consulted their best mathematicians. Each year on Wimwi has 10 days and the
 mathematicians assumed equally likely birthdays and ignored leap years (leap
 years in Wimwi have 11 days), and found 5.78688636 to be the required answer.
 As such, the Wimwians entered this answer and sent the drone back into space.

After traveling light years away, the drone then landed on planet Joka. The
same events ensued except this time, the numbers in the device had changed due
 to some unknown technical issues. The description read:

If people on your planet were to enter a very large room one by one, what will
 be the expected number of people in the room when you first find 3 people with
 Birthdays within 7 days from each other.

With a 100-day year on the planet, the Jokars (inhabitants of Joka) found the
answer to be 8.48967364 (rounded to 8 decimal places because the device allowed
 only 8 places after the decimal point) assuming equally likely birthdays. They
 too entered the answer into the device and launched the drone into space again.

This time the drone landed on planet Earth. As before the numbers in the problem
 description had changed. It read:

If people on your planet were to enter a very large room one by one, what will
be the expected number of people in the room when you first find 4 people with
Birthdays within 7 days from each other.

What would be the answer (rounded to eight places after the decimal point)
 the people of Earth have to enter into the device for a year with 365 days?
 Ignore leap years. Also assume that all birthdays are equally likely and
 independent of each other.
"""
import time
import random


def main():
    # Wimwi Test
    numWimwi = bpr(3, 1, 10)
    print("Wimwi: ", numWimwi)
    print("Differance: ", numWimwi - 5.78688636)
    print()
    # Jokar
    numJokar = "unk"  # bpr(3, 7, 100)
    print("Jokar :", numJokar)
    print("Differance: ", numJokar)  # - 8.48967364)
    print()
    # Earth
    numEarth = "unk"  # bpr(4, 7, 365)
    print("Earth: ", numEarth)


def bpr(numPeopleRequired, numDaysApart, lenYear):
    days = {x: 0 for x in range(0, lenYear)}
    withinDays = False
    while not withinDays:

        # adds a new Person to the room
        days[addBirthDay(lenYear)] += 1
        print(days)

        # Checks to see if n number of bdays are within m days
        for i in range(0, lenYear):
            totalBDays = 0
            for j in range(i, i + numDaysApart + 1):
                totalBDays += days[j]
                print("total days: ", totalBDays)
                print("i: ", i, " i + numDays: ", i + numDaysApart, " j: ", j)
                if totalBDays > numPeopleRequired - 1:
                    withinDays = True
                    break
                break

    # Counts numPeople In room
    totalPeople = 0
    for day, numBDays in days.items():
        totalPeople += numBDays
    return totalPeople


def addBirthDay(lenYear):
    return random.randint(0, lenYear - 1)


startTime = time.clock()
main()
print("\n\nTime: ", time.clock() - startTime)
