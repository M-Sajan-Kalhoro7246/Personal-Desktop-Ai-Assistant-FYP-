#pip install --upgrade BingImageCreator
from os import system , listdir
from PIL import Image

key= open(r"keys\bing","r").readline()
def Generate_Images(prompt:str):
    system(f'python -m BingImageCreator --prompt "{prompt}" -U "{key}"')
    return listdir("output")[-4:]

class Show_Image:
    
    def __init__(self,li:list) -> None:
        self.listd=li
    def open(self,no):
        try:
            img = Image.open(f"output\\{self.listd[no]}")
            img.show()

        except:
            self.open(no+1)
    def close(self,no):
        Image.Image.close()

if __name__=="__main__":
    Generate_Images("crate a tajmahal image")