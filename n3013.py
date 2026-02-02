class Num:
    def __init__(self, val: int):
        self.val = val
        self.idx = None
        self.heap = None

class Heap:
    def __init__(self, cmp: Callable[[Num, Num], int]):
        self.heap = []
        self.cmp = cmp

    def siftUp(self, idx0: int) -> None:
        item = self.heap[idx0]
        item.heap = self
        while idx0 > 0:
            idx1 = (idx0 - 1) // 2
            if self.cmp(item, self.heap[idx1]) > 0:
                break
            self.heap[idx0] = self.heap[idx1]
            self.heap[idx0].idx = idx0
            idx0 = idx1
        self.heap[idx0] = item
        self.heap[idx0].idx = idx0

    def siftDown(self, idx0: int) -> None:
        item = self.heap[idx0]
        item.heap = self
        while True:
            idx1 = idx0 * 2 + 1
            if idx1 >= len(self.heap):
                break
            if (idx1 + 1 < len(self.heap)) and (self.cmp(self.heap[idx1 + 1], self.heap[idx1]) < 0):
                idx1 += 1
            if (self.cmp(item, self.heap[idx1]) < 0):
                break
            self.heap[idx0] = self.heap[idx1]
            self.heap[idx0].idx = idx0
            idx0 = idx1
        self.heap[idx0] = item
        self.heap[idx0].idx = idx0

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        entities = [Num(nums[i]) for i in range(1, len(nums))]
        minh = Heap(lambda x,y : x.val - y.val)
        maxh = Heap(lambda x,y : y.val - x.val)
        sum = 0
        k -= 1
        dist += 1

        for i in range(k):
            sum += entities[i].val
            maxh.heap.append(entities[i])
            maxh.siftUp(i)

        best = sum
        for i in range(k, len(entities)):
            if i - dist >= 0:
                heap = entities[i - dist].heap
                idx = entities[i - dist].idx
                entity = heap.heap.pop()
                if idx < len(heap.heap):
                    heap.heap[idx] = entity
                    heap.siftUp(idx)
                    heap.siftDown(idx)
                if len(maxh.heap) < k:
                    sum -= entities[i - dist].val

            if entities[i].val < maxh.heap[0].val:
                maxh.heap.append(entities[i])
                maxh.siftUp(len(maxh.heap) - 1)
                sum += entities[i].val
            else:
                minh.heap.append(entities[i])
                minh.siftUp(len(minh.heap) - 1)

            if len(maxh.heap) > k:
                sum -= maxh.heap[0].val
                minh.heap.append(maxh.heap[0])
                minh.siftUp(len(minh.heap) - 1)
                maxh.heap[0] = maxh.heap.pop()
                maxh.siftDown(0)
            elif len(maxh.heap) < k:
                sum += minh.heap[0].val
                maxh.heap.append(minh.heap[0])
                maxh.siftUp(len(maxh.heap) - 1)
                entity = minh.heap.pop()
                if len(minh.heap) > 0:
                    minh.heap[0] = entity
                    minh.siftDown(0)
            best = min(best, sum)
        
        return best + nums[0]
