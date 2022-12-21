
import sys

file = sys.stdin.read().splitlines()
N = int(file[0])
tree = {}
persons = set()
parents = set()

for line in file[1:]:
    person, parent = line.split()
    tree.update({person: parent})

persons = list(tree.keys())
parents = list(tree.values())
primal = list(set(parents) - set(persons))
rang = {}
rang.update({primal[0]: 0})
r = 1
new_primal = []

while len(rang) < N:
    for i in range(len(parents)):
        if parents[i] in primal:
            rang.update({persons[i]: r})
            new_primal.append(persons[i])
        if i == len(parents) - 1:
            r += 1
            primal = new_primal
            new_primal = []

for name in sorted(list(rang.items())):
    print(*name)
