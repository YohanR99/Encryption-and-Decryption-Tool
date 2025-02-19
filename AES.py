import random
import time
import psutil
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to measure encryption time and CPU usage
def measure_performance(func, *args):
    start_time = time.time()
    psutil.cpu_percent(interval=None)  # Discard the first reading

    result = func(*args)

    end_time = time.time()
    cpu_usage = psutil.cpu_percent(interval=0.1)  # Measure CPU usage over a small interval
    execution_time = end_time - start_time

    return result, execution_time, cpu_usage

# Generate a random 128-bit AES key
def generate_aes_key():
    return get_random_bytes(16)  # 16 bytes = 128 bits key

# Encrypt message using AES in CBC mode
def encrypt_message_aes(key, message):
    cipher = AES.new(key, AES.MODE_CBC)  # AES in CBC mode
    iv = cipher.iv  # Initialization vector
    padded_message = pad(message.encode('utf-8'), AES.block_size)  # Pad message to match AES block size
    ciphertext = cipher.encrypt(padded_message)
    return iv, ciphertext

# Decrypt message using AES in CBC mode
def decrypt_message_aes(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Use the same key and IV for decryption
    padded_message = cipher.decrypt(ciphertext)
    message = unpad(padded_message, AES.block_size)
    return message.decode('utf-8')

# Main execution
if _name_ == "_main_":
    # Generate AES key
    aes_key = generate_aes_key()

    # Prompt user for input message to encrypt
    message = input("Enter the plaintext message to encrypt using AES: ")

    # Measure encryption time and CPU usage
    (iv, ciphertext), encryption_time, encryption_cpu = measure_performance(encrypt_message_aes, aes_key, message)

    # Print the ciphertext (in hexadecimal format)
    print(f"Ciphertext (hex): {ciphertext.hex()}")

    # Ask if user wants to decrypt the message with the key
    decrypt_choice = input("Do you want to decrypt the message with the AES key [y/n]? ").strip().lower()

    if decrypt_choice == 'y':
        # Measure decryption time and CPU usage
        decrypted_message, decryption_time, decryption_cpu = measure_performance(decrypt_message_aes, aes_key, iv, ciphertext)

        # Print the decrypted message
        print(f"Decrypted message: {decrypted_message}")

        # Write performance results to a text file
        with open("aes_performance.txt", "w") as log_file:
            log_file.write(f"Encryption Time: {encryption_time:.5f} seconds\n")
            log_file.write(f"Encryption CPU Usage: {encryption_cpu:.2f}%\n")
            log_file.write(f"Decryption Time: {decryption_time:.5f} seconds\n")
            log_file.write(f"Decryption CPU Usage: {decryption_cpu:.2f}%\n")
    else:
        # Write only encryption performance results to a text file
        with open("aes_performance.txt", "w") as log_file:
            log_file.write(f"Encryption Time: {encryption_time:.5f} seconds\n")
            log_file.write(f"Encryption CPU Usage: {encryption_cpu:.2f}%\n")
