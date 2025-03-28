class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        sorted_meetings = sorted(meetings, key = lambda x: x[0])
        last_day = 0
        free = 0
        for meeting in sorted_meetings:
            if last_day < meeting[0]:
                free += meeting[0] - last_day - 1
            if meeting[1] > last_day:
                last_day = meeting[1]
        free += days - last_day 
        return free
