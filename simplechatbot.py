from tkinter import *
from datetime import date
import time

root=Tk()

def send():
    send = "You: "+a.get()
    text.insert('end', '\n' +send)
    if (a.get().lower() == 'hi'):
        text.insert('end', '\n' + "Robot: Hello")
    elif (a.get().lower() == 'hey'):
        text.insert('end', '\n' + "Robot: How may I help you?")
    elif (a.get().lower() == 'hello'):
        text.insert('end', '\n' + "Robot: Hi")
    elif (a.get().lower() == 'how are you?'):
        text.insert('end', '\n' + "Robot: I am fine. How are you?")
    elif (a.get().lower() == 'i am fine'):
        text.insert('end', '\n' + "Robot: Nice to hear that")
    elif (a.get().lower() == 'how is your day'):
        text.insert('end', '\n' + "Robot: Good")
    elif (a.get().lower() == 'how can you help me'):
        text.insert('end', '\n' + "Robot: What help you need?")
    elif (a.get().lower() == 'what is your name'):
        text.insert('end', '\n' + "Robot: My name is Aish")
    elif (a.get().lower() == 'are you a human'):
        text.insert('end', '\n' + "Robot: No. I am a robot")
    elif (a.get().lower() == 'what is todays date' ):
        text.insert('end', '\n' + "Robot: " +str(date.today()))
    elif (a.get().lower() == 'what is the time now'):
        text.insert('end', '\n' + "Robot: " + str(time.strftime("%I:%M:%S %p")))
    else:
        text.insert('end', '\n' + "Robot: I didn't get you!")
        
root.title("Aish's Chatbot")
text=Text(bg="white")
text.grid(row=0, column=0, columnspan=2)
a=Entry(root,width=80)
Send=Button(root,bg='green',text="Send", width=20, command = send)
Send.grid(row=1,column=1)
a.grid(row=1,column=0)
root.mainloop()

'''
You: hi
Robot: Hello
You: hey
Robot: How may I help you?
You: hello
Robot: Hi
You: how are you?
Robot: I am fine. How are you?
You: i am fine
Robot: Nice to hear that
You: how is your day
Robot: Good
You: how can you help me
Robot: What help you need?
You: what is your name
Robot: My name is Aish
You: are you a human
Robot: No. I am a robot
You: what is todays date
Robot: 2024-05-08
You: what is the time now
Robot: 03:10:34 PM
You: are you ok
Robot: I didn't get you!
'''
