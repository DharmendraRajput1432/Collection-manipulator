# Project_3:>>   Collection Manipulator - Student Data Organizer

# empty List to store student records
students = []  
print("\nWelcome to the Student Data Organizer!\n")
while True:
    print("\nSelect An Option : \n")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        print("\nEnter Student Details : ")

        student_id = input("Enter Student ID : ")
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        grade=input("Enter Grade : ")
        dob = input("Enter Date of Birth (YYYY-MM-DD) : ")
        subjects = input("Enter Subjects (comma separated) : ").split(",")

        #Remove extra spaces
        subjects = [sub.strip() for sub in subjects]

        # Store as Set (unique subjects)
        subject_set = set(subjects)

        # Store DOB and ID as Tuple (Immutable)
        tup_id = (student_id)
        tup_dob=(dob)

        # Dictionary
        student = {
            "tup_id"    : student_id ,
            "name"      : name,
            "age"       : age,
            "grade"     :grade,
            "tup_dob"   : dob,
            "subjects"  : subject_set
        }

        students.append(student)

        print("\nStudent added successfully!...")


    elif choice == 2:
        if len(students) == 0:
            print("\nNo records found!...")
            
        else:
            print("\n------ Student Records! ------\n")

            for student in students:
                
                print("Student Id         : ",(student["tup_id"]))
                print("Student Name       : ",(student["name"]))
                print("Student Age        : ",(student["age"]))
                print("Student Grade      : ",(student["grade"]))
                print("Student Dob        : ",(student["tup_dob"]))
                print("Student Subjects   : ",(",".join(student["subjects"])))
                print("")


    elif choice == 3:
        sid1 = input("\nEnter Student ID to Update : ")

        if len(students)==0:
            print("\nStudent ID not found!...")

        for student in students:

            if student["tup_id"]!= sid1: 
                print("\nStudent Id Not Found!...")

            if student["tup_id"]== sid1:

                new_name = input("Enter New Name : ")

                if new_name != "":
                    student["name"] = new_name


                age = int(input("Enter New Age : "))

                if age != "":
                    student["age"] = age

                grade =(input("Enter New Grade : "))

                if grade != "":
                    student["grade"] = grade

                new_subject = input("Enter New Subjects : ")

                
                if new_subject != "":
                    student["subjects"]=set(new_subject .split(","))
                    print("\nStudent Updated Successfully!...")
            break
          

    elif choice == 4:
    
        sid = input("\nEnter Student ID to Delete : ")

        found = False

        for i in range(len(students)):
            if students[i]["tup_id"]==sid:
                del students[i]
                found = True
                print("\nStudent Deleted Successfully!")
                break

        if not found:
            print("\nStudent ID Not Found!")
        

    elif choice == 5:
        new_subject=set()
        

        for student in students:
            new_subject=(student["subjects"])
    

        if len(new_subject) == 0:
            print("\nNo Subjects Available.")
        else:
            print("\nSubjects Offered :")
            for subject in (new_subject):
                print(subject,end=", ")

    elif choice == 6:
        print("\nThank you for using Student Data Organizer!.....\n")
        break

    else:
        print("\nInvalid Choice!....")