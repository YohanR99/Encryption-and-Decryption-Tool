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

    return hashing_speed, cpu_usage, memory_usage

if __name__ == "__main__":
    input_data_sizes = [10**3, 10**4, 10**5, 10**6]  # Sizes in bytes (1 KB, 10 KB, 100 KB, 1 MB)
    performance_data = []

    for size in input_data_sizes:
        input_data = 'A' * size  # Generating dummy input data of specified size
        hashing_speed, cpu_usage, memory_usage = measure_performance(input_data)
        
        performance_data.append({
            'Data Size (Bytes)': size,
            'Hashing Speed (Seconds)': hashing_speed,
            'CPU Usage (%)': cpu_usage,
            'Memory Usage (Bytes)': memory_usage
        })

    # Display collected data in a table format
    print("\nPerformance Analysis of SHA-256 Implementation:")
    print("{:<20} {:<20} {:<15} {:<20}".format('Data Size (Bytes)', 'Hashing Speed (Seconds)', 'CPU Usage (%)', 'Memory Usage (Bytes)'))
    for data in performance_data:
        print("{:<20} {:<20.6f} {:<15.2f} {:<20}".format(data['Data Size (Bytes)'], data['Hashing Speed (Seconds)'], data['CPU Usage (%)'], data['Memory Usage (Bytes)']))
