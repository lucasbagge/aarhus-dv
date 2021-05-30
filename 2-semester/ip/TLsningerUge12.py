# Exercise 21.1 (job scheduling)
from heapq import heappush, heappop
import matplotlib.pyplot as plt
from time import time


# a.
def solve(jobs):
    heap = []
    heappush(heap, (0, 1))
    # heap.append((0, 1))
    res = [0] * len(jobs)
    last_machine = 1

    jobs = [(start, end, i) for (i, (start, end)) in enumerate(jobs)]

    for start, end, i in sorted(jobs):
        print(heap)
        free_time, machine = heappop(heap)
        print((free_time, machine))
        # free_time, machine = min(heap)
        # heap.remove((free_time, machine))
        if free_time >= start:
            heappush(heap, (free_time, machine))
            # heap.append((free_time, machine))
            last_machine += 1
            machine = last_machine

        heappush(heap, (end, machine))
        # heap.append(end, machine)
        res[i] = machine
    return res


# b.
def visualize(jobs, schedule):
    for idx, ((start, end), machine) in enumerate(zip(jobs, schedule)):
        plt.plot([start, end], [machine, machine], "g-o")
        plt.text((start + end) / 2, machine, str(idx),
                 horizontalalignment="center", va="bottom")
    plt.ylabel("Machine")
    plt.xlabel("Time")
    plt.ylim(0, max(schedule) + 1)
    plt.yticks(range(1, max(schedule) + 1))
    plt.show()


# c.
jobs = [(1, 5),
        (6, 7),
        (3, 8),
        (2, 4),
        (8, 10),
        (5, 9),
        (1, 2),
        (9, 10)]

schedule = solve(jobs)
print(schedule)
visualize(jobs, schedule)

#Exercise 22.1 (reading csv)
import csv
def load_max_flow(file_name):
    with open(file_name) as f:
        edges = []
        csv_reader = csv.reader(f)
        source, sink = next(csv_reader)
        for u, v, capacity in csv_reader:
            edges.append((u, v, int(capacity)))
    return edges, source, sink

#Exercise 22.2 (re.slit)
import re
string = 'this.was a test!, and here comes   :   the rest'
print(re.split(r'\s*[!?;:.,]+\s*', string))

#Exercise 22.3 (regular expression)
import re
import csv

import re
with open('words.txt', encoding='utf-8') as f:
     words = f.readlines()

#print(words[0:100])

words = [w.split(';')[0] for w in words]

words = {re.sub('^[1-9]. |[ .]', '', w).lower() for w in words}
# Vi fjerne 1 til 9, eller [ .] (mellemrum punktum)


#Exercise 22.4 (find frequent phrases)
from collections import Counter
import re
with open('saxo.txt') as f:
    text = f.read().lower()
phrases = re.findall(r'\bthe\s\w+', text)
#phrases  = [re.sub('\n', ' ', w).lower() for w in phrases]
print(phrases)
for phrase, count in Counter(phrases).most_common(10):
    print(f'{count:3} {phrase}')