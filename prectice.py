# dic={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# b=[]
# for i in dic:
#     b.append(i*i)
# new=zip(dic,b)
# new1=dict(new)
# print(new1)
string="rinki"
string1=list(string)
# print(string1)
i = 0
b=0
while(i<len(string1)):
    if(string1[i]=="k"):
        string1.remove(string1[i])
        string1[i]= "l"
        string1.append(string1[i])
    i=i+1
print(string1)


