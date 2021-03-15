# code review takeaways for hash, dict, Counter, collections etc
import collections

# prefer defaultdict over {}
memo = collections.defaultdict(list)
memo_dict = {}

print(memo['non_exist_key'])          # return [], preferred because it's shorter
print(memo.get('non_exist_key'))      # return []
print(memo_dict['non_exist_key'])     # KeyError exception!

# Counter example
ctr = collections.Count()
string = 'abcddfefef'

for c in string:
  ctr[c]+=1
  
print(ctr['non_exist_char'])        # return 0
