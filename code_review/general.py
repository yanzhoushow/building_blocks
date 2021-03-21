# start= parameter in enumerate()
for idx, name in enumerate(names, start=1):
  print(idx, name)
  
 # zip multiple lists
names = ['Nik', 'Jane', 'Melissa', 'Doug']
ages = [32, 28, 37, 53]
gender = ['Male', 'Female', 'Female', 'Male']

# Zipping through lists with zip()
zipped = zip(names, ages, gender)
zipped_list = list(zipped)

print(zipped_list)
