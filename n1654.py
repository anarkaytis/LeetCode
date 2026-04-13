from enum import Enum

class State(Enum):
    NOT_VISITED = 0
    R_FORWARD = 1
    R_BACKWARD = 2
    FORBIDDEN = 3

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        MAX_STATE = max(x, max(forbidden)) + a + b + 1
        state = [State.NOT_VISITED] * MAX_STATE
        steps = [0] * MAX_STATE
        q = deque()
        q.append(0)
        state[0] = State.R_FORWARD
        for f in forbidden:
            state[f] = State.FORBIDDEN

        while len(q) != 0:
            source = q.popleft()

            forward = source + a
            if (forward < MAX_STATE) and ((state[forward] == State.NOT_VISITED) or (state[forward] == State.R_BACKWARD)):
                q.append(forward)
                state[forward] = State.R_FORWARD
                steps[forward] = steps[source] + 1
                if forward == x:
                    return steps[forward]

            backward = source - b
            if (state[source] != State.R_BACKWARD) and (backward > 0) and (state[backward] == State.NOT_VISITED):
                q.append(backward)
                state[backward] = State.R_BACKWARD
                steps[backward] = steps[source] + 1
                if backward == x:
                    return steps[backward]
        return -1        
