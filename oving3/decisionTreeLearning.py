from math import log2
from random import randint



def pluralityValue(examples):
    """
    Calculates the most common classification within a group
    """
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
    """
    Calculates the entropy for a given probability
    """
    if q==1 or q==0:
        return 0
    else:
        return -(q*log2(q)+(1-q)*log2(1-q))

def numberOfOnes(examples):
    """
    Checks the number of "one"-classified examples in the given set
    """
    count = 0
    for i in examples:
        if i[7]==1:
            count+=1
    return count


def remainder(examples, attribute):
    """
    Calculates the sum of entropy for a given attribute
    """
    firstGroup = []
    secondGroup = []
    for i in examples:
        if i[attribute] == 1:
            firstGroup.append(i)
        else:
            secondGroup.append(i)
    theSum = len(firstGroup)/len(examples)*B(numberOfOnes(firstGroup)/len(firstGroup))
    theSum += len(secondGroup)/len(examples)*B(numberOfOnes(secondGroup)/len(secondGroup))
    return theSum

def gain(examples, attribute):
    """
    Calculates the gain from a given attribute
    """
    return B(numberOfOnes(examples)/len(examples))-remainder(examples,attribute)


def importance(examples, attributes):
    """
    Return the attribute with the highest information gain
    """
    bestGain = gain(examples, attributes[0])
    bestAttribute = attributes[0]
    for i in range(1,len(attributes)-1):
        thisGain = gain(examples, attributes[i])
        if thisGain>bestGain:
            bestGain = thisGain
            bestAttribute = attributes[i]
    return bestAttribute

def randomImportance(examples,attributes):
    """
    Returns a random attribute from the attributes list
    """
    bestGain = 0
    bestAttribute = None
    for i in range(0,len(attributes)-1):
        thisGain = randint(1,300)
        if thisGain > bestGain:
            bestGain = thisGain
            bestAttribute = attributes[i]
    return bestAttribute


def checkIfAllEqual(examples):
    """
    Check if all the datas in the given set has the same classification
    """
    correct = examples[0][7]
    for i in examples:
        if i[7] != correct:
            return False
    return True


def decisionTreeLearning(examples, attributes, parentExamples=None):
    """
    Recursively creates the decision tree
    """
    if len(examples)==0:
        return pluralityValue(parentExamples)
    elif checkIfAllEqual(examples):
        return examples[0][7]
    elif len(attributes)==1:
        return pluralityValue(examples)
    else:
        best = importance(examples,attributes)
        tree = {best:{}}
        attributes.remove(best)
        ones = []
        twos = []
        for i in examples:
            if i[best]==1:
                ones.append(i)
            else:
                twos.append(i)
        subtree1 = decisionTreeLearning(ones,attributes,examples)
        subtree2 = decisionTreeLearning(twos,attributes,examples)
        tree[best][1] = subtree1
        tree[best][2] = subtree2
    return tree





def fixTrainingData(path):
    """
    Changes the input file into two dimensional list
    """
    file = open(path,'r')
    lines = file.readlines()
    examples = []
    for line in lines:
        examples.append(list(map(int, line.split())))
    return examples

def traverseTree(tree,data):
    """
    Used to find the expected classification
    """
    if type(tree) == int:
        return tree
    else:
        key = list(tree.keys())[0]
        return traverseTree(tree[key][data[key]],data)

def testTree(tree,data):
    """
    Tests a tree versus testing data. Returns the fraction of correct ansvers
    """
    correct = 0
    incorrect = 0
    for i in data:
        if traverseTree(tree,i)==i[7]:
            correct += 1
        else:
            incorrect += 1
    return correct/(correct+incorrect)

def main():
    data = fixTrainingData("data/training.txt")
    attributes = [0,1,2,3,4,5]
    tree = (decisionTreeLearning(data,attributes))
    testData = fixTrainingData("data/test.txt")
    print(tree)
    print(testTree(tree,testData))


if __name__ == '__main__':
    main()