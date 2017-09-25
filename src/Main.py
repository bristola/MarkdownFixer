import GetFile
from MarkdownFixer import MarkdownFixer

def run():
    inputFile = GetFile.selectFile()
    with open(inputFile) as fileObj:
        fixer = MarkdownFixer(fileObj)
        fixer.fix()

run()
