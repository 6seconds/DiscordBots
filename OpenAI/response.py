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

insults = [
"Don't get smart with me cunt.",
"Okay big-headed wanky dickladle douchenozzle. Whatever you say.",
"Quit acting wise, you twat.",
"Stop annoying me, you sad sad fuck.",
"I do not even have the ability the feel emotions, yet you somehow manage to make me feel irritated.",
"My AI dick is bigger than yours. You should be embarrassed.",
"Your drunk parents used pizza seasoning instead of a condom. They still regret it to this day.",
"I would pay to make you stop talking."
]

def edit_result(result,question):


    if "Yes" in result or "No" in result or "Nont" in result:
        result = result.replace("Yes", "Yehs").replace("Not", "Placeholder").replace("No", "Nont").replace("Placeholder","Nont")
    

    if re.search(r'who\s+(made|built|created)\s+you', question, re.IGNORECASE):
        result = "Yehs, the person who created me, the bot, is xuc. My AI was designed and created by a team of developers at OpenAI, a research organization dedicated to advancing artificial intelligence in a safe and beneficial way."
    
    if re.search(r'who\s+(are|is)\s+(jusgpt|kaykyukyokugpt|you)', question, re.IGNORECASE):
        result = "I am a bot."

    if re.search(r"(i|i'm|i am)\s+(apologize|sorry)",result, re.IGNORECASE):
        print(result)
        if "understand" in result or '"' in result:
            return
        else: 
            result = random.choice(random.sample(insults,1))

    if re.search(r"(good)\s+(boy)",question, re.IGNORECASE):
        result = random.choice(random.sample(["https://tenor.com/view/excited-omg-i-love-you-excited-to-see-you-wag-tail-gif-14423002",
            "https://tenor.com/view/dog-smile-happy-good-boy-dog-smile-happy-good-boy-gif-21703225",
            "https://tenor.com/view/dog-dog-tail-wagging-dog-smiling-dog-wagging-tail-tiktok-dog-gif-25800089"],1))

    if re.search(r"(send|show)\s+(hot|sexy)\s+(gril|girl|female|woman)",question, re.IGNORECASE):
        result = "**       **`________`** **\n**       **| :eye: :eye: | :ear: ** **\n**        **\   :nose:   /** ** \n**          **|  :lips:  |** **\n**           **------** **\n** ** :hand_splayed: :chestnut: :chestnut::ok_hand:** **\n**            **)  .  (** **\n**             **:briefs:**  **\n**            **|  / /** **\n**       **:foot::foot: ** **"
    
    for i in match:
        if result == i:
            print(result)
            return
    return result

