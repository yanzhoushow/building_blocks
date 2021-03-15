# covers bisect, heapq
# bisect works for both list and string
# bisect(list/string, value, start, end) is same as bisect_right()
# bisect_left(): insert before if value already exists in the list or string.
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

# bisect on string
string = 'abcdefg'
pos_right = bisect.bisect(string, 'b')
print(pos_right)       # 2

pos_left = bisect.bisect_left(string, 'b')
print(pos_left)        # 1
