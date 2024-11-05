import speech_recognition as sr

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    
    # Load audio file
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        
    # Recognize (transcribe) the speech
    try:
        text = recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        text = "Could not understand audio."
    except sr.RequestError:
        text = "Could not request results from the API."
    
    return text
