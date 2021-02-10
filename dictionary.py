import json

data = json.load(open("data.json"))

def dictionary(word):
    if word in data:
        return(data[word])
    else:
        print('not in dictionary')
        return None

if type(output) == list:
    word = input('word to search: ')
    word = word.lower()
    output = dictionary(word)

    if output is not None:
        for item in output:
            print(item)
else:
    print(output)
    print(output)