from queue import *
from math import sqrt

def dis(a : tuple, b : tuple):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def dixtra(start, end, edges : dict):
    nodes = list(edges.keys())

    # zbiór wierzchołków odwiedzonych
    visited = set()
    # słownik kosztów
    cost = { n: float('inf') for n in nodes }
    # słownik poprzedników
    parent = { n: None for n in nodes }
    # utwórz kolejke, w której elementy są ułożone nie w kolejności wprowadzania, lecz w kolejności priorytetu.
    q = PriorityQueue()
    # dodaj wierzchołek startowy
    q.put((0, start))
    cost[start] = 0
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
        if cur_n == end:
            break
        # dla wszystkich krawędzi z aktualnego wierzchołka    
        for nh in edges[cur_n]:
            # przerwij jeśli sąsiad był już odwiedzony
            if nh in visited: 
                continue  
            distance = dis(cur_n, nh)
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
    cur_n = end
    while cur_n is not None:
        path.append(cur_n)
        cur_n = parent[cur_n]
    #path.reverse()
    #path.pop()
    #path.append(start)
    return (path, visited)