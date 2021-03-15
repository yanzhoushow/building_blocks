# covers bisect, heapq, sort
# bisect 
#  - works for both list and string
#  - bisect(list/string, value, start, end) is same as bisect_right()
#  - bisect_left(): insert before if value already exists in the list or string.
# heap / heapsort
#  - heap is special tree data structure to implement priority queue
#  - min-heap: parent node < child nodes (default heapq.heapify()
#  - max-heap: parent node > child nodes (heapq._max_heapify())
#. - complexity
#.    - heapify O(log n)
#     - insert O(1)
#.    - search O(n)
#.    - find-min/max O(1)
#.    - delete-min/max O(log n) <- re-heapify 
import bisect
import heapq

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

### HEAP
# min-heap heapify O(log n)
array = [21,1,45,78,3,5]
heapq.heapify(array)        # min-heap
print('min-heap: ', array)

# delete min
array = array[1:]
print(array)

# max heapify
heapq._heapify_max(array)
print('max-heap: ', array)


