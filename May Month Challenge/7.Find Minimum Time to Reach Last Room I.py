class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0  
        pq = [(0, 0, 0)]
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        while pq:
            t, r, c = heapq.heappop(pq)
            if t > dist[r][c]:
                continue
            if r == n-1 and c == m-1:
                return t

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    depart = max(t, moveTime[nr][nc])
                    arrive = depart + 1
                    if arrive < dist[nr][nc]:
                        dist[nr][nc] = arrive
                        heapq.heappush(pq, (arrive, nr, nc))

        return -1  


# Link : https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/?envType=daily-question&envId=2025-05-07
