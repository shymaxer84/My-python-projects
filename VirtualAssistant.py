import speech_recognition as speechrecognition # To convert speech into text
import pyttsx3  # To convert text into speech
import pywhatkit
import datetime
import wikipedia

listener = speechrecognition.Recognizer()
machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()


def input_instruction():
    try:
        with speechrecognition.Microphone() as origin:
            print('listening')
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if 'Dmitry' in instruction:
                instruction = instruction.replace('Dmitry', " ")
                print(instruction)  # what we are speaking to the assistantexcept:
    except:
        pass
    return instruction


def play_dmitry():
    while True:
        instruction = input_instruction()
        print(instruction)

        if "play" in instruction:
            song = instruction.replace('play', " ")
            talk('playing' + song)
            pywhatkit.playonyt(song)
            continue

        elif "time" in instruction:
            time = datetime.datetime.now().strftime('%I:%Mp')
            print(time)
            talk('Current time' + time)
            continue

        elif "date" in instruction:
            date = datetime.datetime.now().strftime('%d /%m /%Y')
            print(date)
            talk("Today is date" + date)
            continue
        elif "how are you" in instruction:
            talk('I am fine thanks, how about you')

        elif "name" in instruction:
            talk('I am Dmitry, What can I do for you')
            continue

        elif "who is" in instruction:
            human = instruction.replace('who is', " ")
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
            continue

        elif "bye" in instruction:
            talk("Good Bye. Have a nice day!!!")
            exit()
        else:
            talk('Please repeat')


play_dmitry()

# if __name__ == '__main__':
#     play_dmitry()