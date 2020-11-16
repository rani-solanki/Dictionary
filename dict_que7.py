test_list =  [
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
# this will print unic value
res=[]
# take empty list for make new list
for i in range(0,len(test_list)):
    # loop run till len of list
    for j in test_list[i]:
        # chek j element in list
        if test_list[i][j] not in res:
            # append value
            res.append(test_list[i][j])
print(res)
