# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

def high(x):
    word_list = x.split()
    score_list = [0] * len(word_list)
    for pos in range(len(word_list)):
        for letter in word_list[pos]:
            score_list[pos] += (ord(letter) - 96)
    print(score_list)
    return word_list[score_list.index(max(score_list))]
