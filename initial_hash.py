import hashlib
import time

def sha256_hash(data):
    # Create a SHA-256 hash object
    hash = hashlib.sha256()

    # Update the hash object with the encoded input data
    hash.update(data.encode('utf-8'))

    # Return the hexadecimal representation of the hash
    return hash.hexdigest()

if __name__ == "__main__":
    # Sample input data
    input_data = "Hello world "

    # Measure the time taken to hash the data
    start_time = time.time()
    hash_result = sha256_hash(input_data)
    end_time = time.time()

    # Calculate the hashing speed (time taken)
    hashing_speed = end_time - start_time

    # Display the hash result and hashing speed without showing the input text
    print(f"Input data: {input_data}")
    print(f"SHA-256 hash: {hash_result}")
    print(f"Hashing speed: {hashing_speed:.6f} seconds")