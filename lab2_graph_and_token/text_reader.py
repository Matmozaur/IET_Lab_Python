from common_utils.data_read_utils import openable_file
import nltk
nltk.download('punkt')


class TextReader:

    @staticmethod
    def read_tokens_txt(path):
        with open(path, "r+", encoding='utf-8') as file:
            for line in file:
                for word in line.split():
                    for token in nltk.word_tokenize(word):
                        yield token

    @staticmethod
    def read_tokens_conll(path):
        with open(path, "r+", encoding='utf-8') as file:
            for line in file:
                yield line.split()[0][1:-1]

    @staticmethod
    def read_sentences_txt(path):
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
        with open(path, "r+", encoding='utf-8') as file:
            temp = ''
            flag = False
            for line in file:
                line, token_type = line.split()[0][1:-1], line.split()[2]
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
