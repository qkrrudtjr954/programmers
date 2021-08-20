def solution(citations):
    n = len(citations)

    for h in range(n, 0, -1):
        more_than_h = [c for c in citations if c >= h]
        less_than_h = [c for c in citations if c <= h and c not in more_than_h]

        if len(more_than_h) >= h and len(less_than_h) <= h:
            return h

    return 0
