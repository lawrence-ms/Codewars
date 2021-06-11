# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    word_dict = {}
    word_list = sentence.split(" ")
    for word in word_list:
        for char in word:
            if char.isnumeric():
                word_dict[int(char)] = word
    word_list = []
    for num in sorted(list(word_dict.keys())):
        word_list.append(word_dict[num])
    return " ".join(word_list)
