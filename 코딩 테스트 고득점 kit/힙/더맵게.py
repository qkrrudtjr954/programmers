import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0

    while any(K > s for s in scoville):
        if len(scoville) <= 1:
            return -1

        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)

        heapq.heappush(scoville, s1 + s2 * 2)

        answer += 1

    return answer
