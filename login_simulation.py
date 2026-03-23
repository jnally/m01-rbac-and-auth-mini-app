## Author: Jeremy Nally
## Course: SDEV245 - Security and Secure Coding
##
## Assignment Instructions (modified for relevant details):
##
## Module 1: Assignment - RBAC and Authentication Mini-App
## Due: Mon Mar 23, 2026 11:59pm
## 50 Points Possible
##
## Get Ready
## Students will build a simple application with user login and role-based access control. This demonstrates the implementation of basic authentication and access restrictions based on role.
##
## This assignment will support the following outcomes:
##
## 1.2: Compare the differences between authentication and access controls.
## 1.3: Implement a basic access control mechanism in a sample application.
## Supportive Materials
## To be successful with this assignment, you must complete each of the materials listed on the Learning Materials page. 
##
## 
##
## Complete Your Work
## Instructions:
## Build a very basic app or script in any language (e.g., Python, Node.js, Java) that demonstrates the core ideas of authentication, roles, and access control.
##
## Requirements:
## Login simulation
##
## Use a hardcoded username and role in the script.
##
## No need for password hashing or form input.
##
## User roles
##
## Create two user roles (e.g., admin and user) using simple logic or a dictionary.
##
## Protected actions or routes
##
## Simulate two different functions or endpoints.
##
## Allow only admin to access one, and only user to access the other.
##
## Code comment or short paragraph
##
## Explain in a few lines how your app shows one part of the CIA triad (Confidentiality, Integrity, or Availability).
##
## Deliverables:
## Code files (GitHub link)
##
## README (brief explanation of CIA and your app logic)
##
## (Optional) 1-minute screen recording showing login and access control in action
##
##
## 
## RBAC and Authentication Mini-App Rubric
##
## Functional Login System
##  The login system should correctly authenticate users and allow access based on valid credentials. It should handle incorrect logins gracefully and maintain session state or simulate session behavior.
##
## Full Marks
## Fully functional, secure, and user-friendly
## 15 pts
##
## Correct Role-Based Access Logic
##  The system must restrict access to certain features or routes based on user roles (e.g., admin vs. standard user). Logic should be clear and enforceable.
##
## Full Marks
## Fully correct and properly enforced
## 15 pts
##
## Explanation of CIA in README
##  README must include a thoughtful explanation of how the app enforces Confidentiality, Integrity, and Availability. Should include examples from the submitted project.
##
## Full Marks
## Clear, well-organized, and demonstrates strong understanding
## 10 pts
##
## Code Quality & Comments
##  Code should be organized, readable, and include meaningful comments explaining the logic. No unnecessary repetition or poor practices.
##
## Full Marks
## Clean, readable, and well-documented
## 10 pts
##

# users dictionary with roles
users = {
    'carl': {'role':'admin'},
    'donut': {'role':'user'}
    }

# simple math test questions for use by the functions
test_questions = {
    1: {'question':'What is 4*5?','answer':20},
    2: {'question':'What is 2^6?','answer':64},
    3: {'question':'What is 5!?','answer':120},
    4: {'question':'What is the slope of a horizontal line?','answer':0},
    }

# presents the answer key to the math test (admin only!)
def view_answer_key():
    print('Test Answer Key (keep secret)\n')
    for i in test_questions:
        print(i, ': question: ', test_questions[i]['question'], ' answer: ', test_questions[i]['answer'],sep='')

# administers math test (user role only!)
def take_test():
    print('Math Test')
    score = 0
    possible = 100
    for i in test_questions:
        question = test_questions[i]['question']
        question = 'Question #' + str(i) + ': ' + question + ' : '
        answer = test_questions[i]['answer']
        user_input = input(question)
        while not(user_input.isnumeric()):
            print('Invalid Input: Enter a number.')
            user_input = input(question)
        if int(user_input) == answer:
            score += 25
    print('Your test score is ', score, ' out of ', possible, '.', sep='')

# verify that username is in the dictionary
def username_exists(username):
    return

# very trusting login function that only prompts for a username and no password
def login():
    username = input('Enter your username: ')
    while not(username_exists):
        print('Invalid username')
        username = input('Enter your username: ')    
    return username

# present very trusting user login, admin carl can view math test answer key, user donut can take a math test
def main():
    keep_going = True
    logged_in = False
    username = ''
    attempts = 0

    # loop until user wishes to exit or too many failed login attempts
    while keep_going:
        # let user log in with just username  (up to 5 attempts)
        if not(logged_in):
            username = input('Enter your username: ')
            attempts += 1
            while not(username_exists(username)):
                print('Invalid username')
                username = input('Enter your username: ')
                attempts += 1
                if attempts >= 5:
                    return 1
            attempts = 0

        # menu
        if username['role'] == 'admin':
            #todo
        elif username['role'] == 'user':
            #todo
        else:
            print('Nothing to choose...') # should not happen with current users

        # prompt user for logout
        logout = input('Would you like to log out and close? Y or N: ')
        if logout.toupper() == 'Y':
            logged_in = False
            keep_going = False
    #view_answer_key()
    #take_test()
    return

if __name__ == '__main__':
    main()




