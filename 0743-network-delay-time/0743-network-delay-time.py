from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        # Build graph: Linked list
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # Min heap: (distance, node)
        heap = [(0, k)]

        # Shortest distances
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)

            # Already visited with shorter path
            if node in dist:
                continue

            dist[node] = time

            for nei, weight in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + weight, nei))

        # If not all nodes reached
        if len(dist) != n:
            return -1

        return max(dist.values())