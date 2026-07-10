class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the array in ascending order 
        people.sort()

        # Create two pointers
        left, right = 0, len(people) - 1

        # Loop through the array and count the valid boat, and update the pointers
        count = 0
        while left <= right:
            # Both people is within the limitation
            if people[left] + people[right] <= limit:
                count += 1
                left += 1
                right -= 1
            elif people[right] <= limit:
                count += 1
                right -= 1
            else:
                count += 1
                left += 1
        
        return count
        