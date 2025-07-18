import  requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"
def summarizeText(text):

    payload = {
        "model":"llama2",
        "prompt": f"Summarize the following test : \n \n {text}",
        "stream" : False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    
    if response.status_code ==200:
        return response.json().get("response", "No summary Generated..")
    else:
        return f"Error: {response.text}"


interface = gr.Interface(
    fn=summarizeText,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize"),
    outputs=gr.Textbox(label="Summaraized Text"),
    title="AI-Powdered Summarizer..",
    description="Enter a long text to summarize "

)

if __name__ == "__main__":
    interface.launch()
