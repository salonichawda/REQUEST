# l=[23,45,78,90,65]
# l1=[]
# for i in range(len(l)):
#     l[i]=str(l[i])
#     count=0
#     for j in range(len(l[i])):
#         count+=int(l[i][j])
#     l1.append(count)
# print(l1)

# l1=[]
# i=0
# while(i<len(l)):
#     k=str(l[i])
#     count=0
#     j=0
#     while(j<len(k)):
#         count+=int(k[j])
#         j+=1
#     l1.append(count)
#     i+=1
# print(l1)


# l=[0,25,50,100]
# l1=[]
# for i in l:

#     l1.append(i+1)
# print(l1)

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]

# list1[2][1][2].extend(sub_list)

# print(list1)

# l1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# for i in l1:
#     if not i:
#         l1.remove(i)
# print(l1)


# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revere Number ", reverse_number)