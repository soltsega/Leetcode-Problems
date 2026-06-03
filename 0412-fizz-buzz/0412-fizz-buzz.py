# Technique used: Iteration
# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []
        
        # Start at 1 and include n
        for i in range(1, n + 1):
            # Check the most strict condition first
            if i % 3 == 0 and i % 5 == 0:  # or: if i % 15 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i)) # Convert to string type
                
        return output