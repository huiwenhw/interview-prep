'''
https://leetcode.com/contest/weekly-contest-59/problems/my-calendar-ii/

Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
'''

class MyCalendarTwo:
    def __init__(self):
        self.intervals = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.overlaps:
            if start < j and end > i:
                return False
        for i, j in self.intervals:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j)))
        self.intervals.append((start, end))
        return True

cal = MyCalendarTwo()
print(cal.book(10, 20)) # returns true
print(cal.book(50, 60)) # returns true
print(cal.book(10, 40)) # returns true
print(cal.book(5, 15)) # returns false
print(cal.book(5, 10)) # returns true
print(cal.book(25, 55)) # returns true
