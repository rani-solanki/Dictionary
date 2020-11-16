my_dict={"a":45,"b":78,"c":54}
max1=0
max2=0
max3=0
empty_dict={}
for i in my_dict:
    if max1 < my_dict[i]:
        max1=my_dict[i]
        x=i
print(max1)
for j in my_dict:
    if max2<my_dict[j] and max1>my_dict[i]:
        max2 = my_dict[j]
        Y=J
empty_dict.update(max2)
for m in my_dict:
    if max3<my_dict[m] and max1>my_dict[i] and maax2>my_dict[j]:
        max3=my_dict[m]
        z=m
empty_dict.update(max3)
print(empty_dict)

        


            