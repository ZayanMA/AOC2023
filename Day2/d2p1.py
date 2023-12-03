import re

def findColour(str, colour):
    if(re.search(colour, str) == None):
        return 0
    index = int(re.search(colour, str).start())
    num = re.search(r"\d+", str[index-3:index]).group()
    return int(num)


def possibleGames(input):
    f = open(input, "r")
    line = f.readline()
    sum = 0
    while line:
        id = int(re.search(r"\d+", line).group())
        line = line.split(":")[1]
        line = line.rstrip()
        parts = line.split(";")
        impossible = False
        for i in range(len(parts)):
            current = parts[i]
            numBlue = findColour(current, "blue")
            if(numBlue > 14):
                sum += id
                break
            numRed = findColour(current, "red")
            if(numRed > 12):
                sum += id
                break
            numGreen = findColour(current, "green")
            if(numGreen > 13):
                sum +=id
                break
        line = f.readline()
    f.close()
    print(sum)

def main():
    possibleGames("day2input.txt")

if __name__ == "__main__":
    main()