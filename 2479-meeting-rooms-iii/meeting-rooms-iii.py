class Solution:
    # find the lowest empty room (binary search) it can be just earliest ending time
    # adjust the time and set the meeting to the room
    # keep track of the number of meetings in each room
    
    # how do you do the first step quickly? => heap (ending time, room no)
    # What if Room No.1 ends at 15, Room No.2 ends at 13 and next is 18? => You want to use Room No.1
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda meeting: meeting[0])
        max_mtg_room_no = 0
        meeting_counts = [0 for i in range(n)]
        min_heap = []
        unused = collections.deque()
        for i in range(n):
            unused.append(i)
        for meeting in meetings:
            while min_heap and min_heap[0][0] < meeting[0]:
                start, room_no = heapq.heappop(min_heap)
                heapq.heappush(min_heap, (meeting[0], room_no))
            if min_heap and min_heap[0][0] == meeting[0]:
                start, room_no = heapq.heappop(min_heap)
                end = meeting[1]
            elif len(unused) > 0:
                #print("you are here")
                room_no = unused.popleft()
                end = meeting[1]
            else:
                duration = meeting[1] - meeting[0]
                start, room_no = heapq.heappop(min_heap)
                end = start + duration
            meeting_counts[room_no] += 1
            heapq.heappush(min_heap, (end, room_no))
            if meeting_counts[room_no] > meeting_counts[max_mtg_room_no]:
                max_mtg_room_no = room_no
            elif meeting_counts[room_no] == meeting_counts[max_mtg_room_no] and room_no < max_mtg_room_no:
                max_mtg_room_no = room_no
        #print(meeting_counts)
        return max_mtg_room_no
        