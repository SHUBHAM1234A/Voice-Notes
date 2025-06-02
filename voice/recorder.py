import speech_recognition as sr

def record_audio(timeout=5, phrase_time_limit=4) -> sr.AudioData:
    """Convert audio to text using the microphone input."""
    
    recogniser = sr.Recognizer()

    try:
        with sr.Microphone() as src:
            print("Listening...")
            recogniser.adjust_for_ambient_noise(src, duration=1)
            audio = recogniser.listen(source=src, timeout=timeout, phrase_time_limit=phrase_time_limit)
    except AttributeError:
        print("pyaudio is not installed")
    except sr.WaitTimeoutError as e:
        print("Stopped listening due to no input.")
        print(e)
    except OSError:
        print("Error in handling mic")
    except Exception as e:
        print("Error in recording audio")
        print(e)
    finally:
        return audio  