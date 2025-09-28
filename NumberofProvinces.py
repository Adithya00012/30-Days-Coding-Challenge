from union_find import UnionFind

def find_connected_cities(cities):
    n = len(cities)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if cities[i][j] == 1:
                uf.union(i, j)

    return uf.count 
