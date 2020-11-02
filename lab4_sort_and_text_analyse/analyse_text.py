from lab2_graph_and_token.text_reader import TextReader
from collections import defaultdict, deque


SPECIAL = {".", "!", "?", ",", "-", "...", ";", ":"}


def count_words(path):
    counted_words = defaultdict(int)
    for word in TextReader.read_tokens_txt(path):
        if word not in SPECIAL:
            counted_words[word] += 1
    return counted_words


def count_word_sets(path, n=2):
    counted_word_sets = defaultdict(int)
    current = deque()
    for word in TextReader.read_tokens_txt(path):
        if word not in SPECIAL:
            current.append(word)
            if len(current) >= n:
                counted_word_sets[" ".join(current)] += 1
                current.popleft()
    return counted_word_sets


def get_top_from_dict(dictionary, n=None):
    words = list(dictionary.keys())
    if n is None:
        return sorted(words, key=lambda x: dictionary[x], reverse=True)
    else:
        result = []
        last = 0
        for i in range(20):
            most_popular = max(words, key=lambda x: dictionary[x])
            result += [most_popular]
            words.remove(most_popular)
            last = dictionary[most_popular]
        most_popular = max(words, key=lambda x: dictionary[x])
        while dictionary[most_popular] == last:
            result += [most_popular]
            words.remove(most_popular)
            most_popular = max(words, key=lambda x: dictionary[x])
        return result


if __name__ == '__main__':
    print(get_top_from_dict(count_words('potop.txt')), '\n\n\n')
    print(get_top_from_dict(count_word_sets('potop.txt', 2), 20), '\n\n\n')
    print(get_top_from_dict(count_word_sets('potop.txt', 3), 20))
