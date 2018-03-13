
class HiddenMarkov:
    def __init__(self, transitionProb, emissionProb):
        self._transitionProb = transitionProb
        self._emissionProb = emissionProb

    def getEmissionProb(self,emission):
        return self._emissionProb[:, emission]

    def getTransitionProb(self):
        return self._transitionProb

    def num_states(self):
        return self._transitionProb.shape[0]