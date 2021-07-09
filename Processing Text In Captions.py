import json
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os


def camel_case_split(s):
    words = [[s[0]]]

    for c in s[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    return [''.join(word) for word in words]


# assign directory
directory = 'C:/Users/vinay/PycharmProjects/SentimentalAnalysis/IG'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    file1 = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(file1):

        file = open('IG/{}'.format(filename), 'r')

        data = json.load(file)

        f = open('temp.txt', 'w', encoding="utf-8")
        for i in range(0, len(data)):
            caption = data[i]['caption']
            wordlist = caption.split('#')
            f.write(wordlist[0]+' ')

            for x in range(1, len(wordlist)):
                if len(wordlist[x]) > 1:
                    cleaned = camel_case_split(wordlist[x])
                    for word in cleaned:
                        f.write(word+' ')

        f.close()
        file.close()

        text = open("temp.txt", encoding="utf-8").read()

        lower_case = text.lower()
        cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
        tokenized_words = word_tokenize(cleaned_text, "english")

        file = open('{}.txt'.format(filename[:-5]), 'a', encoding="utf-8")

        for word in tokenized_words:
            if word not in stopwords.words('english'):
                file.write(word + ' ')

        file.close()
