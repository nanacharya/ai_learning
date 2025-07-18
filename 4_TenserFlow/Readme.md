brew install python@3.11
python3.11 -m venv tf-env
source tf-env/bin/activate
pip install tensorflow
pip install notebook
pip install ipykernel
python -m ipykernel install --user --name=myenv --display-name tf-env


for apple silicon
pip install tensorflow-macos tensorflow-metal

jupyter notebook

