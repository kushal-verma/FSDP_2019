

import pymongo
import dns

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

client = pymongo.MongoClient("mongodb+srv://lakshya:%40123lakshya@cluster0-p1mqb.mongodb.net/test?retryWrites=true&w=majority")


mydb=client.university

def add_student(sname, sage, sroll, sbranch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.student.insert_one(
            {
            "Student_Name" : sname,
            "Student_Age" : sage,
            "Student_Roll_no" : sroll,
            "Student_Branch" : sbranch
            })
    return "Student added successfully"


def fetch_all_student():
    user = mydb.student.find()
    for i in user:
        print (i)




add_student('Sylvester', 19, 50, 'CSE')
add_student('Yogendra', 20, 70, 'ME')
add_student('Pradeep', 19, 30, 'IT')
add_student('Kunal', 18, 31, 'EC')
add_student('Devendra', 20, 36, 'IT')
add_student('Lakshya', 19, 59, 'CSE')
add_student('Aditya', 17, 23, 'EE')
add_student('Abhishek', 19, 10, 'ME')
add_student('Kushal', 18, 67, 'CE')
add_student('Aman', 20, 76, 'EC')

fetch_all_student()