string="MISSISSIPPI"
a=len(string)
d=list(string)
b={}
count=0
for i in d:
    b[i]=b.get(i,0)+1
print(b)
# my_dict = {}
# for letter in string:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
# print(my_dict)

  