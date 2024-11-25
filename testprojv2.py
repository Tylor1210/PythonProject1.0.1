users = {}

# Function to log user actions to a file
def log_to_file(message):
    with open("user_activity.log", "a") as file:
        file.write(message + "\n")

def signup():
    print("\n--- Signup ---")
    username = input("Choose a username: ")

    # Check if username already exists
    if username in users:
        print("Username already taken. Try a different one.")
        log_to_file(f"Signup attempt failed: Username '{username}' already exists.")
    else:
        password = input("Choose a password: ")
        users[username] = password
        print("Signup successful! You can now log in.")
        log_to_file(f"New signup: Username '{username}' registered successfully.")

def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username exists and password matches
    if username in users and users[username] == password:
        print(f"Login successful! Welcome, {username}.")
        log_to_file(f"Login successful for user '{username}'.")
        quiz_menu(username)
    else:
        print("Login failed. Incorrect username or password.")
        log_to_file(f"Login failed for username '{username}'.")

def quiz_menu(username):
    print("\nWelcome to the Programming Quiz!")
    print("Choose a level:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    choice = input("Enter your choice (1-3): ")
    score = 0

    if choice == "1":
        topic_1()
        topic_2()
        topic_3()
        topic_4()
        topic_5()
        display_lesson()
        score = quiz_beginner()
    elif choice == "2":
        display_lesson()
        score = quiz_intermediate()
    elif choice == "3":
        score = quiz_advanced()
    else:
        print("Invalid choice. Returning to main menu.")
        return

    log_to_file(f"User '{username}' completed a quiz. Level: {choice}, Score: {score}.")
# Put quiz_beginner() here code by: Leidy
def quiz_beginner():
    score = 0 

    print("\n🎓 **Final Quiz: Test Your Knowledge!** 🎓\n")

    # Question 1
    answer1 = input("1. Can a variable store both integers and strings in Python? (yes/no): ").lower()
    if answer1 == "yes":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Actually, variables can store any type of data in Python, so yes!")

    # Question 2
    answer2 = input("\n2. Which of these is a valid variable name?\n(a) 2nd_variable\n(b) _myVariable\n(c) my-variable\n").lower()
    if answer2 == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ The correct answer is (b) _myVariable. Variable names can't start with numbers or contain dashes!")

    # Question 3
    answer3 = input("\n3. Can you modify the value of a variable in Python? (yes/no): ").lower()
    if answer3 == "yes":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Yes! You can modify the value of a variable at any time.")

    # Question 4: input() function
    print("4. What type of data does the input() function return?")
    print("a) Integer")
    print("b) String")
    print("c) Float")
    print("d) Boolean")
    answer1 = input("Enter your answer (a/b/c/d): ")
    if answer1.lower() == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The input() function always returns a string.\n")

    # Question 5: print() function
    print("5. Which of the following is used to display output in Python?")
    print("a) input()")
    print("b) display()")
    print("c) print()")
    print("d) output()")
    answer2 = input("Enter your answer (a/b/c/d): ")
    if answer2.lower() == "c":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The print() function is used for displaying output.\n")

    # Question 6: Formatting Output
    print("6. How would you display a floating-point number with 2 decimal places in Python?")
    print("a) {:.0f}")
    print("b) {:.2f}")
    print("c) {:.3f}")
    print("d) {:.1f}")
    answer3 = input("Enter your answer (a/b/c/d): ")
    if answer3.lower() == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The correct format is '{:.2f}' for rounding to 2 decimal places.\n")
   

    # Final score
    print(f"\nYour final score is: {score}/6")
    if score >= 5:
        print("🎉 Excellent! You are a Python variable pro!")
    elif score >= 4:
        print("👍 Good job! You've got the basics down.")
    else:
        print("📚 You might want to review some material and try again.")

    return score
    

#Put quiz_intermediate() here
def quiz_intermediate():
    score = 0
    print("\n🎓 **Quiz: Test Your Knowledge!** 🎓\n")
    

    # Question 1
    answer = input("1. Can a variable store both integers and strings in Python? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Actually, variables can store any type of data in Python, so yes!")

    # Question 2
    answer = input("\n2. Which of these is a valid variable name?\n(a) 2nd_variable\n(b) _myVariable\n(c) my-variable\n").lower()
    if answer == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ The correct answer is (b) _myVariable. Variable names can't start with numbers or contain dashes!")

    # Question 3
    answer = input("\n3. Can you modify the value of a variable in Python? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Yes! You can modify the value of a variable at any time.")
    #Question 4
    print("\n4. What is a block in programming?(*BONUS POINT IF CORRECT)")
    print("a) A set of statements that belong together as a group")
    print("b) A boolean variable that signals when some condition exists in a program")
    print("c) A set of statements that execute in order in which they appear")
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "a":
        print("✅ Correct")
        score+= 2
    else:
        print("❌ Incorrect, the correct answer is a")
    #Question 5
    print("\n5. What is a flag in programming?")
    print("a) A piece of cloth attached to a pole ")
    print("b) A boolean variable that signals when some condition exists in a program")
    print("c) A decision structure that has only one alternative path execution")
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "b":
         print("✅ Correct")
         score+= 1
    else:
        print("❌ Incorrect, the correct answer is b")
    #Question 6
    print("\n6. Which answer choice defines control structure in programming")
    print("a) A logical design that controls the order in which a set of statements execute")
    print("b) The structure of something that is controlled")
    print("c) The operator that connects two values and determines whether a specific relationship exists between them")
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "a":
        print("✅ Correct")
        score+= 1
    else:
        print("❌ Incorrect, the correct answer is a")

    # Question 7: input() function
    print("7. What type of data does the input() function return?")
    print("a) Integer")
    print("b) String")
    print("c) Float")
    print("d) Boolean")
    answer1 = input("Enter your answer (a/b/c/d): ")
    if answer1.lower() == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The input() function always returns a string.\n")

    # Question 8: print() function
    print("8. Which of the following is used to display output in Python?")
    print("a) input()")
    print("b) display()")
    print("c) print()")
    print("d) output()")
    answer2 = input("Enter your answer (a/b/c/d): ")
    if answer2.lower() == "c":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The print() function is used for displaying output.\n")

    # Question 9: Formatting Output
    print("9. How would you display a floating-point number with 2 decimal places in Python?")
    print("a) {:.0f}")
    print("b) {:.2f}")
    print("c) {:.3f}")
    print("d) {:.1f}")
    answer3 = input("Enter your answer (a/b/c/d): ")
    if answer3.lower() == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The correct format is '{:.2f}' for rounding to 2 decimal places.\n")


    print(f"\nYou scored {score}/9.")
    if score >= 8:
        print("Awsome!!! You're on a roll.")
    elif score >= 6:
        print("Nice job! keep studying.")
    else:
        print("Don't worry, keep practicing.")
    
    return score




#Put quiz_advanced() here-----------------------------------------------------------
def quiz_advanced():
    score = 0
    print("\n🎓 **Quiz: Test Your Knowledge!** 🎓\n")
    
# Question 1
    answer = input("1. Can a variable store both integers and strings in Python? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Actually, variables can store any type of data in Python, so yes!")

    # Question 2
    answer = input("\n2. Which of these is a valid variable name?\n(a) 2nd_variable\n(b) _myVariable\n(c) my-variable\n").lower()
    if answer == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ The correct answer is (b) _myVariable. Variable names can't start with numbers or contain dashes!")

    # Question 3
    answer = input("\n3. Can you modify the value of a variable in Python? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Yes! You can modify the value of a variable at any time.")
    #Question 4
    print("\n4. What is a block in programming?")
    print("a) A set of statements that belong together as a group")
    print("b) A boolean variable that signals when some condition exists in a program")
    print("c) A set of statements that execute in order in which they appear")
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "a":
        print("✅ Correct")
        score+= 1
    else:
        print("❌ Incorrect, the correct answer is a")
    #Question 5
    print("\n5. What is a flag in programming?")
    print("a) A piece of cloth attached to a pole ")
    print("b) A boolean variable that signals when some condition exists in a program")
    print("c) A decision structure that has only one alternative path execution")
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "b":
         print("✅ Correct")
         score+= 1
    else:
        print("❌ Incorrect, the correct answer is b")
    #Question 6
    print("\n6. Which answer choice defines control structure in programming")
    print("a) A logical design that controls the order in which a set of statements execute")
    print("b) The structure of something that is controlled")
    print("c) The operator that connects two values and determines whether a specific relationship exists between them")
    answer = input("Your answer (a/b/c): ").lower()
    if answer == "a":
        print("✅ Correct")
        score+= 1
    else:
        print("❌ Incorrect, the correct answer is a")

    # Question 7: input() function
    print("7. What type of data does the input() function return?")
    print("a) Integer")
    print("b) String")
    print("c) Float")
    print("d) Boolean")
    answer1 = input("Enter your answer (a/b/c/d): ")
    if answer1.lower() == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The input() function always returns a string.\n")

    # Question 8: print() function
    print("8. Which of the following is used to display output in Python?")
    print("a) input()")
    print("b) display()")
    print("c) print()")
    print("d) output()")
    answer2 = input("Enter your answer (a/b/c/d): ")
    if answer2.lower() == "c":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The print() function is used for displaying output.\n")

    # Question 9: Formatting Output
    print("9. How would you display a floating-point number with 2 decimal places in Python?")
    print("a) {:.0f}")
    print("b) {:.2f}")
    print("c) {:.3f}")
    print("d) {:.1f}")
    answer3 = input("Enter your answer (a/b/c/d): ")
    if answer3.lower() == "b":
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect! The correct format is '{:.2f}' for rounding to 2 decimal places.\n")


    print(f"\nYou scored {score}/9.")
    if score >= 8:
        print("Awsome!!! You're on a roll.")
    elif score >= 6:
        print("Nice job! keep studying.")
    else:
        print("Don't worry, keep practicing.")
    
    return score
#LESSONS FOR BEGINNERS BELOW -----------------------------------------------------------------------------------------------------------------------
def topic_1():
    print("\nINSTRUCTIONS: Since you are chose beginner we will go over a few topics and answer some interactive questions before the Quiz. \n")
    print("\n🚀 **Topic 1: What is a Variable?** 🚀\n")
    print("Welcome to the first topic! In Python, a variable is like a box where you can store information. Think of it as a label for a value.")
    print("\nFor example, if you want to store someone's age, you would create a variable and assign the value to it.")
    
    print("\nHere’s an example:\n")
    print('''# Create a variable called 'age' and assign the value 25 to it
age = 25
print(age)  # Output: 25
    ''')

    # Ask the user a question to reinforce the concept
    answer = input("\n🎯 Can you create a variable with the syntax 'age = 25'? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Correct! You've created your first variable!")
    else:
        print("❌ Nope! The syntax 'age = 25' is correct for creating a variable in Python.")
    
    print("\n🎉 You're off to a great start! Let's move on to the next topic!")

def topic_2():
    print("\n💡 **Topic 2: Understanding Different Data Types** 💡\n")
    print("Now that you know how to create a variable, let's explore the different types of data you can store in your variables.")
    print("In Python, a variable can hold many types of values:")
    print("\n1. **Integers (int)**: Whole numbers like 10, -5, 42.")
    print("2. **Floating-point numbers (float)**: Numbers with decimals like 3.14, 0.99, -2.71.")
    print("3. **Strings (str)**: Text values, like 'Hello!', or 'Python'.")
    print("4. **Lists**: A collection of ordered items, like ['apple', 'banana', 'cherry'].")
    print("5. **Booleans (bool)**: True or False values, used for logical operations.")
    
    # Example of data types
    print("\nLet’s see an example of different data types:\n")
    print('''# Integer
num = 10
print(type(num))  # Output: <class 'int'>

# String
greeting = "Hello, world!"
print(type(greeting))  # Output: <class 'str'>
    ''')

    # Interactive question about data types
    answer = input("\n🌟 Can a variable store both numbers and text? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Yes! Python allows variables to store all kinds of data.")
    else:
        print("❌ Actually, variables in Python are dynamic, meaning they can store any type of data!")

    print("\n🚀 You're doing great! Let’s dive into naming your variables in the next topic.")

def topic_3():
    print("\n📝 **Topic 3: Naming Your Variables** 📝\n")
    print("When you create a variable, you need to give it a name. But not just any name! There are a few rules you need to follow.")
    print("\nHere are the key rules for naming variables in Python:")
    print("1. The name must start with a letter (a-z, A-Z) or an underscore (_).")
    print("2. It can contain letters, numbers, and underscores, but no spaces or special characters.")
    print("3. Variable names are **case-sensitive**—'age' and 'Age' are different variables.")
    print("4. Avoid using Python reserved keywords (e.g., 'if', 'while', 'def').")
    
    # Example of valid and invalid variable names
    print("\nLet’s look at some examples:\n")
    print('''# Valid variable names
name = "John"
_age = 25
variable_123 = 100

# Invalid names (commented out)
# 1st_variable = "Error"  # Starts with a number
# my variable = "Oops"  # Contains a space
# def = 10  # 'def' is a reserved keyword
    ''')

    # Interactive question about variable names
    answer = input("\n🎯 Which of the following is a valid variable name?\n(a) 1st_variable\n(b) _age\n(c) my-variable\n").lower()
    if answer == "b":
        print("✅ Correct! '_age' is a valid name. Remember, no spaces or starting with numbers!")
    else:
        print("❌ Oops! The correct answer is (b) _age.")

    print("\n🎉 Nice work! Let’s continue by learning how to assign and modify variables.")

def topic_4():
    print("\n✏️ **Topic 4: Assigning and Modifying Variables** ✏️\n")
    print("In Python, once you create a variable, you can assign a value to it. You can even change that value later in your program!")
    print("\nYou assign a value to a variable using the equals sign (`=`), like so:")
    
    print('''# Assigning a value to a variable
x = 5
print(x)  # Output: 5
    ''')
    
    print("\nBut here's the cool part! You can modify the value of a variable by performing operations on it.")
    print('''# Modifying the value of 'x'
x = x + 10
print(x)  # Output: 15
    ''')

    # Interactive question about variable modification
    answer = input("\n🎯 If 'x' starts at 5, what will be the value of 'x' after 'x = x + 10'? \n(a) 5\n(b) 10\n(c) 15\n").lower()
    if answer == "c":
        print("✅ Correct! After adding 10 to x, the value becomes 15.")
    else:
        print("❌ Oops! The correct answer is (c) 15.")

    print("\n🎉 You’re mastering Python variables! Let’s finish with a quick look at constants.")

def topic_5():
    print("\n🔒 **Topic 5: Constants in Python** 🔒\n")
    print("In Python, there's no built-in constant type, but there’s a naming convention to indicate a constant.")
    print("We use **uppercase** letters to define constants, which are values that shouldn’t change once set.")
    
    print("\nHere’s an example of how to define a constant for the value of Pi:")
    print('''# Defining a constant
PI = 3.14159
print(PI)  # Output: 3.14159
    ''')

    # Interactive question about constants
    answer = input("\n🎯 Is 'PI = 3.14159' an example of using a constant in Python? (yes/no): ").lower()
    if answer == "yes":
        print("✅ Correct! 'PI' is a constant because it's a fixed value.")
    else:
        print("❌ Actually, yes! 'PI' is a constant, commonly used in Python.")


def display_lesson():
    # Intro 
        print("Welcome to the Programming Lesson on Input and Output!\n")
        print("Today, we will cover the following topics:")
        print("1. Understanding Input and Output")
        print("2. The input() function")
        print("3. The print() function")
        print("4. Formatting Output")
        print("5. File Input and Output\n")

    # Lesson on Understanding Input and Output
        print("--- 1. Understanding Input and Output ---")
        print("Input refers to taking data from the user or an external source into the program.")
        print("Output refers to displaying data to the user or sending data to an external source.\n")

    # Lesson on the input() function
        print("--- 2. The input() function ---")
        print("The input() function allows you to take input from the user. It returns the data as a string.")
        print("Example: name = input('Enter your name: ') stores the input in the variable 'name'.\n")

    # Lesson on the print() function
        print("--- 3. The print() function ---")
        print("The print() function is used to display output to the user.")
        print("Example: print('Hello, World!') will display the text 'Hello, World!' to the user.\n")

    # Lesson on Formatting Output
        print("--- 4. Formatting Output ---")
        print("You can format output using f-strings, which allow you to embed variables directly into strings.")
        print("Example: name = 'John'; print(f'Hello, {name}!') will display 'Hello, John!'.")
        print("You can also format numbers using '{:.2f}' to display floating-point numbers to 2 decimal places.\n")

    # Lesson on File Input and Output
        print("--- 5. File Input and Output ---")
        print("You can read and write to files using Python. To read, use open(filename, 'r').")
        print("Example: with open('file.txt', 'r') as file: data = file.read() will read the contents of 'file.txt'.")
        print("To write to a file, use open(filename, 'w') or 'a' for appending.")
        print("Example: with open('output.txt', 'w') as file: file.write('Hello, file!') writes text to 'output.txt'.\n")

    # Mentioning Redirection (more advanced)
        print("Advanced: You can also redirect input and output using command-line redirection.")
        print("For example, python script.py < input.txt > output.txt would redirect input from 'input.txt' and output to 'output.txt'.\n")
        print("\n🎉 Congratulations, you've completed the topics! Time for a quick quiz to check your understanding.")

def main():
    while True:
        print("\n--- Welcome ---")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

