class Alphabet:

    def __init__(self, chain):
        self.chainAlphabet = self.checkAlphabet(chain)

    def getChainAlphabet(self):
        return self.chainAlphabet

    def __repr__(self):
        return str(self.chainAlphabet)

    def checkAlphabet(self, chainAlphabet):
        chainAlphabetToSet = set(chainAlphabet)
        newList = list(chainAlphabetToSet)
        return newList


class Language:
    def __init__(self, chain):
        self.chainLanguage = chain

    def __repr__(self):
        return str(self.chainLanguage)

    def getChainLanguage(self):
        return self.chainLanguage

class Operations:
    def __init__(self) -> None:
        pass