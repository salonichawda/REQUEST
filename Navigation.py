import requests
import json

url=requests.get('https://api.merakilearn.org/courses')
r=json.loads(url.text)
# print(r)
with open("requts.json","w") as f:
    json.dump(r,f,indent=4)
i=0
while i<len(r):
    print(i+1,r[i]["name"],r[i]["id"])
    i+=1
print(" ")    
course_no=int(input("select which course you want display  :"))
print(course_no,r[course_no-1]["name"])
course_id=r[course_no-1]["id"]

url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
deta=json.loads(url1.text)
with open("parent.json","w") as f2:
    json.dump(deta,f2,indent=6)
print(r[course_no-1]['name'],"-",r[course_no-1]["id"])
i = 0
while i < len(deta["course"]["exercises"]):
    print((i+1),".",deta["course"]["exercises"][i]["name"])
    print(deta["course"]["exercises"][i]["slug"])
    i+=1


topic=int(input("enter the topic no:- "))
topic  = topic-1
i = 0
while i < len(deta["course"]["exercises"][topic]["content"]):
    print(deta["course"]["exercises"][topic]["content"][i]["value"])
    print()
    i+=1
while topic <= len(deta["course"]["exercises"]):
    next_previuos = input("previous or next(p&n):")
    if  next_previuos == "p": 
        topic-=1
        if next_previuos == "p" and topic >=1:
            print(deta["course"]["exercises"][topic]["name"],"\n")
            i = 0 
            while i < len(deta["course"]["exercises"][topic]["content"]):
                print(deta["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
                
        else :
            i = 0
            while i < len(deta):
                print(str(i+1),deta["course"]["exercises"][i]["name"])
                i+=1
    elif  next_previuos == "n":
        topic+=1
        if next_previuos == "n" and topic < len(deta["course"]["exercises"]):
                print(deta["course"]["exercises"][topic]["name"],"\n")
                i = 0 
                while i < len(deta["course"]["exercises"][topic]["content"]):
                    print(deta["course"]["exercises"][topic]["content"][i]["value"])
                    i+=1
        if topic+1 == len(deta["course"]["exercises"]):
            print("topic is completed.")
            break

    elif next_previuos=="stop":
        break    
    else:
        print("wrong user_input ")
        break