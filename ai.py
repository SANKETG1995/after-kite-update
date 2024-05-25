import os
from google.cloud import speech

# Set up Google credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"

def detect_intent_from_audio(audio_file_path):
    speech_client = speech.SpeechClient()

    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = {"content": content}
    config = {
        "encoding": speech.RecognitionConfig.AudioEncoding.LINEAR16,
        "sample_rate_hertz": 16000,
        "language_code": "en-US",
    }
    response = speech_client.recognize(config=config, audio=audio)

    for result in response.results:
        input_text = result.alternatives[0].transcript

    return input_text

def main():
    # Replace with actual audio file path
    audio_file_path = "path/to/your/audio/file.wav"
    
    input_text = detect_intent_from_audio(audio_file_path)
    
    print("User:", input_text)

if __name__ == "__main__":
    main()
