from flask import Flask, render_template, request, jsonify
from chatbot import process_question  # Import chatbot logic from chatbot.py

# Initialize Flask app
app = Flask(__name__)

# Route to serve the HTML interface (index.html)
@app.route('/')
def home():
    return render_template('index.html')  # Renders the HTML page from templates folder

# API endpoint for chatbot interactions
@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get('question')  # Get the question from the frontend
    
    # Get the chatbot's answer by processing the question
    answer = process_question(user_question)

    # Return the response in JSON format
    return jsonify({"answer": answer})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
