
import hashlib
import time
import psutil
import os

def sha256_hash(data):
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Update the hash object with the encoded input data
    hash_object.update(data.encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return hash_object.hexdigest()

def measure_performance(input_data):
    # Record CPU and memory usage before hashing
    process = psutil.Process(os.getpid())
    initial_cpu = psutil.cpu_percent(interval=0.1)
    initial_memory = process.memory_info().rss

    # Measure the time taken to hash the data
    start_time = time.time()
    hash_result = sha256_hash(input_data)
    end_time = time.time()

    # Calculate the hashing speed (time taken)
    hashing_speed = end_time - start_time

    # Record CPU and memory usage after hashing
    final_cpu = psutil.cpu_percent(interval=0.1)
    final_memory = process.memory_info().rss

    # Calculate CPU and memory consumption
    cpu_usage = final_cpu - initial_cpu
    memory_usage = final_memory - initial_memory

    return hashing_speed, cpu_usage, memory_usage, hash_result

def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None

if __name__ == "__main__":
    input_file = 'input_file.txt'  # Specify the input file name
    input_data = read_file_content(input_file)
    
    if input_data:
        hashing_speed, cpu_usage, memory_usage, hash_result = measure_performance(input_data)

        # Display the performance data and the hash result
        print("\nPerformance Analysis of SHA-256 Implementation:")
        print(f"File Name: {input_file}")
        print(f"Hashing Speed (Seconds): {hashing_speed:.6f}")
        print(f"CPU Usage (%): {cpu_usage:.2f}")
        print(f"Memory Usage (Bytes): {memory_usage}")
        print(f"SHA-256 Hash: {hash_result}")