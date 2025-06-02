import speech_recognition as sr

def transcribe_audio(audio: sr.AudioData) -> str:
    """Transcribe audio input to text using the microphone."""

    text = ""
    recogniser = sr.Recognizer()
    
    try:
        text = recogniser.recognize_google(audio)
    except AttributeError:
        print("pyaudio is not installed")
    except sr.WaitTimeoutError as e:
        print("Stopped listening due to no input.")
        print(e)
    except OSError:
        print("Error in handling mic")
    except sr.UnknownValueError as e:
        text = " this is a sample text   "
        print(e)
    except sr.RequestError:
        text = "[API unavailable or offline]"
        print("speech recognition API offline")
    except Exception as e:
        print("Error in recording audio")
        print(e)
    finally:
        return text 
