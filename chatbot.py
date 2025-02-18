import json

# Load the JSON data from iso27001.json
with open('data/iso27001.json', 'r', encoding='utf-8') as file:
    iso_data = json.load(file)

# Process the user's question and return an answer
def process_question(question):
    # Convert the question to lowercase for easier matching (you can improve this logic)
    question = question.lower()
    
    # Check if the question matches any of the FAQ questions
    for faq in iso_data["iso_27001_2022"]["faq_chatbot"]:
        if faq["question"].lower() in question:
            return faq["reponse"]

    # If no match, return a default message
    return "Désolé, je n'ai pas pu comprendre votre question."

