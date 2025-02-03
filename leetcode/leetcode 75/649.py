def predictPartyVictory(senate: str) -> str:
    rad, dir = [], []
    n = len(senate)

    for i in range(n):
        if senate[i] == 'R':
            rad.append(i)
        else:
            dir.append(i)

    while rad and dir:
        x, y = rad.pop(0), dir.pop(0)
        if x < y:
            rad.append(n)
        else:
            dir.append(n)
        n += 1

    if rad:
        return 'Radiant'
    else:
        return 'Dire'


if __name__ == '__main__':
    print(predictPartyVictory("RD") == "Radiant")
    print(predictPartyVictory("RDD") == "Dire")
    print(predictPartyVictory("DDRRR") == "Dire")
    print(predictPartyVictory("DDRRRR") == "Radiant")
    print(predictPartyVictory("DRRD") == "Dire")
    print(predictPartyVictory("DRRDRDRDRDDRDRDR") == "Radiant")
