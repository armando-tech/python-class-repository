import random  

def main():
    grades = []  #empty list variable

    # Loop collect grades from the user
    while True:
        grade = int(input("Please enter a grade or -1 to stop: "))
        if grade == -1:
            break  
        grades.append(grade)  # Adding grade to a list

    print(grades)

    # remove lowest grade
    lowest_grade = min(grades)
    grades.pop(grades.index(lowest_grade))  
    print("Removing lowest grade:\n", grades)

    # removal of a random grade
    random_grade = random.choice(grades)      
    grades.remove(random_grade)
    print("Removing random grade\n", grades)

    # Edit a grade
    print("\nEdit a grade:")
    for index in range(len(grades)):
        print(f"{index + 1}. {grades[index]}")
    
    
    while True:
        index = int(input("Which grade do you want to edit: ")) - 1
        if 0 <= index < len(grades):
            new_grade = int(input("Enter the new grade: "))
            grades[index] = new_grade  
            break
        else:
            print("Enter a valid grade!")
    print(grades)

    #sort and reverse list
    grades.sort()
    grades.reverse()
    print("Sorting and Reversing List\n",grades)
   
   #getting grade total and average. 
    print("\nGetting Grade Total and Average") 
    total = sum(grades)
    average = total / len(grades)
    print(f"Total: {total}\n Average: {average}")
    
    #Completion message
    print("\nCompleted by, Armando Gaona")

#main function
if __name__ == "__main__":
    main()
