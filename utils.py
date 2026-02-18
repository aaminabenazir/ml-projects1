'''scores=[85,92,78,95,88]
total=sum(scores)
count=len(scores)
average=total/count
print(f"average score:{average:}")'''



'''names = ["Alice", "Bob", "Emily", "David", "Oliver", "Sarah"]

vowels = {'A', 'E', 'I', 'O', 'U'}

count = 0

for name in names:
    if name and name[0].upper() in vowels:
        count += 1

print(f"Names starting with vowels: {count}")'''

'''names = ["Alice", "Bob", "Emily", "David", "Oliver", "Sarah"]
vowels = {'A', 'E', 'I', 'O', 'U'}
count = sum(1 for name in names
if name.startswith(('A', 'E', 'I', 'O', 'U')))
print(f"Names starting with vowels: {count}")'''

'''numbers = [45, 23, 67, 89, 12, 56]

max_value = max(numbers)
max_index = numbers.index(max_value)

print("Maximum value:", max_value)
print("Position:", max_index)'''


'''number=(7,)
print(number)
print(type(number))'''


'''red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)


print("Red:   ", red)
print("Green: ", green)
print("Blue:  ", blue)'''



numbers = [5, 2, 8, 2, 9, 2, 1, 2]
target = 2

positions = []

for index in range(len(numbers)):
    if numbers[index] == target:
        positions.append(index)

print(f"Value {target} found at positions: {positions}")

