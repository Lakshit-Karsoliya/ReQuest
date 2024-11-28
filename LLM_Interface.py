import requests
import json
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

class Interface:
    def __init__(self):
        self.interface_inof = "Interfave for LLMS"
        self.ollama_url='http://localhost:11434/api/generate'
        self.pod_initiated = False
    def generate_ollama_response(self,model_name:str,prompt:str,verbose:bool=False):
        """Function used to establish connection between ollama generate api"""
        payload={
            "stream":True,
            "model":model_name,
            "prompt":prompt
        }
        response = requests.post(self.ollama_url,json=payload,stream=True)
        accumulated_data = ""
        for chunk in response.iter_content(chunk_size=512):
            if chunk:
                data = chunk.decode('utf-8')
                accumulated_data+=data 
                try:
                    json_data = json.loads(accumulated_data)
                    if verbose:print(f"[INFO][Ollama Response : {json_data}]")
                    try:
                        yield json_data["response"]
                    except:
                        pass 
                    accumulated_data=""
                except json.JSONDecodeError:
                    continue
    def initiate_runpod_interface(self):
        self.runpod_interface_client = OpenAI(
            api_key=os.environ['RUNPOD_API_KEY'],
            base_url=f"https://api.runpod.ai/v2/{os.environ['RUNPOD_INFERENCE_POD_ID']}/openai/v1"
        )
        print('Runpod Serverless VLLM client is set')
        self.pod_initiated = True
    def generate_runpod_response(self,prompt,inference_model_name=os.environ['RUNPOD_SERVERLESS_VLLM_MODEL_NAME']):
        if self.pod_initiated:
            response = self.runpod_interface_client.chat.completions.create(
                model = inference_model_name,
                messages=[{"role":"system","content":"""You are helpful assistant"""},
                    {"role":"user","content":prompt}
                    ],
                temperature=0.9,
                max_tokens=2048,
                stream=True,
            )
            for i in response:
                yield i.choices[0].delta.content
        else:
            print("Please Initiate Runpod Serverless Vllm by calling 'initiate_runpod_interface'")


if __name__ == "__main__":
    print("This is Interface.py file used to to establish interfave between ollama ,  runpod  and openAI models ")