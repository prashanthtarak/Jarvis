import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import google_search


engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()


def cmd(text):
    engine.say(text)
    engine.runAndWait()


def listen_voice():  
    try:
        with sr.Microphone() as source:
            print('Listening....')
            cmd('Listening....')
            audio = r.listen(source=source, timeout=5, phrase_time_limit=5)       
            input_voice = r.recognize_google(audio)
            print(f'Command: {input_voice}')
            return input_voice
        cmd(command)
    except:
        exit()


if __name__ == "__main__":
    cmd('Hello Mr.Prashanth, Welcome')

    while True:

        command = listen_voice()
        try:
            if 'Jarvis' in command:
                cmd('Hello, What Can I Do For You')
                continue

            elif 'open' in command:
                string = (command.split(' '))
                jon = ' '.join(string[1:])
                try:
                    os.startfile(f"D:\\{jon}")
                except FileNotFoundError:
                    os.startfile(f"C:\\{jon}")
                except:
                    cmd('File Not Found')
                continue

            elif 'search' in command:
                cmd('What do u want to search')
                command = listen_voice()
                google_search.query=command
                print(google_search.sr)
                # webbrowser.open('http://www.google.com/search?btnG=1&q={}'.format(command.replace('search','')))
                continue

            elif 'goodbye' in command:
                cmd('Bye Prashath')
                break

            else:
                cmd(f'There is No Caommand Like {command}')
                continue

        except:
            break
