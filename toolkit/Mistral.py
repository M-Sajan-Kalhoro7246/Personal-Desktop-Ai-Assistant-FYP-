from huggingface_hub import InferenceClient
import random
from time import time as t
from os import listdir

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
# Replace YOUR_API_KEY_HERE with the obtained API key from Hugging Face
headers = {"Authorization": f"Bearer {open('keys//Mistral2').read()}"}


def LoadInjection(end="mistral"):
    files=listdir(r"injection/")
    TotData=[]
    for i in files:
        if i.split(".")[-1]==end:
            with open(fr"injection/{i}","r") as f:
                data=f.read()
            temp={"role":"system","content":data}
            TotData.append(temp)
    return TotData




messages = [
    {"role": "system", "content": "I'm the latest J.A.R.V.I.S. AI, designed by MUHAMMAD SAJAN with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
    {"role": "user", "content": "Open Google Chrome."},
    {"role": "assistant", "content":"Done Sir," "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {"role": "system", "content": "Python includes built-in functions you can use. For instance:"},
    {"role": "user", "content": "Jarvis can you generate masjid image"},
    {"role": "assistant", "content":"""```python
from Genration_Of_Images import Generate_Images, Show_Image
IMGS = Generate_Images(prompt="iron man")
print(IMGS)
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
```
```python
from func.Jukebox.YouTube import MusicPlayer
#taks song name and it stats playing music
ncs=MusicPlayer("ncs")
#any btw 0 - 100
ncs.Vol(30)
#pause or play
ncs.Play()
ncs.Pause()
#next song
ncs.Next()
#quit song
ncs.Quit()
```
```python
from toolkit.ChatGpt import ChatGpt
from toolkit.Mistral import Mistral7B
from toolkit.Filter import Filter

#u can use chat gpt its slow but its accurate
print(ChatGpt("essay on saving environment *under 200 words*"))
code=ChatGpt("python code to open google chrome ***use python programing language. just write complete code nothing else, also don't dare to use input function***")

# Filter return only python code from provided txt
exec(Filter(code))```

#u can use Mistral7B its fast but not much accurate it can work grate but only for small task not grater than 256 tokens
print(Mistral7B("hii",temperature=0.9))
```
```python
from toolkit.Alarm import set_alarm

alarm_time = "02:27:50"
sound_file = "audio//Unknown Brain MATAFAKA.mp3"
set_alarm(alarm_time, sound_file)
```"""},
    {"role": "user", "content": "Jarvis generate a cute cat image and show it to me"},
    {"role": "assistant", "content":"""```python
from Genration_Of_Images import Generate_Images, Show_Image
IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
```"""},
    {"role": "user", "content": "Jarvis show me next image", "content": "jarvis dosri image dekho"},
    {"role": "assistant", "content":"""```python
IMGS_TO_SHOW.open(0)
IMGS_TO_SHOW.open(1)
```"""},
    {"role": "user", "content":"Jarvis play neffex cold"},
    {"role": "assistant", "content":"""```python\nneffex=MusicPlayer("neffex cold song")```"""},
    {"role": "user", "content":"Jarvis write an essay on Python around 200 words and save it to a text file in my current working directory"},
    {"role": "assistant", "content":"""```python\nfrom toolkit.ChatGpt import ChatGpt\nres=ChatGpt("essay on python *around 100 words*")\nopen("python_essay.txt","w").write(res)```"""},
    {"role": "user", "content":"Jarvis set an alarm for 2:55 ***use python programing language. just write complete code nothing else, also don't dare to use input function*** **you can use the module that i provided if required**"},
    {"role": "assistant", "content":"""```python\nfrom toolkit.Alarm import set_alarm\nalarm_time = "02:55:00"\nsound_file = r"audio//Unknown Brain MATAFAKA.mp3"\nset_alarm(alarm_time, sound_file)```"""}
]
# Function to format prompt
def format_prompt(message, custom_instructions=None):
    prompt = ""
    if custom_instructions:
        prompt += f"[INST] {custom_instructions} [/INST]"
    prompt += f"[INST] {message} [/INST]"
    return prompt

# Function to generate response based on user input
def Mistral7B(prompt, temperature=0.9, max_new_tokens=512, top_p=0.95, repetition_penalty=1.0):
    C=t()
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=random.randint(0, 10**7),
    )
    custom_instructions=str(messages)
    formatted_prompt = format_prompt(prompt, custom_instructions)

    messages.append({"role": "user", "content": prompt})

    client = InferenceClient(API_URL, headers=headers)
    response = client.text_generation(formatted_prompt, **generate_kwargs)

    messages.append({"role": "assistant", "content": response})
    print(t()-C)
    return response

if __name__=="__main__":
    while True:
        # Get user input
        user_prompt = input("You: ")

        # Exit condition
        if user_prompt.lower() == 'exit' or user_prompt.lower() == 'Good By Jarvis' or user_prompt.lower() == 'Good By' or user_prompt.lower() == 'Good Luch':
            break

        # Generate a response based on user input
        generated_text = Mistral7B(user_prompt)
        print("Ai:", generated_text)