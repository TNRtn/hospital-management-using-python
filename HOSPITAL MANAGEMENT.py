#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import getpass
def doctorsignin():
    print("=========================")
    f = open('doctor.csv', 'a', newline='\r')
    s = csv.writer(f)
    docname = input("Enter name of the doctor :- ")
    docid = input("Enter the id : ")
    password = getpass.getpass("Enter the password : - ")
    special = input("Enter specilization : ")
    exp = input("Enter the experience : ")
    r = [docname, docid, password, special, exp]
    s.writerow(r)
    f.close()
    print("patient information successfully saved ")
    print("Patient Record Saved")
    input("Press any key to continue..")
def doctorlogin():
    print("\n\n")
    ch = input("Enter ypur id : ")
    passwd =input("Enter your password : ")
    f = open('doctor.csv', 'r', newline="\r\n")
    s = csv.reader(f)
    for r in s:
        if r[1] == r or r[2] == passwd:
            print("-------------------------------")
            print("Doctor name :", r[0])
            print("Doctor id :", r[1])
            print("Specalization : ", r[3])
            print("Experience : ", r[4])
            print("successfully login completed")
            print("you can proceed for further information ")
            menu()
            print("💊" * 20)
    else:
              print("Invalid !............")
              print("incorrect password and id,please verify")
               # print("please verify")
    f.close()
    input("press any key to continue....")
def newPatient():
    print("*******WELCOME******")
    print("Add a new Patient Record")
    print("please fill the following file with data ")
    print("=========================")
    f = open('srm.cse.v.csv', 'a', newline='\r\n')
    s = csv.writer(f)
    Patientid = input('Enter Patient id=')
    Patientname = input('Enter Patient name=')
    Disease = input('Enter Disease=')
    fee = float(input('Enter Fee='))
    Doctorname = input('Enter name of Doctor=')
    phno = input("Enter mobile number of the patient : ")
    patientgardian = input("Enter name of the patient gardian :-")
    print("----------------------------------------------------")
    rec = [Patientid, Patientname, Disease, fee, Doctorname, phno, patientgardian]
    s.writerow(rec)
    f.close()
    print("patient information successfully saved ")
    print("Patient Record Saved")
    input("Press any key to continue..")


def editPatient():
    print("Modify a Patient Record")
    print("=========================")
    f = open('srm.cse.v.csv', 'r', newline='\r\n')
    f1 = open('temp.csv', 'w', newline='\r\n')
    f1 = open('temp.csv', 'a', newline='\r\n')
    r = input('Enter Patientid whose record you want to modify=')
    s = csv.reader(f)
    s1 = csv.writer(f1)
    for rec in s:
        if rec[0] == r:
            print("💊" * 20)
            print("Patient id=", rec[0])
            print("Patient Name=", rec[1])
            print("Disease=", rec[2])
            print("Fee=", rec[3])
            print("Name of Doctor=", rec[4])
            print("Mobile number of the patien : ", rec[5])
            print("Patient gardian name : ", rec[6])
            print("💊" * 20)

            choice = input("Do you want to modify this Patient Record ? (y/n)=")
            if choice == 'y' or choice == 'Y':
                print("💊"*20)
                Patientid = input('Enter new Patient id(if required)=')
                Patientname = input('Enter new Patient name(if required)=')
                Disease = input('Enter Disease=')
                fee = float(input('Enter Fee='))
                Doctorname = input('Enter name of Doctor=')
                phno = input("Enter the patient mobile number : ")
                patientgardian = input("Enter the patient gardian name : ")
                print("💊" * 20)
                rec = [Patientid, Patientname, Disease, fee, Doctorname, phno, patientgardian]
                s1.writerow(rec)
                print("Patient Record Modified")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("srm.cse.v.csv")
    os.rename("temp.csv","srm.cse.v.csv")

    input("Press any key to continue..")


def delPatient():
    f = open('srm.cse.v.csv', 'r', newline='\r\n')
    f1 = open('temp.csv', 'w', newline='\r\n')
    f1 = open('temp.csv', 'a', newline='\r\n')
    r = input('Enter Patientid whose record you want to delete')
    s = csv.reader(f)
    s1 = csv.writer(f1)
    for rec in s:
        if rec[0] == r:
            print("-------------------------------")
            print("Patient id=", rec[0])
            print("Patient Name=", rec[1])
            print("Disease=", rec[2])
            print("Fee=", rec[3])
            print("Name of Doctor=", rec[4])
            print("Mobile number of the patient : ", rec[5])
            print("gardian of the patient : ", rec[6])
            print("💊" * 20)
            choice = input("Do you want to delete this Patient Record(y/n)")
            if choice == 'y' or choice == 'Y':
                pass
                print("Patient Record Deleted....")
            else:
                s1.writerow(rec)
        else:
            s1.writerow(rec)
    f.close()
    f1.close()
    os.remove("srm.cse.v.csv")
    os.rename("temp.csv", "srm.cse.v.csv")

    input("Press any key to continue..")


def searchPatient():
    print("Search a Patient Record")
    print("💊" * 20)
    f = open('srm.cse.v.csv', 'r', newline='\r\n')
    r = input('Enter Patientid you want to search')
    s = csv.reader(f)
    for rec in s:
        if rec[0] == r:
            print("-------------------------------")
            print("Patient id=", rec[0])
            print("Patient Name=", rec[1])
            print("Disease=", rec[2])
            print("Fee=", rec[3])
            print("Name of Doctor=", rec[4])
            print("Mobile number of the patien : ", rec[5])
            print("Gardian of the patien : ", rec[6])
            print("💊" * 20)
    f.close()
    input("Press any key to continue..")


def listofPatients():
    print("💊" * 20)
    print("\t\t\t List of All Patients")
    print("💊" * 20)
    f = open('srm.cse.v.csv', 'r', newline='\r\n')
    s = csv.reader(f)
    i = 1
    for rec in s:
        print(rec[0], end="\t\t")
        print(rec[1], end="\t\t")
        print(rec[2], end="\t\t")
        print(rec[3], end="\t\t")
        print(rec[4], end="\t\t")
        print(rec[5], end="\t\t")
        print(rec[6], end="\t\t")
        i += 1
    f.close()
    print("💊" * 20)
    input("Press any key to continue..")


def menu():
    choice = 0
    while choice != 6:
        print("\n")
        print("🧑‍⚕️" * 20)
        print("🧑‍⚕️")
        print("\t\t 🌳🌳🌳 WELCOME TO SRM HOSPITAL 🌳🌳🌳")
        print("🧑‍⚕️")
        print("🧑‍⚕️" * 20)
        print("🩺" * 20)
        print("\t\t 🏥🏥🏥 MENU 🏥🏥🏥")
        print("\n\n")
        print("1. Add a new Patient Record")
        print("2. Modify Existing Patient information ")
        print("3. Delete Existing Patient informatino ")
        print("4. Search Patient information")
        print("5. List all Patients")
        print("6. Exit")
        print("-------------------------------")
        choice = int(input('Enter your choice'))
        print("-------------------------------")
        if choice == 1:
            newPatient()
        elif choice == 2:
            editPatient()
        elif choice == 3:
            delPatient()
        elif choice == 4:
            searchPatient()
        elif choice == 5:
            listofPatients()
        elif choice == 6:
            choice=6
            print("THANK YOU FOR VISITING ")
            print(quit)
            quit()


def doctormenu():
    t=0
    while t != 3:
        print("\n\n")
        print("🧑‍⚕️" * 20)
        print("🧑‍⚕️")
        print("\t\t 🌳🌳🌳 WELCOME TO SRM HOSPITAL 🌳🌳🌳")
        print("🧑‍⚕️")
        print("🧑‍⚕️" * 20)
        print("🩺" * 20)
        print("\t\t 🏥🏥🏥 MENU 🏥🏥🏥")
        print("\n\n")
        print("1.RIGISTER/SIGN IN")
        print("2.Login")
        print("3.exit")
        print("-------------------------------")
        ch = int(input('Enter your choice : '))
        print("-------------------------------")
        if ch == 1:
            doctorsignin()
        elif ch == 2:
            doctorlogin()
        else:
            t=3
            print("\n THANKYOU FOR VISITING ")
            print(quit)
            quit()


doctormenu()


# In[ ]:





# In[ ]:





# In[ ]:




