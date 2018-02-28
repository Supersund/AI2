# Implementation fo the forward backward algorithm
import numpy as np
import hmm

def forward(hmm,dist,emissions):
    dists = [dist]
    em = []
    em.append(np.dot(hmm.getTransitionProb(),np.diagflat(hmm.getEmissionProb(0)))) #Precalculate these
    em.append(np.dot(hmm.getTransitionProb(),np.diagflat(hmm.getEmissionProb(1))))

    for emission in emissions:
        dist = forwardStep(dist,em[emission])
        dists.append(dist)
    return dists


def normalize(a):
     theSum = sum(a)
     for i in range(len(a)):
         a[i] /= theSum
     return a


def forwardStep(dist,em):
    dist = np.dot(dist,em)
    normalize(dist)
    return dist


def backward(hmm,emissions):
    dist = np.array([0.5, 0.5])
    dists = [dist]
    for emission in emissions:
        dist = backwardStep(hmm,dist,emission)
        dists.append(dist)
    return dists


def backwardStep(hmm,dist,em):
    return normalize(np.dot(hmm.getTransitionProb(), np.dot(np.diagflat(hmm.getEmissionProb(em)), dist.T)).T)


def forwardBackward(hmm, dist, emissions):
    forwardDists = forward(hmm, dist, emissions)
    backwardDists = backward(hmm, emissions)

    return normalize(np.multiply(forwardDists, backwardDists))

emissionProbs = np.array([[0.9,0.1],[0.2,0.8]])
transitionProbs = np.array([[0.7,0.3],[0.3,0.7]])
hmm = hmm.HiddenMarkov(transitionProbs,emissionProbs)
initialDist = [0.5,0.5]
#emissions = [0,0,1,0,0]
emissions = [0,1,0,1]

if __name__ == "__main__":
    print(forward(hmm,initialDist,emissions))
    print(backward(hmm,emissions))
    print(forwardBackward(hmm,initialDist,emissions))

