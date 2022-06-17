# Maximum and minimum of an array using minimum number of comparisons
array = list(map(int,input("Number: ").strip().split()))[:]
print(f"Array of Number is: {array}")
min = array[0]
max = array[0]
for i in array:
    if i<min:
        min=i
    if i>max:
        max=i
print(f"Minimum Value : {min} & Maximum Value : {max}")
