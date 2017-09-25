from tkinter import filedialog
from tkinter import *

def selectFile():
    root = Tk()
    fileName =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Markdown Files","*.md"),("all files","*.*")))
    if (not validate(fileName)):
        return None
    return fileName

def validate(fileName):
    if (fileName == None):
        return False
    fileArr = fileName.split(".")
    fileExtension = fileArr[len(fileArr)-1]
    if (len(fileArr) > 1 and fileExtension == "md"):
        return True
    return False
