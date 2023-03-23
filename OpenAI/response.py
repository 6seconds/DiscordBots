import re
import random

match = [
"Hello, how can I help you?",
"Hello, how may I help you?",
"Hello, how can I help you today?",
"Hello, how may I help you today?",
"Hello! How can I assist you?",
"Hello! How may I assist you?",
"Hello! How may I assist you today?",
"Hello! How can I assist you today?",
"Hello! Is there anything I can help you with today?",
"Hello there! How may I assist you today?",
"Hi there! How can I assist you today?",
"Is there anything you would like to chat about or a question you have for me?",
"Is there anything I can help you with?",
"Is there anything specific you would like to chat about?",
"Is there anything else you want to chat about?"
"Is there anything I can assist you with today?"
]

replies = [
"EXAMPLE1",
"EXAMPLE2",
"EXAMPLE3"
]

def edit_result(result,question):    

    
    if re.search(r'(who)\s+(is|are)\s+(this|you)', question, re.IGNORECASE):
        result = "I am a bot."

    if re.search(r"(i|i'm|i am)\s+(apologize|sorry)",result, re.IGNORECASE):
        print(result)
        if "understand" in result or '"' in result:
            return
        else: 
            result = random.choice(random.sample(insults,1))
    
    for i in match:
        if result == i:
            print(result)
            return
    return result

