fileopen = open("Data\\api.txt","r")
API = fileopen.read()
print(API)
fileopen.close()

import openai
from dotenv import load_dotenv

AiBrain=str()

openai.api_key= API
load_dotenv()
completion = openai.Completion()

def Assign_Brain(BrainOfAI):
    global AiBrain
    AiBrain= BrainOfAI

def Reply(question, chat_log= None, temp_chat_log=None):
    FileLog = open("Database\\"+AiBrain,"r")
    chat_log_template = FileLog.read()
    FileLog.close()

    temp_FileLog = open("Database\\temp_chat.txt","r")
    temp_chat_log_template = temp_FileLog.read()
    temp_FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

    if temp_chat_log is None:
        temp_chat_log = temp_chat_log_template
    
    prompt= f"{chat_log}{temp_chat_log}You : {question}\nReply : "
    response= completion.create(
        model= "text-davinci-003",
        prompt=prompt,
        temperature= 1, 
        max_tokens= 200,
        top_p= 0.3,
        frequency_penalty = 0)
    
    ans= response.choices[0].text.strip()
    chat_log_template_update= chat_log_template + f"\nNew : {ans}"
    temp_chat_log_template_update= temp_chat_log_template + f"\nYou : {question}\nReply : {ans}"
    temp_FileLog = open("Database\\temp_chat.txt", "w")
    temp_FileLog.write(temp_chat_log_template_update)
    temp_FileLog.close()
    if "remember" in question:
        FileLog = open("Database\\"+AiBrain, "w")
        FileLog.write(chat_log_template_update)
        FileLog.close()
    return ans

