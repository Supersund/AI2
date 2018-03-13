from math import log2
from random import randint


def pluralityValue(examples):
    ones = 0
    twos = 0
    for i in examples:
        if i[7] == 1:
            ones += 1
        else:
            twos += 1
    if ones > twos:
        return 1
    elif twos > ones:
        return 2
    else:
        return randint(1,2)


def B(q):
    return -(q*log2(q)+(1-q)*log2(1-q))


def remainder(examples, attribute):
    theSum = 0


def importance(examples, attributes):
    pass


def checkAllEqual(examples):
    correct = examples[0][7]
    for i in examples:
        if i[7] != correct:
            return False
    return True


def decisionTreeLearning(examples, attributes, parentExamples):
    if len(examples)==0:
        return pluralityValue(parentExamples)
    elif checkAllEqual(examples):
        return examples[0][7]
    elif len(attributes)==0:
        return pluralityValue(examples)

def fixTrainingData(path):
    file = open(path,'r')
    lines = file.readlines()
    examples = []
    for line in lines:
        examples.append(list(map(int, line.split())))
    return lines


def main():
    data = fixTrainingData("data/training.txt")


if __name__ == '__main__':
    main()