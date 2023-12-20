
from queue import *

# s - wierzchołek startowy
# g - wierzchołek docelowy
# nodes - lista wierzchołków

s = 1
nodes = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
edges = {
    1: [1, 2],
    2: [1, 5],
    3: [1, 4],
    4: [3, 6],
    5: [2, 6, 8],
    6: [5, 8, 7],
    7: [6],
    8: [5, 6]
}
g = 8
# lista odwiedzonych wierzchołków
visited = set()
# słownik poprzedników
parent = { n: None for n in nodes }

q = Queue()

q.put(s)
# ustaw jego poprzednika jako jego samego, aby oznaczyć go jako odwiedzony
parent[s] = s
# dopóki kolejka nie jest pusta, czyli są jeszcze jakieś wierzchołki do odwiedzenia
while not q.empty():
  # pobierz następny wierzchołek i usuń go z kolejki
  cur_n = q.get()

  # przerwij jeśli dotarliśmy do celu
  if cur_n == g:
    break

  # dla wszystkich krawędzi z aktualnego wierzchołka
  for nh in edges.get(cur_n):
    # jeśli sąsiad nie był jeszcze odwiedzony
    if nh not in visited:
      # oznacz jako odwiedzony i dodaj do kolejki
      parent[nh] = cur_n
      visited.add(nh)
      q.put(nh)

# ścieżka do wierzchołka docelowego
path = []

# zaczynamy od wierzchołka docelowego i cofamy się po znalezionej ścieżce
cur_n = g
# dopóki nie dotrzemy do startu
while cur_n != s:
  # dodajemy aktualny wierzchołek i przechodzimy do poprzednika
  path.append(cur_n)
  cur_n = parent[cur_n]
# wierzchołki są w odwrotnej kolejności, więc odwracamy listę
path.append(s)
path.reverse()

print(path)