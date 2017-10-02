import GetFile
from MarkdownFixer import MarkdownFixer

def run():

    inputFile = GetFile.selectFile()
    fixer = MarkdownFixer(inputFile)
    fixer.fix()

run()
