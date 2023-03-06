import speech_recognition as a
import pyttsx3   # text to speech                
import pywhatkit  
import datetime  
import wikipedia
listener=a.Recognizer() 

machine=pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try: 
        with a.Microphone() as mic:
            print('listening...')
            speech = listener.listen(mic)
            instruction=listener.recognize_google(speech)
            instruction=instruction.lower()
            if 'Alexa' in instruction:
                instruction=instruction.replace('Alexa','')
                print(instruction)
        


 
    except:
        pass
    return instruction
def play_Alexa():
    instruction=input_instruction()
    print(instruction)
    if 'play' in instruction:
        song=instruction.replace('play',"")
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time=datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time'+ time)
        play_Alexa()
    elif 'date' in instruction:
        date=datetime.datetime.now().strftime('%d /%m /%Y')
        talk("Today's date" + date)
        play_Alexa()
    elif 'how are you' in  instruction:
        talk('I am fine, how are you')
        play_Alexa()
    elif 'fine' in instruction:
        talk('Good,what can i do for you')
        play_Alexa()
    elif 'my name' in instruction:
        talk('Your name is Kotamarthy Veerabhadra Shravan Kumar')
    elif 'what is your name' in instruction:
        talk('I am alexa, what can i do for you')
    elif 'friends' in instruction:
        talk('Your best friends are Vamsi,Sudha,Rohith,Chanakya')
    elif 'thank you' in instruction:
        talk('you are welcome Shravan')
    elif 'who is ' in instruction:
        human=instruction.replace('who is', " ")
        info = wikipedia.summary(human,10)
        print(info)
        talk(info)

    else:
        talk('Please repeat!')


play_Alexa()




