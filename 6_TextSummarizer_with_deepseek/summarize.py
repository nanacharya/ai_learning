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

# if __name__ == "__main__":
#     sample_text = """
#     Artificial Intelligence (AI) is the science and engineering of creating machines and software that can perform tasks typically requiring human intelligence. These tasks include reasoning, learning, perception, understanding language, problem-solving, and even creativity. At its core, AI is about simulating aspects of human cognitive abilities with computers, allowing them to make decisions, interpret data, and adapt to new situations.
#     AI is not a single technology but a field covering many subfields such as machine learning, natural language processing (NLP), computer vision, robotics, and expert systems. Machine learning (ML) is the backbone of modern AI. In ML, computers learn from data to improve their performance over time, without being explicitly programmed for every rule. For example, by analyzing thousands of emails labeled as spam or not-spam, a machine learning model can start predicting whether a new email is spam. Deep learning, a subfield of ML using neural networks with many layers, has advanced areas like image recognition, speech recognition, and even game-playing to human or superhuman levels.
#     """
#     print("Summary ####")
#     print(summarizeText(sample_text))
#


interface = gr.Interface(
    fn=summarizeText,
    inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize"),
    outputs=gr.Textbox(label="Summaraized Text"),
    title="AI-Powdered Summarizer..",
    description="Enter a long text to summarize "

)

# if __name__ == "__main__":
    # interface.launch()
