from queue import *

# s - wierzchołek startowy
# g - wierzchołek docelowy
# nodes - lista wierzchołków

s = '1'
g = '8'
nodes = ['1', '2', '3', '4', '5', '6', '7', '8']
edges_raw = [
    ['1', '2', 1],
    ['1', '3', 1],
    ['2', '5', 7],
    ['3', '4', 2],
    ['4', '6', 1],
    ['5', '6', 3],
    ['6', '7', 5],
    ['5', '8', 2],
    ['6', '8', 6],
]
edges = { n: list() for n in nodes }
for v1, v2, d in edges_raw:
    edges[v1].append([v2, d])
    edges[v2].append([v1, d])
    

# zbiór wierzchołków odwiedzonych
visited = set()
# słownik kosztów
cost = { n: float('inf') for n in nodes }
# słownik poprzedników
parent = { n: None for n in nodes }
# utwórz kolejke, w której elementy są ułożone nie w kolejności wprowadzania, lecz w kolejności priorytetu.
q = PriorityQueue()
# dodaj wierzchołek startowy
q.put((0,s))
cost[s] = 0
# dopóki kolejka nie jest pusta, czyli są jeszcze jakieś wierzchołki do odwiedzenia
while not q.empty():
    # pobierz wierzchołek o najmniejszym priotytecie i usuń go z kolejki
    _, cur_n = q.get()
    # przerwij jeśli odwiedzony
    if cur_n in visited:
      continue
    # dodaj wierzchołek do listy odwiedonych
    visited.add(cur_n)
      # przerwij jeśli dotarliśmy do celu
    if cur_n == g:
        break
    # dla wszystkich krawędzi z aktualnego wierzchołka    
    for nh, distance in edges[cur_n]:
        # przerwij jeśli sąsiad był już odwiedzony
        if nh in visited: 
          continue  
        # pobierz koszt sąsiada lub przypisz mu inf
        old_cost = cost[nh]
        # oblicz koszt dla danego wierzchołka 
        new_cost = cost[cur_n] + distance
        # rozważ nową ścieżkę tylko wtedy, gdy jest lepsza niż dotychczas najlepsze ścieżka
        if new_cost < old_cost:
            # zaktualizuj wartość sąsiada w słowniku kosztów
            cost[nh] = new_cost
            # ustaw poprzednika
            parent[nh] = cur_n
            # dodaj sąsiada do kolejki
            q.put((new_cost, nh))
# odtwórz ścieżkę
path = []
cur_n = g
while cur_n is not None:
    path.append(cur_n)
    cur_n = parent[cur_n]
path.reverse()

print(path)