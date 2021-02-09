import json

data = json.load(open("data.json"))

want = 1
while want == 1 :
    word = input('word to search: ')
    word = word.lower()
    if word in data:
        print(data[word])
    else:
        print('not in dictionary')
    want = int(input("press 1 for more and 0 to end: "))
    