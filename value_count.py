dic = [
    {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}]
count=0
a={}
# for i in dic:
#     if isinstance(dic[i],list):
#         count+=len(dic[i])
# print(count)
for i in range(0,len(dic)):
    for j in dic[i]:
        count=count+1
    print(count)

