from ast import NameConstant
import enum
from random import sample


def macierz_sasiedztwa(n):
    sasiedztwo = [[0 for _ in range(n)] for _ in range(n)]
    edges = (n*(n-1)//2)//2 + 1
    temp = []
    for i in range(n):
        for j in range(i+1, n):
            temp.append([i, j])
    temp = sample(temp, edges)
    for i in temp:
        sasiedztwo[i[0]][i[1]] = 1
    #print(*sasiedztwo, sep='\n')
    return sasiedztwo


def lista_nastepnikow(sasiedztwo, n):
    nastepnicy = [[] for _ in range(n)]
    for y, row in enumerate(sasiedztwo):
        for x, element in enumerate(row):
            if element != 0:
                nastepnicy[y].append(x)
    return nastepnicy


def sprawdzanie_spojnosci(sasiedztwo, n):
    for index in range(1, n):
        connected = False
        for row in sasiedztwo:
            if row[index] == 1:
                connected = True
        if not connected:
            sasiedztwo[0][index] = 1


def tabela_krawedzi(nastepnicy):
    krawedzie = []
    for index, element in enumerate(nastepnicy):
        for i in element:
            krawedzie.append([index, i])
    return krawedzie


def macierz_z_klawiatury(n):
    sasiedztwo = []
    while len(sasiedztwo) < n:
        try:
            sasiedztwo.append(list(map(int, input().split())))
        except ValueError:
            print("Podaj wartosci calkowitoliczbowe")
    return sasiedztwo


def bfs(graph, n):
    visited = [False] * n
    queue = []
    res = []
    for i in range(n):
        if graph[i] != [] and visited[i] == False:
            start_index = i
            break

    queue.append(start_index)
    visited[start_index] = True
    res.append(start_index)
    while queue:
        start_index = queue[0]
        queue.pop(0)
        for node in graph[start_index]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
                res.append(node)
    return res


def dfs(graph, n):
    visited = []
    for i in range(n):
        if graph[i] != []:
            start_index = i
            break
    res = []
    dfs_loop(graph, n, visited, res, start_index)
    return res


def dfs_loop(graph, n, visited, res, index):
    visited.append(index)
    res.append(index)

    for node in graph[index]:
        if node not in visited:
            dfs_loop(graph, n, visited, res, node)


# Sortowanie topologiczne bfs x3:
def topological_bfs_nastepnicy(graph, n):
    in_degree = [0] * n
    for i in graph:
        for j in i:
            in_degree[j] += 1
    queue = []
    for index, degree in enumerate(in_degree):
        if degree == 0:
            queue.append(index)
    res = []
    while queue:
        temp = queue.pop(0)
        res.append(temp)
        for i in graph[temp]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)
    return res


def topological_bfs_krawedzie(graph, n):
    in_degree = [0] * n
    for i in graph:
        in_degree[i[1]] += 1
    queue = []
    for index, degree in enumerate(in_degree):
        if degree == 0:
            queue.append(index)
    res = []
    while queue:
        temp = queue.pop(0)
        res.append(temp)
        for i in graph:
            if i[0] == temp:
                in_degree[i[1]] -= 1
                if in_degree[i[1]] == 0:
                    queue.append(i[1])
    return res


def topological_bfs_sasiedztwo(graph, n):
    in_degree = [0] * n
    for index, row in enumerate(graph):
        for i, element in enumerate(row):
            if row[i] == 1:
                in_degree[i] += 1
    queue = []
    for index, degree in enumerate(in_degree):
        if degree == 0:
            queue.append(index)
    res = []
    while queue:
        temp = queue.pop(0)
        res.append(temp)
        for index, i in enumerate(graph[temp]):
            if i == 1:
                in_degree[index] -= 1
                if in_degree[index] == 0:
                    queue.append(index)
    return res


# 1: Sasiedztwo 2: Nastepnicy 3: krawedzie
def topological_dfs(graph, n, mode):
    visited = [False] * n
    stack = []
    if mode == 1:
        for i in range(n):
            if visited[i] == False:
                topological_dfs_sasiedztwo(visited, stack, i, graph)
    if mode == 2:
        for i in range(n):
            if visited[i] == False:
                topological_dfs_nastepnicy(visited, stack, i, graph)
    if mode == 3:
        for i in range(n):
            if visited[i] == False:
                topological_dfs_krawedzie(visited, stack, i, graph)
    return stack[::-1]


def topological_dfs_nastepnicy(visited, stack, node, graph):
    visited[node] = True
    for i in graph[node]:
        if visited[i] == False:
            topological_dfs_nastepnicy(visited, stack, i, graph)
    stack.append(node)


def topological_dfs_krawedzie(visited, stack, node, graph):
    visited[node] = True
    for i in graph:
        if i[0] == node:
            if visited[i[1]] == False:
                topological_dfs_krawedzie(visited, stack, i[1], graph)
    stack.append(node)


def topological_dfs_sasiedztwo(visited, stack, node, graph):
    visited[node] = True
    for index, i in enumerate(graph[node]):
        if i == 1:
            if visited[index] == False:
                topological_dfs_sasiedztwo(visited, stack, index, graph)
    stack.append(node)


def main():
    n = int(input("Podaj ilosc krawedzi w grafie: "))
    if input("Nacisnij 1 aby wygenerowac graf lub 2, aby go wpisac: ") == "1":
        sasiedztwo = macierz_sasiedztwa(n)  # Macierz sasiedztwa
    else:
        sasiedztwo = macierz_z_klawiatury(n)
    print("Macierz sasiedztwa:", *sasiedztwo, sep='\n ')
    sprawdzanie_spojnosci(sasiedztwo, n)
    print("Macierz sasiedztwa:", *sasiedztwo, sep='\n ')
    input()
    nastepnicy = lista_nastepnikow(sasiedztwo, n)  # Lista nastepnikow
    print("Lista nastepnikow:\n", *nastepnicy)
    krawedzie = tabela_krawedzi(nastepnicy)  # Tabela krawedzi
    print("Tabela krawedzi:\n", *krawedzie)

    while (inp := input("\n1. BFS\n2. DFS\n3. Sortowanie topologiczne BFS\n4. Sortowanie topologiczne DFS\nWybor = ")) != ("q" or "0"):
        if inp == "1":
            print(bfs(nastepnicy, n))
        if inp == "2":
            print(dfs(nastepnicy, n))
        if inp == "3":
            temp = input(
                "1. Lista sasiedztwa\n2. Lista nastepnikow\n3. Tablica krawedzi\nWybor = ")
            if temp == "1":
                print(topological_bfs_sasiedztwo(sasiedztwo, n))
            if temp == "2":
                print(topological_bfs_nastepnicy(nastepnicy, n))
            if temp == "3":
                print(topological_bfs_krawedzie(krawedzie, n))
        if inp == "4":
            temp = input(
                "1. Lista sasiedztwa\n2. Lista nastepnikow\n3. Tablica krawedzi\nWybor = ")
            if temp == "1":
                print(topological_dfs(sasiedztwo, n, 1))
            if temp == "2":
                print(topological_dfs(nastepnicy, n, 2))
            if temp == "3":
                print(topological_dfs(krawedzie, n, 3))
        input()


if __name__ == '__main__':
    main()
