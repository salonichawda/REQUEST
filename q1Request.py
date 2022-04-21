import requests

import json

a=requests.get("https://api.merakilearn.org/courses")

get_url=a.json()

my_file=open("courses.json","w")

b=json.dump(get_url, my_file,indent=6)

serial=0
for i in range(len(get_url)):

    for k,v in get_url[i].items():

        if k=="name":

            serial+=1

            print(serial, v,'-',get_url[i]['id'])

choose=int(input("which course do you want please enter:-"))

idd=get_url[choose-1]['id']
# next(i)
url="https://api.merakilearn.org/courses/"+str(idd)+"/exercises"

get_data=requests.get(url)

data=get_data.json()

file=open("courses_exercises.json","w")

json.dump(data, file,indent=6)

print(get_url[choose-1]['name'],'-',get_url[choose-1]['id'])

serial=1
serial1=1
list1=[]
list2=[]
for i in data['course']['exercises']:
    if i['parent_exercise_id']==None:
        print(serial,i['name'])
        print("  ",serial1,i['slug'])
        serial+=1
        list1.append(i)
        list2.append(i)
        # continue
    elif i['parent_exercise_id']==i['id']:
        
        print(serial,i['name'])
        serial+=1
        list1.append(i)
        new_no=1
    elif i['parent_exercise_id']!=i['id']:
        
        print("  ",new_no,i['name'])
        new_no+=1
        list2.append(i)
        # break
file=open("list1.json","w")

json.dump(list1, file,indent=6)

file=open("list2.json","w")

json.dump(list2, file,indent=6)

parent_id=int(input("which parent id you want please enter:-"))

serial=1

idd=list1[parent_id-1]['id']
       
for i in list1:

    if i['parent_exercise_id']==i['id']:

        print(serial,list1[parent_id-1]['name'])
        serial+=1
        break
    else:
        if i['parent_exercise_id']!=i['id']:
            print(serial,list1[parent_id-1]['name'])

            print(" ",list1[parent_id-1]['content'])
            serial+=1
            break
l=[]
l1=[]
new_no=1
idd=list1[parent_id-1]['id']

for j in list2:
    
    if j['parent_exercise_id']==idd:

        print(" ",new_no,j['name'])

        l.append(j['name'])
        l1.append(j['content'])

        new_no+=1

child_id=int(input("which child id do you want please enter:-"))

# idd=l1[child_id-1]
# for i in idd:

#     print(i)


for i in range(len(l)):
    if child_id-1==i:
        print(l[i])
        print(l1[i])
        break
        








# d={'c':{'2':3,'3':9,'e':[{'2':4,'3':5},{'2':5,'3':4,'5':4}]}}

# for i in range(len(d)):
#     for j in d[i]:
#         for a in j['e']:
#             for k,v in a.items():
#                 print(k,v)
#                 # if d[i][j][a]['3']==4:
#                     print(i+1,v)
#     for 

# idd=d[a-1]['3']

# print(idd)
    



# l=[10,12,10,12,13,23,10,10]
# l1=[]
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[i]==l[j]:
#             del l[i], l[j]
#         else:
#             l1.append([l[i],l[j]])

# print(l1)

    










# You have to take a user input 
# and check whether its last digit 
# is 3 or not and if it is 3 then it 
# is divisible by 3 or not.




# Take a user input and 
# check if it is negative or positive 
# if negative So positive number should come in the output 
# and if positive then negative should come


# Take values of length and breadth of a rectangle
#  from user and check if it is square or not.


# A company decided to give bonus of 5% to employee 
# if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and
#  print the net bonus amount.


# Take three int values from user and print greatest among them.


#  Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if 
# the year is century year like 2000, 1900, 2100 then it must be 
# divisible by 400.


# l=[10,101,100,10101]
# l1=[]
# l2=[]
# for i in range(len(l)):
    
#     l[i]=str(l[i])

#     str1=""

#     for j in l[i]:

#         if j!='0':
    
#             str1+=j
        
#     l1.append(int(str1))
        

# print(l1)




# l=['jyoti','salonii','aarti','ashu','ayush','ranu','chawdaa']
# mx_len=len(l[0])
# l1=[]
# for i in range(len(l)):
#     # for j in l[i]:
#         if len(l[i])>mx_len:
    
#             mx_len=len(l[i])

#         if len(l[i])==mx_len:
            
#             l1.append(l[i])

# print(mx_len)

# print(l1)



# l1=[]
# for i in l:
#     for j in l:
#         if len(i)>len(j):
#             print(len(i))
#             l1.append(i)
#         break
# print(l1)






# list1=[3,5,-1,4,6,10]
# l=[]
# max=list1[0]
# for i in range(len(list1)):
#     if list1[i]>max:
#         max=list1[i]
#     l.append(max)
# print(l)

# list=[1,1,0,1,1,1,0,1]

# count=0

# l=[]
# i=0
# for i in range(len(list)-1):
#     if list[i]==0:
#         count+=1 
#     l.append(count)
# print(l)



a=[1,2,3,4,5]

# b=d={}
# for i in a:
#     d[i]={}
#     d=d[i]                           
# print(b)

# i=len(a)-1

# d={}

# while i>=0:

#     d={a[i]:d}

#     i-=1

# print(d)



# l=[[1,2,3],[4,5,6]]

# d={1:[2,3],4:[5,6]}
# d={}
# for i in l:

#         d.update({i[0]:[i[1],i[2]]})

# print(d)




# d={}
# i=0
# while i<len(l):
#     j=0
#     a=l[i][j]
#     while j<len(l[i]):
#         if l[i][j]==a:
#             del l[i][j]
#         else:
#             d.update({a:l[i]})
#         j+=1
#     i+=1

# print(d)
