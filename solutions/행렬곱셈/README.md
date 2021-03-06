# 행렬 곱셈

두 이차원 배열이 주어졌을 때, 행렬의 곱셈을 구하는 문제였다.

## 풀이 순서
1. 두번째 행렬의 행과 열을 바꾼다.
   1. 두번째 행렬의 행과 열을 바꾸면 첫번째 행렬의 row와 두번째 행렬의 row를 비교하여 계산하면 편하기 때문이다.
2. 첫번째 행렬과 두번째 행렬의 각 원소의 곱셈 합을 정답에 저장한다.


## 재밌었던 점

### 행렬의 행과 열을 치환하는 방법

풀이를 편하게 하기 위해서는 두번째 배열에서 원하는 원소에 접근을 편하게 해야한다.
그 방법으로 행렬의 행과 열을 바꿔주는(90도 회전) 방법으로 접근했다. 

```python
def rotation_90_degree(arr):
    row = len(arr)
    col = len(arr[0])

    new_arr = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            new_arr[j][i] = arr[i][j]

    return new_arr
```

1. 행렬의 row, col 수를 구하고 이를 반대로 새로운 행렬을 초기화한다.
2. 모든 배열 원소를 순회하며, 인덱스를 반전해서 새로운 배열에 원소를 추가한다.

하지만, 위 함수는 `zip` 을 사용하면 단 한줄로 처리할 수 있다.

```python
arr2 = list(zip(*arr2))
```
내부 동작 순서는 다음과 같다.
1. 배열에 있는 각 row를 *를 사용해서 zip에 argument로 추가한다.
2. 각 row의 원소가 zip에 의해 하나씩 꺼내진다.