# 행렬 회전

하나의 이차원 배열이 주어졌을 때, 시작점과 목적지를 정하면 시계 방향으로 회전하는 문제.

[문제 풀이 바로가기](https://programmers.co.kr/learn/courses/30/lessons/77485)

## 풀이 순서
1. 각 방향별로 배열을 한칸 씩 이동한다.
2. 마지막에 누락된 부분을 채워준다.

## 재밌었던 점
기존에 주어진 값을 행렬로 초기화하는 과정에서 발생한 문제로 몇시간을 고생했다.

```python
matrix = [[0] * columns for _ in range(rows)]

for i in range(rows):
    for j in range(columns):
        matrix[i][j] = i * columns + (j + 1)
```

가장 마지막 줄 숫자를 채워넣을 때, `i * columns` 를 `i * rows` 로 해서 문제가 발생했다. 
테스트 케이스에서는 N x N 행렬만 나왔기 때문에 오류를 찾을 수 없었다. 테스트 케이스를 더 구체적으로 세울 필요가 있겠다.