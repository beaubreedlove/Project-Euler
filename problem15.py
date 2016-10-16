
# Lattics Paths

cache = {}

def lattice_paths(i, j):
    if i > j:
        k = i
        i = j
        j = k

    if i == 0:
        return 1

    if (i,j) in cache:
        return cache.get((i,j))
    
    r = lattice_paths(i, j - 1) + lattice_paths(i - 1, j)

    cache[(i,j)] = r

    return r

print lattice_paths(20, 20)


