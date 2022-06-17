# Write a program to reverse an array or string
array = list(map(int, input("Enter Array Element: ").strip().split()))[:]
print(f"Befor Reversing : {array}")
for i in range(len(array)//2):
    temp = array[i]
    array[i] = array[len(array)-1-i]
    array[len(array)-1-i] = temp
print(f"After Reversing : {array}")

#Using Slicing Operator :)
print(f"Reversing Again : {array[::-1]}")