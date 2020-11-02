"""
Czy te sortowania są stabilne?
- insertion sort - Tak.
-selection sort - Zależy od implementacji min (do stabilności potrzebowalibyśmy dodatkowej tablicy aby pamiętać indeksy
w orginalnej tablicy, zatem ta implementacja nie jest stabilna - widać na przykładzie poniżej).
"""


def insertion_sort(elements, value=lambda x: x):
    for i in range(len(elements)):
        current_val = value(elements[i])
        prev = i - 1
        while prev >= 0 and current_val < value(elements[prev]):
            elements[prev], elements[prev+1] = elements[prev+1], elements[prev]
            prev -= 1


def selection_sort(elements, value=lambda x: x):
    for i in range(len(elements)):
        min_val_idx = i + min(enumerate(elements[i:]), key=lambda x: value(x[1]))[0]
        elements[i], elements[min_val_idx] = elements[min_val_idx], elements[i]


if __name__ == "__main__":
    l1 = [6, 2, 5, 4, -3, 3, 0]
    insertion_sort(l1, value=lambda x: abs(x))
    print(l1)
    l2 = [6, 2, 5, -5, 4, -3, 3, -3, 0]
    selection_sort(l2, value=lambda x: abs(x))
    print(l2)
