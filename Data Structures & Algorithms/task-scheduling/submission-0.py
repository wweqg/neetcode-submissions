import heapq
from collections import deque, Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequencies of the tasks
        task_counts = Counter(tasks)
        
        # Step 2: Create a max-heap with the frequencies (using negative to simulate max-heap)
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)
        
        # Step 3: Queue to store the tasks that are cooling down
        cool_down = deque()  # Each element will be (time when the task can re-enter, task frequency)
        
        time = 0  # Keep track of the total time
        
        # Step 4: Process tasks while we have either tasks in the heap or tasks in cooldown
        while max_heap or cool_down:
            time += 1
            
            if max_heap:
                # Pop the most frequent task
                current_task = heapq.heappop(max_heap)
                current_task += 1  # Reduce frequency (because we're using negative values)
                
                # If there are still occurrences of the task, put it in cooldown
                if current_task < 0:
                    cool_down.append((time + n, current_task))
            
            # Check if any tasks in the cooldown are ready to re-enter the heap
            if cool_down and cool_down[0][0] == time:
                _, ready_task = cool_down.popleft()
                heapq.heappush(max_heap, ready_task)
        
        return time
