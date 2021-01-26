from collections import Counter

def majority(alist):
    if alist is None:
        return []

    counts = Counter(alist)
    sorted_counts = sorted(counts, key=lambda x: -counts[x])
    major_element = sorted_counts[0]

    if counts[major_element] >= 2:
        return [i for i, elem in enumerate(alist)
                if elem == major_element]
    return []


#alist = []
#alist = [1,2]
#alist = [1, 1, 2]
alist = [3,1,2,2,3,3,3,4,5]
print(majority(alist))