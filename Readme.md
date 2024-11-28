![Cover Art](assets/coverArt/ReQuest-28-11-2024_created_with_textstudio_and_upscale_with_imgupscaler.png "This is cover Art")
<h5 align="center">ReQuest: LLM-Powered Practice Question Generator</h5>
ReQuest is an AI-driven application designed to assist learners and educators by generating similar practice questions based on an input question. Built using advanced language models suppoets interface with ollama and runpod vllm serverless inference, ReQuest ensures the generated questions maintain relevance while offering variety, making it ideal for  testing, or refining understanding of a topic to build confidence.

---


<br><br>
  
<h3 align="center">Struggling with preparation? Watch how ReQuest generates tailored questions to help examiners , interviewers and students.</h3>

https://github.com/user-attachments/assets/b82a9716-1735-4ba8-88d8-894f31161b5d



## Installation and Usage  

#### **Installation Guide for Linux**
```bash
# Step 1: Clone the Repository
git clone https://github.com/Lakshit-Karsoliya/ReQuest.git
cd ReQuest
# Step 2: Set Up a Virtual Environment
virtualenv env
source env/bin/activate
pip install -r requirements.txt
# Step 3: Install Ollama
curl -fsSL https://ollama.com/install.sh | sh
# Step 4: Pull Llama 3.1 Model
ollama run llama3.1
# To Exit the Ollama Chat Interface: type "/bye" or press Ctrl + D
# Step 5: Launch the Streamlit UI 
streamlit run ui_streamlit_ollama_interface.py 
```
#### **Installation Guide for Windows**
```bash
# Step 1: Clone the Repository
git clone https://github.com/Lakshit-Karsoliya/ReQuest.git
cd ReQuest
# Step 2: Set Up a Virtual Environment
pip install virtualenv
virtualenv env
cd env
Scripts\activate 
cd ..
pip install -r requirements.txt
# Step 3: Install Ollama
# install ollama exe file from https://ollama.com/download here and install it 
# Step 4: Pull Llama 3.1 Model 
# Inside cmd 
ollama run llama3.1
# To Exit the Ollama Chat Interface: type "/bye" or press Ctrl + D
# Step 5: Launch the Streamlit UI 
streamlit run ui_streamlit_ollama_interface.py 
```
## Support Serverless VLLM runpod Based Inference
To run with runpod you require an account 
- Make runpod account 
- setup a serverless vllm machine with desired llm set configurations according to your need use only one gpu with no additional workers if you are strictly using for one person
- create apikey 
- paste apiKey , machine_Id , model_name in .env



<h5 align="center">Here is Video of How to do it</h5>

https://github.com/user-attachments/assets/e046565a-97f1-4f58-877d-ffcc591fe976





## Features  
- **Input-Based Question Generation**: Provide any question as input, and ReQuest will generate a set of similar questions tailored to the same context.  
- **Customizable Output**: Adjust the number of generated questions to suit your needs.  
- **Intuitive Interface**: User-friendly interface.  

---

## Use Cases  
- **Students**: Generate additional questions for exam preparation or self-assessment.  
- **Educators**: Create diversified question banks for quizzes and assignments.  
- **Professionals**: Practice interview-style questions in a focused manner.  

---

## Additional Info  
- `prompts.json` contains the prompts for the LLM. Feel free to experiment and customize them.  
- This branch uses **llama3.1** in Ollama and **mistral-nemo** on RunPod. If others clone and improve this project, you may find these models in their respective branches.  


---

## Special Thanks  
- **TextStudio**: Used to generate the request text at the top of the README.  
- **ImgUpscaler**: Used to upscale the images.  
- **OBS Studio**: Used to record the video.  
- **Ollama**: For providing the LLM framework.  



<br><br><br><br>
<h5 align="center">Made with ❤ by Lakshit</h5>
