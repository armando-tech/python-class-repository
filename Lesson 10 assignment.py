def main():
    print("Welcome to the String Replacement Program!")
    print("-" * 75)
    
    
    # Obtain the main string and substring to search
    string = get_user_input("Please enter string to search through: ")
    substring = get_user_input("Please enter string to search for: ")
    
    # Check substring is in main string and get index
    index = find_substring(string, substring)
    

    # If substring is found update string
    if index != -1:  
        if ask_yes_no("Would you like to replace with something else? (yes or no): "):
            new_string = get_user_input("Please enter the new string: ")
            updated_string = string.replace(substring, new_string)
            print(f"Updated string: {updated_string}")
        else:
            print("No replacement was made.")
    
    
#return user input
def get_user_input(prompt):
    return input(prompt)

#determine if the sub string is within the main function
def find_substring(string, substring):
  
  #.find() returns -1 if not found
    index = string.find(substring)          
    if index != -1:
        print(f"The substring '{substring}' was found at index {index}.")
    else:
        print(f"The substring '{substring}' was not found.")
    return index

#yes or no response from user.
def ask_yes_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no"]:
            return response == "yes"
        print("Invalid input. Please enter 'yes' or 'no'.")


# Run the main function
if __name__ == "__main__":
    main()


print("Thank you for using our program!")
print("Completed by, Armando Gaona")
