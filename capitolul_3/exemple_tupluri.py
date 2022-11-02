# my_tuple=()
# my_tuple=tuple()
# my_tuple=(1,2,3,4)

my_tuple = (10, "abc", 20, "True", True, 1, -100, 3.5)
print(my_tuple[2])
# my_tuple[2]=100
my_tuple += (4,5,6,20)
print(my_tuple)

for val in my_tuple:
    print(val, end=" ")
print()
print(70 in my_tuple)
print(70 not in my_tuple)
