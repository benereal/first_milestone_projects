# print(".............................. C    B   T................................................")
questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["a) 3", "b) 4", "c) 5", "d) 6"],
        "answer": "b"
    },
   {"question": "What color is the sky on a clear day?",
    "options": ["a) red", "b) blue", "c) green", "d) yellow"],
    "answer": "b"
   },
   {"question": "How many legs does a spider have?",
    "options": ["a) 6", "b) 7", "c) 8", "d) 9"],
    "answer": "c"
   },
      {"question": "What sound does a cow make?",
    "options": ["a) meow", "b) quack", "c) moo", "d) bark"],
    "answer": "c"
   },
    {"question": "What is the opposite of 'hot'?",
    "options": ["a) warm", "b) cold", "c) cool", "d) boilig"],
    "answer": "b"
   }
]
def my_quiz (questions):
    score = 0
    for question in questions:
        print (question["question"])
        for option in question["options"]:
            print(option)
        user_input = input("Enter an option from (a-d): ").strip().lower()
        if user_input == question["answer"]:
            print("Correct!\n")
            score+=1
        else:
            print(f"Wrong. The correct answer was {question['answer']}.\n")
    return score 
score = my_quiz(questions)
print(f"You scored {score} out of {len(questions)}")

    


phonebook = []
menu = """select operation:
1. add contact
2. view_contacts
3. update_contact
4. search_contact
5. mark_favorite
6. umark_favorite
"""

# Add a new contact
def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    favorite = input("Enter Yes/No for favorite: ").strip().lower()

    contact = {
        "name": name,
        "phone number": number,
        "Favorite": True if favorite == "yes" else False
    }

    phonebook.append(contact)
    print("Contact added successfully!\n")

# View all contacts
def view_contacts():
    if not phonebook:
        print("No contacts found.\n")
    else:
        for contact in phonebook:
            print(f"Name: {contact['name']}")
            print(f"Phone Number: {contact['phone number']}")
            print(f"Favorite: {contact['Favorite']}\n")

# Update a contact by name
def update_contact():
    name_to_update = input("Enter the name of the contact to update: ")
    for contact in phonebook:
        if contact["name"].lower() == name_to_update.lower():
            new_number = input("Enter new phone number: ")
            contact["phone number"] = new_number
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")
            
def search_contact():
    search_for_contact = input("Enter a name to search: ").strip().lower()
    found = False

    for contact in phonebook:
        if contact["name"].lower() == search_for_contact:
            print(f"{contact['name']} is in the phonebook.")
            print(f"Phone Number: {contact['phone number']}")
            print(f"Favorite: {contact['Favorite']}\n")
            found = True
            break

    if not found:
        print(f"{search_for_contact} was not found in the phonebook.\n")
        
        
def mark_favorite():
    phone_num = input("Enter num you want to mark fav: ").strip()
    found = False
    for contact in phonebook:
        if contact["phone number"] == phone_num:
            contact["Favorite"]= True
            print(f"{contact['name']} has been marked as a favorite.\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")
        
def unmark_favorite():
    phone_num = input("Enter num you want to mark fav: ").strip()
    found = False
    for contact in phonebook:
        if contact["phone number"] == phone_num:
            contact["Favorite"]= False
            print(f"{contact['name']} has been removed from favorite.\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")
        
        
while True:
    print(menu)
    choice = input("Enter your choice: ")
    
    if choice not in "123456":
        print("invalid choice")
        
    if choice == "1":
        print(add_contact)
        
        
        
        


questions  = [
    {
        "question": "Explain the process of photosynthesis.",
        "keywords": {
            "photosynthesis": 2,
            "chloroplast": 2,
            "light energy": 2,
            "chlorophyll": 2,
            "carbon dioxide": 1,
            "water": 1,
            "glucose": 1,
            "oxygen": 1,
            "ATP": 1
        }
    },
    {
        "question": "What do plants need to grow?",
        "keywords": {
            "sunlight": 2,
            "water": 2,
            "soil": 2,
            "nutrients": 2,
            "carbon dioxide": 1
        }
    },
    {
        "question": "Name any three animals that live in water.",
        "keywords": {
            "fish": 2,
            "whale": 2,
            "shark": 2,
            "dolphin": 2,
            "octopus": 2
        }
    },
    {
        "question": "What is the capital of Nigeria?",
        "keywords": {
            "abuja": 5
        }
    },
    {
        "question": "Mention any two sources of electricity.",
        "keywords": {
            "solar": 2,
            "hydro": 2,
            "wind": 2,
            "coal": 2,
            "generator": 2
        }
    }
]

def ask_questions(questions):
    answers = []
    for q in questions:
        print(q["question"])
        answer = input("Your answer: ").lower()
        answers.append(answer)
    return answers

def score_answers(questions, answers):
    total_score = 0
    max_score = 0

    for i in range(len(questions)):
        q = questions[i]
        ans = answers[i]
        keywords = q["keywords"]
        max_score += sum(keywords.values())

        for word, points in keywords.items():
            if word.lower() in ans:
                total_score += points

    return total_score, max_score

def run_exam():
    print("Welcome to Exam Wizard!\n")
    answers = ask_questions(questions)
    print("\nEvaluating your answers...\n")
    total, maximum = score_answers(questions, answers)
    print("Your total score is:", total, "out of", maximum)


run_exam()
    
        


        
    


    