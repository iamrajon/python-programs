import heapq

class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        # This ensures that the Task with lower priority number has higher priority
        return self.priority < other.priority

    def __repr__(self):
        return f"Task(priority={self.priority}, description='{self.description}')"

# Create a priority queue (min-heap)
priority_queue = []

# Add tasks to the priority queue
heapq.heappush(priority_queue, Task(3, 'Write report'))
heapq.heappush(priority_queue, Task(1, 'Finish homework'))
heapq.heappush(priority_queue, Task(2, 'Go to gym'))
heapq.heappush(priority_queue, Task(4, 'Cook dinner'))

# Display the priority queue
print("Priority Queue:", priority_queue)

# Process tasks based on priority
while priority_queue:
    # Pop the highest priority task (lowest priority number)
    task = heapq.heappop(priority_queue)
    print(f"Processing task: {task}")




# Output:
# Priority Queue: [Task(priority=1, description='Finish homework'), Task(priority=3, description='Write report'), Task(priority=2, description='Go to gym'), Task(priority=4, description='Cook dinner')]
# Processing task: Task(priority=1, description='Finish homework')
# Processing task: Task(priority=2, description='Go to gym')
# Processing task: Task(priority=3, description='Write report')
# Processing task: Task(priority=4, description='Cook dinner')
