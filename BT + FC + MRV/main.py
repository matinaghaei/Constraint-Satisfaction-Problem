from search import Search

v = int(input())
e = int(input())

nodes = input().split()

neighbours = []
for i in range(e):
    neighbours.append(list(map(int, input().split())))

Search(nodes, neighbours)
