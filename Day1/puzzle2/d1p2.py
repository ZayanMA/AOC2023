import re

def wordsToNumbers(s):
    words_to_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
 
    pattern = re.compile(r'\b(' + '|'.join(words_to_numbers.keys()) + r')\b')
    return re.sub(pattern, lambda x: words_to_numbers[x.group()], s)

def getCalibrationValues(input):
    f = open(input, 'r')
    values = []
    line = f.readline()
    while line:
        line = line.rstrip()
        num1 = re.search(r"\d|one|two|three|four|five|six|seven|eight|nine", line).group(0)
        num2 = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)[-1]
        num1 = wordsToNumbers(num1)
        num2 = wordsToNumbers(num2)
        num = int(num1 + num2)
        values.append(num)
        line = f.readline()
    f.close()
    print(values)
    print(sum(values))

def main():
    getCalibrationValues("input.txt")

if __name__ == "__main__":
    main()

