string = 'OEAQMHCLUINR'

def findSequence(string):
    dictionary = buildDictionary(string)
    words = identifyValidWords(dictionary)
    solnDict = createSolutionDictionary(words)
    solution = checkForTwoWordSolution(solnDict)
    return solution

def buildDictionary(string):
    letters = list(string)
    sides_dict = {
        'north': letters[:3],
        'east': letters[3:6],
        'south': letters[6:9],
        'west': letters[9:12]
    }
    dictionary = dict()
    for side in sides_dict.keys():
        for l in sides_dict[side]:
            dictionary[l] = list(set(letters) - set(sides_dict[side]))
    return dictionary

def identifyValidWords(dictionary):
    valid_words = []
    with open('/Users/alex/Desktop/words.txt') as f:
        words = f.readlines()
    words = [x.strip() for x in words]
    for w in words:
        letters = list(w)
        i = 0
        while True:
            if i == 0:
                if letters[i] in dictionary.keys():
                    if letters[i + 1] in dictionary[letters[i]]:
                        i += 1
                    else:
                        break
                else:
                    break
            elif i == len(letters) - 1:
                valid_words.append(w)
                break
            else:
                if letters[i + 1] in dictionary[letters[i]]:
                    i += 1
                else:
                    break
    return valid_words

def createSolutionDictionary(words):
    solnDict = {}
    for word in words:
        letters = ''.join(sorted(list(set(list(word)))))
        if letters in solnDict.keys():
            solnDict[letters].append(word)
        else:
            solnDict[letters] = [word]
    return solnDict

def checkForTwoWordSolution(solnDict):
    viablePairs = []
    solutions = []
    for key in solnDict.keys():
        complement = ''.join(sorted(list(set(list(string)) - set(list(key)))))
        for key2 in solnDict.keys():
            if set(list(complement)).issubset(set(list(key2))):
                if key2 in solnDict.keys():
                    if [key2, key] not in viablePairs:
                        viablePairs.append([key, key2])
    for p in viablePairs:
        for w in solnDict[p[0]]:
            for v in solnDict[p[1]]:
                if w[-1] == v[0]:
                    solution = [w,v]
                    solutions.append(solution)
                elif w[0] == v[-1]:
                    solution = [v,w]
                    solutions.append(solution)
    if solutions == []:
        return 'No two-word solutions'
    else:
        answer_dict = {}
        for p in solutions:
            answer_dict[str(' + '.join(p))] = len(''.join(p)) - 13
        return sorted(answer_dict.keys(), key = answer_dict.get)

findSequence(string)
