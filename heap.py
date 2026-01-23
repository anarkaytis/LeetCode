def siftUp(self, heap: List[dict], idx0: int) -> None:
    item = heap[idx0]
    while idx0 > 0:
        idx1 = (idx0 - 1) // 2
        if (heap[idx1]["sum"] < item["sum"]) or ((heap[idx1]["sum"] == item["sum"]) and (heap[idx1]["idx"] < item["idx"])):
            break
        heap[idx0] = heap[idx1]
        heap[idx0]["heap_idx"] = idx0
        idx0 = idx1
    heap[idx0] = item
    heap[idx0]["heap_idx"] = idx0

def siftDown(self, heap: List[dict], idx0: int, n: int) -> None:
    item = heap[idx0]
    while True:
        idx1 = idx0 * 2 + 1
        if idx1 >= n:
            break
        if (idx1 + 1 < n) and ((heap[idx1 + 1]["sum"] < heap[idx1]["sum"]) or ((heap[idx1 + 1]["sum"] == heap[idx1]["sum"]) and (heap[idx1 + 1]["idx"] < heap[idx1]["idx"]))):
            idx1 += 1
        if (item["sum"] < heap[idx1]["sum"]) or ((item["sum"] == heap[idx1]["sum"]) and (item["idx"] < heap[idx1]["idx"])):
            break
        heap[idx0] = heap[idx1]
        heap[idx0]["heap_idx"] = idx0
        idx0 = idx1
    heap[idx0] = item
    heap[idx0]["heap_idx"] = idx0
