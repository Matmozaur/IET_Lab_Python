from common_utils.data_read_utils import openable_file
import nltk


class TextReader:   # czy ta klasa jest potrzebna, skoro ma same metody statyczne?

    @staticmethod
    def read_tokens_txt(path):
        path = openable_file(path)  # czy kontrola w tym miejscu coś Panu daje?
        with open(path, "r+", encoding='utf-8') as file:
            for line in file:
                for word in line.split():
                    for token in nltk.word_tokenize(word):
                        yield token

    @staticmethod
    def read_tokens_conll(path):
        path = openable_file(path)
        with open(path, "r+", encoding='utf-8') as file:
            for line in file:
                yield line.split()[0][1:-1]

    @staticmethod
    def read_sentences_txt(path):
        path = openable_file(path)
        with open(path, "r+", encoding='utf-8') as file:
            temp = ''
            flag = False
            for c in file.read():
                if flag:
                    if c.isupper():
                        yield temp.strip()
                        temp = ''
                    if not c.isspace():
                        flag = False
                    temp += c
                else:
                    temp += c
                    if c == '.':
                        flag = True
            yield temp

    @staticmethod
    def read_sentences_conll(path):
        path = openable_file(path)
        with open(path, "r+", encoding='utf-8') as file:
            temp = ''
            flag = False
            for line in file:
                line, token_type = line.split()[0][1:-1], line.split()[2]
                # moja sugestia: token, lemma, token_type = line.split(); token = token[1:-1]
                if token_type == 'Interp':
                    flag = False
                if flag:
                    temp += ' '
                temp += line
                flag = True
                if line == '.':
                    yield temp
                    temp = ''
                    flag = False


if __name__ == '__main__':
    for t in TextReader.read_sentences_conll('nkjp.conll'):
        print(t)
