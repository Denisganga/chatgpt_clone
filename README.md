# Django Chatbot with OpenAI API Integration

This is a Django-based chatbot application that leverages the OpenAI API for natural language processing and conversation generation.

![Example Image](confirmation.png)


![Example Image](input.png)

## Prerequisites

- Python (version 3.11.7)
- Django (version 3.2.20)
- OpenAI API key (version 0.28)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/denisganga/chatgpt_clone.git

cd django-chatbot
```

### 2. Setup Virtual Environment

```bash
# Create a virtual environment
python3 -m venv myenv

# Activate the virtual environment
# On Windows
myenv\Scripts\activate
# On Unix or MacOS
source myenv/bin/activate
```
### 3. Install dependancies

```bash
pip install -r requirements.txt
```
### 4.  Set Up OpenAI API Key

From the OpenAi website get your API key and add it in your views.py file

### 5. Apply Migration

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
### 6. Run the development server

```bash
python3 manage.py runserver
```
### 7. Features
1) Login Page
2) Register Page
3) Conversational chatbot powered by OpenAI API.

### 8. Usage
Type on the message box and the chatbot will respond to you

### 9. Contribution
Contribution is welcomed, I Welcome Your Pull Requests: Contribute to the Chatbot

### 10. License
This project is licensed under the [MIT_License](MIT_License).

### 11. Acknowledgements
OpenAI for providing the powerful natural language processing capabilities.
