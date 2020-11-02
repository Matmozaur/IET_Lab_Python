"""
Czy te sortowania są stabilne?
- insertion sort - Tak.
-selection sort - Zależy od implementacji min (do stabilności potrzebowalibyśmy dodatkowej tablicy aby pamiętać indeksy
w orginalnej tablicy, zatem ta implementacja nie jest stabilna - widać na przykładzie poniżej).
"""
import operator


def insertion_sort(elements, key=lambda x: x, reverse=False):
    compare = operator.gt if reverse else operator.lt
    for i in range(len(elements)):
        current_val = key(elements[i])
        prev = i - 1
        while prev >= 0 and compare(current_val, key(elements[prev])):
            elements[prev], elements[prev+1] = elements[prev+1], elements[prev]
            prev -= 1


def selection_sort(elements, key=lambda x: x, reverse=False):
    find_first = max if reverse else min
    for i in range(len(elements)):
        min_val_idx = i + find_first(enumerate(elements[i:]), key=lambda x: key(x[1]))[0]
        elements[i], elements[min_val_idx] = elements[min_val_idx], elements[i]


if __name__ == "__main__":
    l1 = [6, 2, 5, 4, -3, 3, 0]
    insertion_sort(l1, key=lambda x: abs(x))
    print('l1 ascending:\n', l1, '\n')
    l1 = [6, 2, 5, 4, -3, 3, 0]
    insertion_sort(l1, key=lambda x: abs(x), reverse=True)
    print('l1 descending:\n', l1, '\n')
    l2 = [6, 2, 5, -5, 4, -3, 3, -3, 0]
    selection_sort(l2, key=lambda x: abs(x))
    print('l2 ascending:\n', l2, '\n')
    l2 = [6, 2, 5, -5, 4, -3, 3, -3, 0]
    selection_sort(l2, key=lambda x: abs(x), reverse=True)
    print('l2 descending:\n', l2, '\n')
