# Technique used: Resource ordering
# Time complexity: O(1) per call as each operation or method uses atomic contant time
# Space complexity: O(1) as each method return value holds constant atmomic space


import threading
from typing import Callable

class DiningPhilosophers:
    def __init__(self):
        # Initialize 5 locks, one for each fork
        self.forks = [threading.Lock() for _ in range(5)]

    # call the functions directly to execute, x()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: Callable[[], None],
                   pickRightFork: Callable[[], None],
                   eat: Callable[[], None],
                   putLeftFork: Callable[[], None],
                   putRightFork: Callable[[], None]) -> None:
        
        # Determine fork indices based on philosopher ID
        left_fork_idx = philosopher
        right_fork_idx = (philosopher + 1) % 5
        
        # Assign primary and secondary forks based on asymmetry (Even vs Odd)
        if philosopher % 2 == 0:
            first_fork = self.forks[left_fork_idx]
            second_fork = self.forks[right_fork_idx]
        else:
            first_fork = self.forks[right_fork_idx]
            second_fork = self.forks[left_fork_idx]
            
        # Acquire locks, execute actions, and release locks safely
        with first_fork:
            with second_fork:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()