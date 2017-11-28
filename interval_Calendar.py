'''
https://leetcode.com/contest/weekly-contest-59/problems/my-calendar-i/

Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.
Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.
A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)
For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
'''

class MyCalendar:
    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        can_add = True
        if len(self.intervals) == 0:
            self.intervals.append([start, end-1])
        else:
            for interval in self.intervals:
                #if interval[1] >= start and end > interval[0]:
                if not (interval[1] < start or end <= interval[0]):
                    can_add = False
            if can_add: self.intervals.append([start, end-1])
        return can_add 

    def book_short(self, start, end):
        for s, e in self.intervals:
            if not (start >= e or end <= s): return False
        self.intervals.append((start, end))
        return True
        
cal = MyCalendar()
print(cal.book(10, 20)) # returns true
print(cal.book(15, 25)) # returns false
print(cal.book(20, 30)) # returns true
cal2 = MyCalendar()
print(cal2.book_short(10, 20)) # returns true
print(cal2.book_short(15, 25)) # returns false
print(cal2.book_short(20, 30)) # returns true
