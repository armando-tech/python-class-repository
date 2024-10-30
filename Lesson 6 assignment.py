# student_information.py

def main():
    # Create an empty dictionary to store student information
    student_info = {}
   

    #student entries
    student_info["Mando"] = {"ID": "1", 
                               "GPA": 3.9, 
                               "Credits": 55.0, 
                               "Grades": [96, 92, 97, 100]}
    student_info["Jose"] = {"ID": "2", 
                              "GPA": 3.6, 
                              "Credits": 30.0, 
                              "Grades": [91, 94, 79, 81]}

    # Print dictionary contsaining all student info
    print("Student Information Dictionary:")
    print(student_info)
   



# Print student names heading
    print("\nList of Student names")
    for student in student_info:          
        print(student)
    

   
   
   
    #announcing the accessing of students information
    print("\nAccessing of student information")
    print("Student\tID\tGPA\tCredits\t\tGrades")             #using \t tab everything in the correct ordeer.
    
    for name, info in student_info.items():
        print(f"{name}\t{info["ID"]}\t{info["GPA"]}\t{info["Credits"]}\t\t{info["Grades"]}")

   
    print("\nAccessing Student information using Key in a Loop")
    for key in student_info:
        print(key,student_info[key])
    

   
   
   # Removing a student
    student_info.pop("Jose")                    #using the pop method to remove jose
    print("\nRemoving Jose from student registry")
    print(student_info)

   
   
    # Access GPA information
    print("\nGetting Mando GPA")
    for name in student_info:
        print(f"{student_info[name]["GPA"]}")

    
    
    
    
    
    # Clear the student registry
    print("\nCleared Student Registry:")
    student_info.clear()
    print(student_info)

   
   
   
    # Completion
    print("\nCompleted by, Armando Gaona")




#main function
if __name__ == "__main__":
    main()
    