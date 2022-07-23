#Question 1

list1 = [4,5,6,7,8,9,10,11]
list1.append(12)

#Question 2

for i in range(2,7):
    print(list1[i])

#Question 3

new_tuple = ("A1","A2","A3","A4","A5","A6")
tuple_list = list(new_tuple)
tuple_list.append("A7")
tuple_list.insert(2,"A8")
new_tuple=tuple(tuple_list)
print(len(new_tuple)-2)