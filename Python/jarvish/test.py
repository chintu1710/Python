import speech_recognition as sr
import win32com.client

# Create a Recognizer instance

recognizer = sr.Recognizer()
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source)
    print("You can start speaking now...")

    try:
        # Listen to the input from the microphone
        audio_data = recognizer.listen(source)
        print("Recognizing your speech...")
        # Recognize the speech using Google's speech recognition API
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
        if text:
            speaker.Speak('I have to say Good Morning Because I can listen')
        else:
            pass

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from the service; {e}")


# print('hello')