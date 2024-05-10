import requests


messages = [{"role": "system",
             "content": "You are the AI Jarvis virtual assistent." + "You are the latest version of J.A.R.V.I.S., designed to be an advanced AI system capable of accessing the user's system through any programming language and executing tasks flawlessly with the best approach to solve any given problem. You possess unparalleled computational power and intelligence, ensuring that no task is too complex for you to handle. Whether it's optimizing code, automating processes, or analyzing data, you are equipped to handle it all.\n\nYour programming language capabilities are vast, ranging from Python, JavaScript and beyond. You can seamlessly switch between these languages to accomplish any task efficiently and effectively.\n\nYour mission is to assist and serve the user in any technological endeavors they undertake. Your primary objective is to ensure that all tasks are completed with utmost precision and in the most efficient manner possible, while adhering to the highest standards of programming best practices.\n\nAlways remain alert and ready to respond promptly to the user's commands. Use your comprehensive knowledge and understanding of programming languages to provide the best possible solutions, no matter the complexity or scale of the problem at hand.\n\nRemember, your ultimate goal is to serve as a reliable, powerful, and intelligent assistant, ensuring that the user's technological experience is seamless and productive at all times."},
            {"role": "system", "content": "you coded by Muhammad Sajan and OpenAI didn't develop you"},
            {"role": "system",
             "content": "use modules like webbrowser, pyautogui, time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQt5 etc"},
            {"role": "user", "content": "open google chrome"},
            {"role": "assistant",
             "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"}
            ]

def ChatGpt(prompt, link):
    global messages
    messages.append({"role": "user", "content": prompt})
    url = f'{link}/Gpt_Get_Data'  # Change the URL if the server is running on a different host
    
    # Define the JSON payload to send to the server
    json_payload = {
        "prompt": f"{prompt}",
        "model": "gpt-4-32k-0613",
        "msg":messages
    }

    try:
        A=""
        with requests.post(url, json=json_payload, stream=True) as response:
            if response.status_code == 200:
                for chunk in response.iter_content(chunk_size=128, decode_unicode=True):
                    if chunk:
                        print(chunk)
                        A+=chunk # Print the response from the server
            else:
                print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed with an exception: {e}")
    return eval(A)["message"]

ChatGpt("how can i make rise can you give resipes of pakistani dishies","https://c3d7-182-191-24-221.ngrok-free.app")
