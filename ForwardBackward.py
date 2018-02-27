# Implementation fo the forward backward algorithm
import numpy as np
import hmm

def forward(hmm,dist,emissions):
    dists = [dist]
    em = []
    em.append(np.dot(hmm.getTransitionProb(),np.diagflat(hmm.getEmissionProb(0))))
    em.append(np.dot(hmm.getTransitionProb(),np.diagflat(hmm.getEmissionProb(1))))

    for emission in emissions:
        dist = forwardStep(hmm,dist,em[emission])
        dists.append(dist)
    return dists

def normalize(a):
    theSum = sum(a)
    for i in range(len(a)):
        a[i] /= theSum

def forwardStep(hmm,dist,em):
    dist = np.dot(dist,em)
    normalize(dist)
    return dist






def backward():
    pass


emissionProbs = np.array([[0.9,0.1],[0.2,0.8]])
transitionProbs = np.array([[0.7,0.3],[0.3,0.7]])
hmm = hmm.HiddenMarkov(transitionProbs,emissionProbs)
initialDist = [0.5,0.5]
emissions = [0,0,1,0,0]

if __name__ == "__main__":
    print(forward(hmm,initialDist,emissions))

