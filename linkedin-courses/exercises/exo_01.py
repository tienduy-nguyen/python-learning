num_stairs = int(input("Enter the number of stair: "))
# for num in range(1,num_stairs):
#     print((num_stairs-num)*" "+num*"#")

for num in range(1,num_stairs):
    if num% 2 != 0:
        empty_partial = int((num_stairs-num)/2) * " "
        print(empty_partial+num*"#"+empty_partial)

f = 0
def someFunction():
    global f
    f = "f in def"
    print(f)

someFunction()
print(f)
