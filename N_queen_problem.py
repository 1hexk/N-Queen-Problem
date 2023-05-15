import random
import heapq
import sys

sys.setrecursionlimit(10000)


class State:
    def __init__(self, queens, steps=0):
        self.queens = queens
        self.gn = steps

    def __lt__(self, other):
        return self.gn < other.gn

    def __hash__(self):
        return hash(tuple(self.queens))

    def __eq__(self, other):
        if isinstance(other, State):
            return self.queens == other.queens
        return False
    @staticmethod
    def random_state(n):
        if not isinstance(n, int):
            raise TypeError("n must be an integer")
        queens = [random.randint(1, n) for _ in range(n)]
        return State(queens)

    def IsGoal(self):
        n = len(self.queens)
        for i in range(n):
            for j in range(i + 1, n):
                if self.queens[i] == self.queens[j] or abs(self.queens[i] - self.queens[j]) == j - i:
                    return False
        return True

    def SuccessorFunction(self):
        states = set()
        n = len(self.queens)
        for i in range(n):
            for j in range(1, n + 1):
                if j != self.queens[i]:
                    new_queens = list(self.queens)
                    new_queens[i] = j
                    successor_state = State(new_queens, self.gn + 1)
                    states.add(successor_state)
        return list(states)

    def heuristic(self):
        attacks = 0
        n = len(self.queens)
        for i in range(n):
            for j in range(i + 1, n):
                if self.queens[i] == self.queens[j] or abs(self.queens[i] - self.queens[j]) == j - i:
                    attacks += 1
        return attacks

    def cost(self):
        return self.gn


def BFS(initial_state):
    steps = 0
    FIFO = [(initial_state, 0)]
    visited = {initial_state}
    search_cost = 0
    max_fringe_size = 1

    while FIFO:
        state, steps = FIFO.pop(0)

        if state.IsGoal():
            return state, steps, search_cost, max_fringe_size

        for successor_state in state.SuccessorFunction():
            if successor_state not in visited:
                visited.add(successor_state)
                FIFO.append((successor_state, steps + 1))
                search_cost += 1
                max_fringe_size = max(max_fringe_size, len(FIFO))

    return None, steps, search_cost, max_fringe_size


def DFS(initial_state):
    LIFO = [(initial_state, 0)]
    visited = {initial_state}
    steps = 0
    search_cost = 0
    max_fringe_size = 1

    while LIFO:
        state, steps = LIFO.pop()

        if state.IsGoal():
            return state, steps, search_cost, max_fringe_size

        for successor_state in state.SuccessorFunction():
            if successor_state not in visited:
                visited.add(successor_state)
                LIFO.append((successor_state, steps + 1))
                search_cost += 1
                max_fringe_size = max(max_fringe_size, len(LIFO))

    return None, steps, search_cost, max_fringe_size


def greedy(initial_state):
    heap = [(initial_state.heuristic(), initial_state)]
    visited = set()
    steps = 0
    search_cost = 0
    max_fringe_size = 1

    while heap:
        _, state = heapq.heappop(heap)
        visited.add(state)

        if state.IsGoal():
            return state, steps, search_cost, max_fringe_size

        for successor_state in state.SuccessorFunction():
            if successor_state not in visited and successor_state not in [s for _, s in heap]:
                heapq.heappush(heap, (successor_state.heuristic(), successor_state))
                search_cost += 1
                max_fringe_size = max(max_fringe_size, len(heap))

        steps += 1

    return None, steps, search_cost, max_fringe_size


def Astar(initial_state):
    heap = [(initial_state.heuristic() + initial_state.cost(), initial_state)]
    visited = set()
    steps = 0
    search_cost = 0
    max_fringe_size = 1

    while heap:
        _, state = heapq.heappop(heap)
        visited.add(state)

        if state.IsGoal():
            return state, steps, search_cost, max_fringe_size

        for successor_state in state.SuccessorFunction():
            if successor_state not in visited and successor_state not in [s for _, s in heap]:
                heapq.heappush(heap, (successor_state.heuristic() + successor_state.cost(), successor_state))
                search_cost += 1
                max_fringe_size = max(max_fringe_size, len(heap))

        steps += 1

    return None, steps, search_cost, max_fringe_size


def PrintBoard(queens):
    n = len(queens)
    for i in range(n):
        print(' ---' * n)
        for j in range(1, n + 1):
            p = 'Q' if queens[i] == j else ' '
            print('| %s ' % p, end='')
        print('|')
    print(' ---' * n)

def printinfo(steps, search_cost, max_fringe_size):
    print("Total number of steps to reach a solution (solution cost):", steps)
    print("Total number of nodes generated before reaching a solution (search cost):", search_cost)
    print("Maximum size of the frienge:", max_fringe_size)
