class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):

        new_edges = []
        for i, edge in enumerate(edges):
            new_edges.append([edge[0], edge[1], edge[2], i])

 
        new_edges.sort(key=lambda x: x[2])

        def kruskal(skip_edge=-1, force_edge=-1):
            parent = list(range(n))

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(x, y):
                px = find(x)
                py = find(y)

                if px == py:
                    return False

                parent[px] = py
                return True

            cost = 0
            edges_used = 0


            if force_edge != -1:
                u, v, w, _ = new_edges[force_edge]
                if union(u, v):
                    cost += w
                    edges_used += 1

            for i, (u, v, w, _) in enumerate(new_edges):

                if i == skip_edge:
                    continue

                if union(u, v):
                    cost += w
                    edges_used += 1


            if edges_used != n - 1:
                return float("inf")

            return cost


        base_cost = kruskal()

        critical = []
        pseudo = []

        for i in range(len(new_edges)):


            if kruskal(skip_edge=i) > base_cost:
                critical.append(new_edges[i][3])

            elif kruskal(force_edge=i) == base_cost:
                pseudo.append(new_edges[i][3])

        return [critical, pseudo]