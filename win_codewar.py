# https://www.codewars.com/kata/5e3f043faf934e0024a941d7

def codewar_result (cw, op) :
    cw.sort()
    op.sort()
    new_cw = cw.copy()
    battle_score = 0
    for i in range(len(cw)):
        for j in range(len(op)):
            if cw[i] > op[-1]:
                new_cw.remove(cw[i])
                op.pop()
                battle_score += 1
                break
            elif cw[i] <= op[j] and j > 0 and cw[i] > op[j - 1]:
                new_cw.remove(cw[i])
                op.pop(j - 1)
                battle_score += 1
                break
    cw = new_cw.copy()
    for i in range(len(cw)):
        for j in range(len(op)):
            if cw[i] == op[j]:
                op.pop(j)
                break
    for j in range(len(op)):
        battle_score -= 1
    return "Victory" if battle_score > 0 else "Stalemate" if battle_score == 0 else "Defeat"
