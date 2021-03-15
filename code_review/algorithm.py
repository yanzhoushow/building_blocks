# covers bisect, heapq
import bisect

array = [1, 3, 5, 7]
pos = bisect.bisect(array, 4)     # same as bisect_right(), the insert point comes after (to the right of) any existing entries of x in array
print(f'bisect result: {pos}')

val = 4
array.insert(pos, val)
print(array)                 # [1,3,4,5,7]

# bisect with range
array = [9, 7, 1, 3, 5]
start = 2
end = 4
value = 4
pos = bisect.bisect(array, value, start, end)
array.insert(pos, value)
print(array)        # [9,7,1,3,4,5]
