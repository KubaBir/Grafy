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


def tabela_krawedzi(nastepnicy):
    krawedzie = []
    for index, element in enumerate(nastepnicy):
        for i in element:
            krawedzie.append([index, i])
    return krawedzie


def main():
    n = int(input("Podaj ilosc krawedzi w grafie: "))
    sasiedztwo = macierz_sasiedztwa(n)  # Tworzenie macierzy sąsiedztwa
    print(*sasiedztwo, sep='\n')
    # Tworzenie listy następników
    nastepnicy = lista_nastepnikow(sasiedztwo, n)
    print(*nastepnicy)
    krawedzie = tabela_krawedzi(nastepnicy)  # Tworzenie tabeli krawędzi


if __name__ == '__main__':
    main()
