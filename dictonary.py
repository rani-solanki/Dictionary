thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
   print(x)
   print(thisdict[x])
#    use of value()
for x in thisdict.values():
   print(x)
#    it will print keys and value
for x, y in thisdict.items():
  print(x, y)
#   chek the value
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")   
# change value
thisdict["year"] = 2018
print(thisdict)
thisdict["color"] = "red"
print(thisdict)
# select same value
x = thisdict["model"]
x = thisdict.get("model")
print(x)
