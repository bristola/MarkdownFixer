class MarkdownFixer:

    lineLength = 75

    def __init__(self, fileName):

        self.fileName = fileName

    def fix(self):

        with open(self.fileName, 'r') as readableFile:
            self.contents = readableFile.readlines()
            self.newContents = list()
            self.fixLines()

        with open(self.fileName, 'w') as writeableFile:
            writeableFile.truncate()
            writeableFile.writelines(self.newContents)

    def fixLines(self):

        stack = list(reversed(self.contents))
        while (len(stack) is not 0):
            stackItem = stack.pop()
            if (stackItem == "\n"):
                self.newContents.append(stackItem)
            curLine = stackItem.replace("\n","")
            if (len(curLine) < 75):
                self.newContents.append(curLine+"\n")
                continue
            charCount = 0
            for word in curLine.split(' '):
                print ("Current word is "+word+" and the charCount now is "+str(charCount+len(word)))
                if (charCount + len(word) > self.lineLength):
                    self.newContents.append(curLine[:charCount-1]+"\n")
                    break
                else:
                    charCount += len(word) + 1

            leftOver = curLine[charCount:]
            if (len(leftOver) > 0):
                if (len(stack) == 0 and len(leftOver) > 75):
                    stack.append(leftOver)
                elif (len(stack) == 0 and len(leftOver) < 75):
                    self.newContents.append(leftOver)
                    break
                else:
                    stack.append(leftOver + ' ' + stack.pop())
