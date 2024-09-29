first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
current_year = int(input("Enter the current year: "))
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print()
print("Hello " + first_name + " " +last_name)
print("You are " +str(age) + " years old this year")
print()
age += 1
print(f"In the next year 2025, you will be {age} years old in {current_year +1}.")
print("Completed by, [Armando Gaona]")
                 
