'''
https://leetcode.com/problems/container-with-most-water/description/

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''

# want to find container with max height and max width btwn them 
# start from ends of array 
# shift shorter one in 
# keep checking the max 
# stop when we reach the middle 
def max_area(height):
    start, end = 0, len(height)-1
    m = -1
    # not <= cause dont have to check with itself, area will be 0
    while start < end:
        area = (end - start) * min(height[start], height[end])
        print(start, end, area)
        m = max(m, area)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return m

print(max_area([4, 1, 3, 4])) # 12
