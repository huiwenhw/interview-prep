'''
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example, given heights = [2,1,5,6,2,3], return 10.
'''

# keep ascending buildings index in a stack
# if a descending building is detected, pop out the latest building from the stack
# checks for every peak in the array and keeps the ascending elements 
# once all ascendings buildings are added at index i, check 
# use dummy building at the end to calc the 'final' ascending buildings
def area_short(height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(height)):
        print('i ', i, ' s ', stack, ' height[i] ', height[i], ' h[s[-1]] ', height[stack[-1]])
        while height[i] < height[stack[-1]]:
            print('h[i] ', height[i], ' < h[s[-1]] ', height[stack[-1]])
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            print('h', h, ' w', w, ' hw', h*w, ' i ', i, ' s ', stack)
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans

# naive way TLE
def area(heights):
    if not heights: return 0
    start, end = 0, len(heights)-1
    area = maxa = 0
    for i in range(len(heights)):
        for k in range(i, len(heights)):
            minn = min(heights[i:k+1])
            area = ((k-i)+1) * minn
            maxa = max(maxa, area)
    return maxa

# didnt pass, did the container way which was wrong
def area(heights):
    if not heights: return 0
    start, end = 0, len(heights)-1
    area = maxa = 0
    while start <= end:
        minn = min(heights[start:end+1])
        area = ((end-start)+1) * minn
        print('s ', start, ' e ', end, ' h[s] ', heights[start], ' h[e] ', heights[end], area)
        maxa = max(maxa, area)
        if heights[start] <= heights[end]:
            start += 1
        elif heights[start] > heights[end]:
            end -= 1
    return maxa


heights = [4,2,0,3,2,4,3,4]
heights = [5,5,1,7,1,1,5,2,7,6]
heights = [1,2,3,4]
heights = [2,1,5,6,2,3]
print(area_short(heights))
heights = [4,3,2,1]
print(area_short(heights))

'''
#print(area(heights)) # 10
heights = [1,5,1]
print(area_short(heights))
#print(area(heights)) # 5
heights = [11]
print(area_short(heights))
#print(area(heights)) # 11
heights = [4,2,0,3,2,4,3,4]
print(area_short(heights))
#print(area(heights)) # 10
heights = [5,5,1,7,1,1,5,2,7,6]
print(area_short(heights))
#print(area(heights)) # 12
'''
