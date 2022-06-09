str1=input("Enter string:")
str2=input("Enter another string:")
dict1={}
dict2={}
for i in str1:
	dict1[i]=str1.count(i)
print(dict1)
for i in str2:
	dict2[i]=str2.count(i)
print(dict2)
length=len(dict1)
count=0
if len(str1)!=len(str2):
	print("Not anagrams to each other")
else:
	for k in dict1.keys():
		if k in dict2.keys() and dict1[k]==dict2[k]:
			count+=1
if count==length:
	print("They are anagrams of each other")
else:
	print("not anagrams")	

