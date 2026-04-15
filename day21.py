'''
import pyttsx3
name=input()
engine=pyttsx3.init()
def speech_to_text(text):
    engine.say(text)
    engine.runAndWait()
print("Hi!I'm ",name)
speech_to_text(f"Hello {name}! I'm siri, your voice asssistant.I'm here to help you with anything.")
'''
import pyttsx3
engine=pyttsx3.init()
def speach_text(text):
    engine.say(text)
user_text=input("enter your message: ").lower()
name="user"
if "my name is" in user_text:
    name=user_text.split("my name is")[-1].strip()
elif "name is" in user_text:
    name=user_text.split("name is")[-1].strip()
if user_text in ["hi","hello","hey"]:
    response="Hello!How can I help you?"
elif "name" in user_text:
    response=f"Hello {name} , how can i help you?"
else:
    response="sorry i did not understand that"
print(response)
speach_text(response)
engine.runAndWait()
