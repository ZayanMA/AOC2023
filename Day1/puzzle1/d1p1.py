import re

def getCalibrationValues(input):
    f = open(input, 'r')
    values = []
    line = f.readline()
    while line:
        line = line.rstrip()
        num1 = re.search(r"\d", line).group(0)
        num2 = re.findall(r'\d', line)[-1]
        num = int(num1 + num2)
        values.append(num)
        line = f.readline()
    f.close()
    #print(values)
    print(sum(values))

def main():
    getCalibrationValues("day1input.txt")

if __name__ == "__main__":
    main()

