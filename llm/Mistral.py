from gradio_client import Client
from time import time as t
client = Client("https://osanseviero-mistral-super-fast.hf.space/")

def Mistral7B(user_input):
    C=t()
    result = client.predict(
        user_input,
        0.6,
        1024,
        0.9,
        1.1,
        api_name="/chat"
    )
    print(C)
    return result[0:-4]

if __name__=="__main__":
    while 1:
        print(Mistral7B(input(">>> ")))