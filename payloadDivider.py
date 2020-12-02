import sys

usage = "Usage: payloadDivider.py -f filename -m maxFileLen"

def parseArgs(args):
    file = ''
    maxLen = 100
    if(len(args) == 0):
        raise Exception("Missing parameters " + usage)
        return
    index = 1
    while(index < len(args)):
        if(args[index] == '-m'):
            try:
                maxLen = int(args[index + 1])
                print(maxLen)
                index += 2
            except:
                raise AssertionError("Invalid value for maxLen" + args[1])
        elif (args[index] == '-f'):
            try:
                file = args[index + 1]
                index += 2
                print(file)
            except:
                raise IOError("File error")
        else:
            raise Exception("Missing parameters " + usage)
    return file, maxLen


def splitter(file, maxLen):
    count = 1
    charCounter = 0
    newFile = open("payload" + str(count) + ".h", "w")
    newFile.write("const PROGMEM char payload"+str(count)+"[] = {\"")
    with open(file, "r") as payload:
        while(True):
            char = payload.read(1)           
            if not char:  
                break
            newFile.write(char)
            charCounter += 1
            if(charCounter >= maxLen):
                charCounter = 0
                newFile.write("\"};")
                newFile.close()
                count += 1
                print(count)
                newFile = open("payload" + str(count) + ".h", "w")
                newFile.write("const PROGMEM char payload"+str(count)+"[] = {\"")
        if(not newFile.closed):
            newFile.write("\"};")
            newFile.close()
            




if __name__ == "__main__":
    args = sys.argv
    f,m = parseArgs(args)
    splitter(f,m)
    pass