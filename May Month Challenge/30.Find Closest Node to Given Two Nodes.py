class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        node1_visited = set()
        node2_visited = set()
        queue = deque([(node1, 1), (node2, 2)])
        found_node = float("inf")
        while queue:
            queue_len = len(queue)
            # traverse level-by-level with the for loop
            for _ in range(queue_len):
                curr, source = queue.popleft()
                if source == 1:
                    node1_visited.add(curr)
                if source == 2:
                    node2_visited.add(curr)
                if (source == 1 and curr in node2_visited) or (source == 2 and curr in node1_visited):
                    found_node = min(found_node, curr)
                if edges[curr] != -1:
                    if (source == 1 and edges[curr] in node1_visited) or (source == 2 and edges[curr] in node2_visited):
                        continue
                    queue.append((edges[curr], source))
            if found_node != float("inf"):
                return found_node
        return -1

  #Link : https://leetcode.com/problems/find-closest-node-to-given-two-nodes/?envType=daily-question&envId=2025-05-30
