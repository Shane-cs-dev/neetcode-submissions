class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        print(count)
        max_freq_test = 0
        max_count_test = 0
        for key, value in count.items():
            if value > max_freq_test:
                max_freq_test = value
                max_count_test = 1
            elif value == max_freq_test:
                max_count_test += 1
        print(max_count_test)

        # Create a list to track the frequency
        freq = [0] * 26

        # Loop through the task and update the frequency
        max_freq = 0
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
            if freq[ord(task) - ord('A')] > max_freq:
                max_freq = freq[ord(task) - ord('A')]
        
        # Find the count for max freq
        max_count = 0
        for i in range(len(freq)):
            max_count += 1 if freq[i] == max_freq else 0
        print(max_count)
        
        time = (max_freq_test - 1) * (n + 1) + max_count_test
        return max(time, len(tasks))
