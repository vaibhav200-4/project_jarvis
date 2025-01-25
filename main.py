import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process recognized commands
def processCommand(command):
    command = command.lower()  # Normalize to lowercase for easier matching

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "play music" in command:
        speak("Opening Spotify")
        webbrowser.open("https://open.spotify.com/")

    elif 'hello' in command:
        speak("Hello! How can I assist you today?")

    elif 'good bye' in command:
        speak("Goodbye! Have a great day.")
        exit()  # Exit the program

    else:
        speak("I didn't understand that command. Please try again.")

if __name__ == "__main__":
    speak("Initializing Jarvis")
    
    while True:
        # Listen for wake word "Jarvis"
        print("Listening for 'Jarvis'...")

        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)

                print(f"Recognized: {word}")

                if "jarvis" in word.lower():
                    speak("Jarvis at your service")
                    print("Listening for command...")

                    # Listen for the actual command after "Jarvis" is detected
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print(f"Command received: {command}")
                        processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
