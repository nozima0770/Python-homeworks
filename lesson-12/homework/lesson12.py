# Lesson 12 Homework
# task 1
import threading

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True  # <-- must be outside the for loop

# Worker function for threads
def check_primes(start, end, result_list):
    for num in range(start, end):
        if is_prime(num):
            result_list.append(num)

# Main function
def threaded_prime_checker(start_range, end_range, num_threads=4):
    threads = []
    results = [[] for _ in range(num_threads)]  # List to hold results for each thread
    range_size = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * range_size
        end = start_range + (i + 1) * range_size if i != num_threads - 1 else end_range
        thread = threading.Thread(target=check_primes, args=(start, end, results[i]))  # Removed extra space
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Combining results from all threads
    all_primes = []
    for sublist in results:
        all_primes.extend(sublist)

    all_primes.sort()
    print(f"Prime numbers in range({start_range}, {end_range}): \n{all_primes}")

# Example usage 
if __name__ == "__main__":
    threaded_prime_checker(1, 100, num_threads=4)

# task 2

import threading
from collections import Counter
import os

# Worker function for counting words in a chunk of lines
def count_words(lines, result_list, index):
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)
    result_list[index] = word_count

# Main function to perform threaded word counting
def threaded_word_counter(file_path, num_threads=4):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Read all lines from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []
    results = [None] * num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        thread = threading.Thread(target=count_words, args=(lines[start:end], results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Merge results from all threads
    total_count = Counter()
    for word_count in results:
        total_count.update(word_count)

    # Display summary
    print("Word Occurrences:")
    for word, count in total_count.most_common(20):  # Top 20 words
        print(f"{word}: {count}")

# Example usage
if __name__ == "__main__":
    
    threaded_word_counter(r"C:\Users\User\Desktop\txt file.txt", num_threads=4)

        
