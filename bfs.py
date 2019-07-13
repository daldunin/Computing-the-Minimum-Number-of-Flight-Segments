#Uses python3

# Problem: Computing the Minimum Number of Flight Segments
# Problem Introduction
# You would like to compute the minimum number of flight segments to get from one city to another one. For
# this, you construct the following undirected graph: vertices represent cities, there is an edge between two
# vertices whenever there is a flight between the corresponding two cities. Then, it suffices to find a shortest
# path from one of the given cities to the other one.
# Problem Description
# Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges and two vertices 𝑢 and 𝑣, compute the length
# of a shortest path between 𝑢 and 𝑣 (that is, the minimum number of edges in a path from 𝑢 to 𝑣).
# Input Format. A graph is given in the standard format. The next line contains two vertices 𝑢 and 𝑣.
# Constraints. 2 ≤ 𝑛 ≤ 105, 0 ≤ 𝑚 ≤ 105, 𝑢 ̸= 𝑣, 1 ≤ 𝑢, 𝑣 ≤ 𝑛.
# Output Format. Output the minimum number of edges in a path from 𝑢 to 𝑣, or −1 if there is no path.

import sys
import queue


def distance(adj, s, t):
    #write your code here
    dist = [1000000]*n

    dist[s] = 0
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in adj[u]:
            if dist[v] == 1000000:
                q.put(v)
                dist[v] = dist[u] + 1

    if dist[t] != 1000000:
        return dist[t]

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
