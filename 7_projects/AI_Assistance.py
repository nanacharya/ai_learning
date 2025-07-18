import requests
import gradio as gr
import speech_recognition as sr
import pyttsx3

OLLAMA_URL = "http://localhost:11434/api/generate"

engine = pyttsx3.init()

def ai_assistnace (text):
    prompt=f"Respond this query as a personal AI assistance : \n \n {text}"
    payload = {
        "model":"deepseek-r1",
        "prompt": prompt,
        "stream" : False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        ai_response = response.json().get("response", "I am sorry")
        engine.say(ai_response)
        engine.runAndWait()
        return ai_response
    else:
        return "Sorry some issue is happened"

def listen_command():
    reconizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listing....")
        reconizer.adjust_for_ambient_noise(source)
        audio = reconizer.listen(source)

    try:
        command = reconizer.recognize_google(audio)
        print(f"User :  {command}")
        return  command
    except sr.UnknownValueError:
        return "Sorry I cound't understand that "


if __name__ == "__main__":
    sample_query = "Tell me Joke in nepali language"
    print("AI Response")
    print(ai_assistnace(sample_query))



