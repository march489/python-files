import time

def minion_game(string: str):
    start = time.time()
    kevin_score = 0
    stuart_score = 0
    for index in range(len(string)):
        if string[index] in ['A', 'E', 'I', 'O', 'U']:
            kevin_score += len(string) - index
        else:
            stuart_score += len(string) - index
    end = time.time()
    print(end - start)
    if kevin_score > stuart_score:
        return 'Kevin ' + str(kevin_score)
    elif kevin_score < stuart_score:
        return 'Stuart ' + str(stuart_score)
    else:
        return 'Draw'

if __name__ == '__main__':
    s = input()
    print(minion_game(s))
    