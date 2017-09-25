import GetFile
from MarkdownFixer import MarkdownFixer

def run():
    inputFile = GetFile.selectFile()
    try:
        with open(inputFile) as fileObj:
            fixer = MarkdownFixer(fileObj)
            fixer.fix()
    except TypeError:
        print ("No file was selected")
    except:
        print ("Could not fix file")

run()
