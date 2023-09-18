import os

def getNames():
    with  open("carsFormatted.txt", "r") as file:
        for line in file.readlines():
            yield line

def formatName(name):
    out =  " ".join(name.split("\t")).strip() + ")"
    index = len(out) - 10
    out = out[:index] + "(" + out[index:]

    index = len(out) - 5
    out = out[:index - 1] + "-" + out[index:]
    return out

if __name__ == "__main__":
    with open("carNames.txt", "w+") as f:
        for x in getNames():
            f.write(formatName(x) + "\n")