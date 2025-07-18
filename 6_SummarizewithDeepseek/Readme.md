brew install ollama
ollama serve
ollama pull llama2

Test : -> 
curl http://localhost:11434/api/generate -d '{
"model": "llama2",
"prompt": "Explain what Ollama is in one line.",
"stream": false
}'



pip install requests gradio 
