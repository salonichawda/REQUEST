import requests

import json

import os 

file=os.path.exists("courses.json")

if file==False:

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
    a=os.path.exists(str(idd)+".json")
    # next(i)
    url="https://api.merakilearn.org/courses/"+str(idd)+"/exercises"

    get_data=requests.get(url)

    data=get_data.json()

    file=open(idd+".json","w")

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


elif file==True:

    my_file=open("courses.json","r")

    get_url=json.load(my_file)

    serial=0
    for i in range(len(get_url)):

        for k,v in get_url[i].items():

            if k=="name":

                serial+=1

                print(serial, v,'-',get_url[i]['id'])

    choose=int(input("which course do you want please enter:-"))

    idd=get_url[choose-1]['id']
    file=os.path.exists(idd+".json")

    if file==False:
        url="https://api.merakilearn.org/courses/"+str(idd)+"/exercises"

        get_data=requests.get(url)

        data=get_data.json()

        file=open(idd+".json","w")

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
    elif file==True:
        my_file=open(idd+".json","r")

        data=json.load(my_file)


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
        file=os.path.exists("list1.json")

        file1=os.path.exists("list2.json")

        if file==True and file1==True:

            a=open("list1.json","r")

            b=json.load(a)

            a=open("list2.json","r")

            b=json.load(a)

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
        else:
            print("file does not exists") 