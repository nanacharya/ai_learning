
pip install -r requirements.txt
curl -fsSL https://ollama.com/install.sh | sh
ollama list
ollama pull codellama:13b
nohup ollama serve > ollama.log 2>&1 &


brew install ollama
ollama serve
ollama pull codellama
 or codellama:13b


Test : -> 
curl http://localhost:11434/api/generate -d '{
"model": "codellama",
"prompt": "Explain what Ollama is in one line.",
"stream": false
}'



pip install requests gradio 
