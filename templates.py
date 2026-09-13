"""자주 쓰는 알고리즘 템플릿 모음. 본문은 직접 채운다."""

import sys
import heapq
from bisect import bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from functools import cache
from typing import Any, Hashable, Iterable

sys.setrecursionlimit(10**6)


def bfs_grid(grid, start):
    """2D 그리드 BFS. start=(r, c)에서 시작해 최단 거리/방문 정보를 반환.

    grid: list[list[...]] — 벽/통로 표현은 문제마다 다름
    start: (row, col)
    return: dist 배열 또는 방문 집합 (문제에 맞게)
    """
    pass


def dfs_graph_iterative(adj, start):
    """인접 리스트 그래프의 반복문 DFS (재귀 깊이 회피용).

    adj: dict[node, list[node]] 또는 list[list[int]]
    start: 시작 노드
    return: 방문 순서 리스트
    """
    pass


def binary_search(nums, target):
    """정렬된 nums에서 target의 인덱스를 찾는다. 없으면 -1.

    bisect 사용 버전:
        i = bisect_left(nums, target)
        return i if i < len(nums) and nums[i] == target else -1
    ── 삽입 위치(lower bound)는 bisect_left, upper bound는 bisect_right.
    """
    pass


def two_pointers_sorted(nums, target):
    """정렬된 배열에서 합이 target인 두 수를 투 포인터로 찾는다.

    nums: 정렬된 리스트
    return: (i, j) 인덱스 쌍 또는 None
    """
    pass


def sliding_window_max_len(nums, k):
    """조건을 만족하는 최대 길이 윈도우를 구한다.

    nums: 입력 배열
    k: 제약값 (합 한계, 서로 다른 원소 개수 등 문제에 따라)
    return: 최대 윈도우 길이
    """
    pass


def prefix_sum(nums):
    """누적합 배열을 만든다. ps[i] = nums[:i]의 합, len(ps) == len(nums) + 1.

    구간 [l, r) 합 = ps[r] - ps[l]
    """
    pass


def difference_array(n, updates):
    """차분 배열로 구간 일괄 업데이트 후 최종 배열을 만든다.

    n: 배열 길이
    updates: [(l, r, val), ...] — [l, r] 구간에 val 더하기
    return: 최종 배열 (길이 n)
    """
    pass


def monotonic_stack_next_greater(nums):
    """각 원소의 오른쪽 첫 번째 더 큰 값을 단조 스택으로 구한다.

    return: 길이 n 리스트. 없으면 -1.
    """
    pass


def heap_top_k(nums, k):
    """상위 k개 원소를 힙으로 구한다.

    nums: 입력 배열
    k: 개수
    return: 상위 k개 리스트
    """
    pass


class UnionFind:
    """경로 압축 + union by size 를 쓰는 서로소 집합."""

    def __init__(self, n):
        """원소 0..n-1 로 초기화."""
        pass

    def find(self, x):
        """x의 루트를 반환 (경로 압축)."""
        pass

    def union(self, a, b):
        """a, b를 합친다. 이미 같은 집합이면 False."""
        pass


def dijkstra(adj, src):
    """가중치 그래프의 단일 출발점 최단 거리.

    adj: dict[node, list[(next_node, weight)]]
    src: 출발 노드
    return: dist 딕셔너리/리스트 (도달 불가는 inf)
    """
    pass


@cache
def memo_recursion_example(n):
    """메모이제이션 재귀 예시 (functools.cache).

    인자는 모두 hashable 이어야 한다. 리스트는 tuple로 바꿔서 넘길 것.
    클래스 메서드에 쓰면 self 가 캐시에 잡혀 누수되니 주의.
    """
    pass
