class students():
    name:str
    age:int
    std_id:int
    entry:str
    father_name:str
    address:str
    personal_phone_no:str
    parent_phone_no:str
    courses_in_withprice={}
    courses_and_price={'Accounting':10000,'Finance':8500,'English':4000}

    #Function to save a Student information into a File
    def save_tofile(self):
        filename=open('std_information','a')
        filename.write(self.name+',')
        filename.write(str(self.age)+',')
        filename.write(self.address+',')
        filename.write(self.entry+',')
        filename.write(self.father_name+',')
        filename.write(self.personal_phone_no+',')
        filename.write(self.parent_phone_no+',')

        no_ofcourse=self.courses_in_withprice.keys()
        temp_course_fees=0
        for i in no_ofcourse:
            temp_course_fees=self.courses_in_withprice.get(i)
            filename.write(i+',')
            filename.write(temp_course_fees+',')

        filename.write('\n')
        filename.close()



def add_student():
    print('Enter Student Credentials: ')
    temp_obj=students()
    temp_name=input("Enter Name: ")
    temp_obj.name=temp_name
    temp_age=input("Enter Age: ")
    temp_obj.age=temp_age
    temp_entry=input("Enter Entry Date Of Student in MM/DD/YY Format : ")
    temp_obj.entry=temp_entry
    temp_father_name=input("Enter Father Name: ")
    temp_obj.father_name=temp_father_name
    temp_address=input("Enter adderss: ")
    temp_obj.address=temp_address
    temp_phone_no=input("Enter Student Phone No: ")
    temp_obj.personal_phone_no=temp_phone_no
    temp_parent_phone_no=input("Enter Parent Phone No: ")
    temp_obj.parent_phone_no=temp_parent_phone_no

    print("Enter Number Of Course To Enter: ")
    temp_decision=input("Enter: ")
    for i in range(0,int(temp_decision)):
        temp_course_name=input("Enter Course Name :")
        temp_course_price=input("Enter Course Fees: ")
        temp_obj.courses_in_withprice[temp_course_name]=str(temp_course_price)

    print("Are you sure to Make this Entry")
    print("yes or no")
    temp_decision=input("Enter: ")
    if(temp_decision.lower()=='yes'):
        temp_obj.save_tofile()
        print('Entry Process is Successful')
        return temp_obj
    else:
        print('Entry Process is Terminated Without Entry')
        return 0

def read_previous_students():
    filename=open('std_information','r')
    student_list=[]

    for i in filename.readlines():
        temp_str=i
        student_list.append(temp_str)
        temp_str=0

    filename.close()
    return student_list

def students_search(students_list,actual_name):
#Search By Name
    for i in students_list:
        if(i.name==actual_name):
            print('--------------------------------------------------------')
            print('Name: ' + i.name)
            print('Age: ' + i.age)
            print('Entry Date: ' + i.entry)
            print('Father Name: ' + i.father_name)
            print('address: ' + i.address)
            print('Student Phone No: ' +i.personal_phone_no)
            print('Parent Phone No:' + i.parent_phone_no)
            print('--------------------------------------------------------')

            print('\n')
    return 0

def students_complete_information(students_list):
    for i in students_list:
        print('--------------------------------------------------------------')
        print('Name: ' + i.name)
        print('Age: ' + i.age)
        print('Entry Date: ' + i.entry)
        print('Father Name: ' + i.father_name)
        print('address: ' + i.address)
        print('Student Phone No: ' +i.personal_phone_no)
        print('Parent Phone No:' + i.parent_phone_no)
        print('--------------------------------------------------------------')

    return 0

def recreating_student_Object(students_info):
    temp_list=[]
    obj_list=[]
    temp_obj:object
    #seperate attribute from list with ,

    for i in students_info:
        temp_list=i.split(",")
        temp_obj=students()
        temp_obj.name=temp_list[0]
        temp_obj.age=temp_list[1]
        temp_obj.address=temp_list[2]
        temp_obj.entry=temp_list[3]
        temp_obj.father_name=temp_list[4]
        temp_obj.personal_phone_no=temp_list[5]
        temp_obj.parent_phone_no=temp_list[6]
        obj_list.append(temp_obj)
        #print(temp_list)

    #then create object Array

    return obj_list

def cancel_student_entry(student_list,std_name):
    list_index=0
    k=0
    std_temp_list=[]
    for i in student_list:
        if(i.name==std_name):
            break
        list_index=list_index+1

    #print((student_list[0].name))
    filename=open('std_information','w')
    for j in range(0,len(student_list)):

        if(j!=list_index):
            filename.write(student_list[j].name+',')
            filename.write(str(student_list[j].age)+',')
            filename.write(student_list[j].address+',')
            filename.write(student_list[j].entry+',')
            filename.write(student_list[j].father_name+',')
            filename.write(student_list[j].personal_phone_no+',')
            filename.write(student_list[j].parent_phone_no+',')
            filename.write('\n')


    filename.close()




    return  0

def update_student_information(student_list,std_name):
    list_index=0
    k=0
    std_temp_list=[]
    for i in student_list:
        if(i.name==std_name):
            #Enter Data
            print("Enter 1)Change Name \n 2)Change Age \n 3)Change Entry Date \n 4)Change Fathername \n 5)Change Address \n 6)Change Phone No \n 7)Change Parent Phone no \n 8)Update Course")
            temp_decision_2=input("Enter: ")
            print('Enter Student Credentials: ')
            #temp_obj=students()

            if(temp_decision_2=='1'):
                temp_name=input("Enter Name: ")
                i.name=temp_name
            elif(temp_decision_2=='2'):
                temp_age=input("Enter Age: ")
                i.age=temp_age
            elif(temp_decision_2=='3'):
                temp_entry=input("Enter Entry Date Of Student in MM/DD/YY Format : ")
                i.entry=temp_entry
            elif(temp_decision_2=='4'):
                temp_father_name=input("Enter Father Name: ")
                i.father_name=temp_father_name
            elif(temp_decision_2=='5'):
                temp_address=input("Enter adderss: ")
                i.address=temp_address
            elif(temp_decision_2=='6'):
                temp_phone_no=input("Enter Student Phone No: ")
                i.personal_phone_no=temp_phone_no
            elif(temp_decision_2=='7'):
                temp_parent_phone_no=input("Enter Parent Phone No: ")
                i.parent_phone_no=temp_parent_phone_no

            elif(temp_decision_2=='8'):
                print("Enter Number Of Course To Enter: ")
                temp_decision=input("Enter: ")
                for j in range(0,int(temp_decision)):
                    temp_course_name=input("Enter Course Name :")
                    temp_course_price=input("Enter Course Fees: ")
                    i.courses_in_withprice[temp_course_name]=str(temp_course_price)

        #list_index=list_index+1

    #print((student_list[0].name))
    filename=open('std_information','w')
    for j in range(0,len(student_list)):
        filename.write(student_list[j].name+',')
        filename.write(str(student_list[j].age)+',')
        filename.write(student_list[j].address+',')
        filename.write(student_list[j].entry+',')
        filename.write(student_list[j].father_name+',')
        filename.write(student_list[j].personal_phone_no+',')
        filename.write(student_list[j].parent_phone_no+',')
        filename.write('\n')
    filename.close()
    return 0


students_list=read_previous_students()
obj_list=recreating_student_Object(students_list)



for i in range(0,6):
    print('Select Option:\n 1)For Student Entry \n 2)View Students Complete Detail \n 3)Search Student By Name \n 4)Cancel the Entry \n 5)Update information')
    temp_decision=input("Enter: ")
    if(temp_decision=='1'):
        temp_obj=add_student()
    elif(temp_decision=='2'):
        students_complete_information(obj_list)
    elif(temp_decision=='3'):
        temp_name=input('Enter Name to Search Studenet: ')
        students_search(obj_list,temp_name)
    elif(temp_decision=='4'):
        temp_name=input('Enter Name to Cancel Studenet: ')
        cancel_student_entry(obj_list,temp_name)
    elif(temp_decision=='5'):
        temp_name=input('Enter Name to Cancel Studenet: ')
        update_student_information(obj_list,temp_name)

    else:
        print("No Such Fucntionality Yet")
    students_list=read_previous_students()
    obj_list=recreating_student_Object(students_list)
    print('\n')
    print('#####################################################')
    print('\n')
