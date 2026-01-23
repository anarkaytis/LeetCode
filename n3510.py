class Solution:
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

    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        disorder_cnt = 0
        ll = [{} for _ in range(n)]
        for i in range(n):
            ll[i]["num"] = nums[i]
            ll[i]["sum"] = nums[i] + nums[i + 1] if i != n - 1 else 0
            ll[i]["disorder"] = nums[i] > nums[i + 1] if i != n - 1 else False
            if ll[i]["disorder"]:
                disorder_cnt += 1
            ll[i]["prev"] = ll[i - 1] if i != 0 else None
            ll[i]["next"] = ll[i + 1] if i != n - 1 else None
            ll[i]["idx"] = i
            ll[i]["heap_idx"] = i if i != n - 1 else -1
        
        heap_size = n - 1
        for i in range(heap_size // 2, -1, -1):
            self.siftDown(ll, i, heap_size)

        while (disorder_cnt != 0) and (heap_size != 0):
            node = ll[0]
            discarded = node["next"]
            d_next = discarded["next"]
            prev = node["prev"]
            node["num"] = node["sum"]

            if d_next is not None:
                node["sum"] += d_next["num"]
            else:
                heap_size -= 1
                ll[0] = ll[heap_size]
                ll[heap_size] = node
                ll[0]["heap_idx"] = 0
                node["heap_idx"] = -1
            self.siftDown(ll, 0, heap_size)
            
            if prev is not None:
                prev["sum"] = prev["num"] + node["num"]
                self.siftUp(ll, prev["heap_idx"])
                self.siftDown(ll, prev["heap_idx"], heap_size)
                disorder_cnt -= 1 if prev["disorder"] else 0
                prev["disorder"] = prev["num"] > node["num"]
                disorder_cnt += 1 if prev["disorder"] else 0
                print(disorder_cnt)

            disorder_cnt -= 1 if discarded["disorder"] else 0
            disorder_cnt -= 1 if node["disorder"] else 0
            node["disorder"] = False
            node["next"] = d_next

            if d_next is not None:
                d_next["prev"] = node
                node["disorder"] = node["num"] > d_next["num"]
                disorder_cnt += 1 if node["disorder"] else 0
                print("d_next disorder")
                print(disorder_cnt)

            if discarded["heap_idx"] >= 0:
                heap_size -= 1
                last = ll[heap_size]
                ll[discarded["heap_idx"]] = last
                last["heap_idx"] = discarded["heap_idx"]
                if last["heap_idx"] < heap_size:
                    self.siftUp(ll, last["heap_idx"])
                    self.siftDown(ll, last["heap_idx"], heap_size)

            discarded["num"] = 0
            discarded["sum"] = 0
            discarded["disorder"] = False
            discarded["heap_idx"] = -1
            discarded["prev"] = None
            discarded["next"] = None

        return n - heap_size - 1 
