import time
import os
"""
    Reads a file, extracts hex values before the colon, 
    removes '0x', sorts them, and saves to a new file.
"""
def process_hex_file(input_filename, output_filename, limit=900000):
  
    hex_values = []
    start_time = time.time()

    print(f"--- Starting Process ---")
    
    # Check if file exists before trying to open it
    if not os.path.exists(input_filename):
        print(f"Error: The file '{input_filename}' was not found.")
        return

    try:
        # Read and Parse
        print(f"Reading first {limit} lines from {input_filename}...")
        with open(input_filename, 'r') as infile:
            for i, line in enumerate(infile):
                if i >= limit:
                    break
                parts = line.split(':')
                if parts:
                    # Remove '0x' and strip whitespace/newlines
                    clean_hex = parts[0].strip().replace('0x', '')
                    if clean_hex:
                        hex_values.append(clean_hex)

        # Sort the data
        print(f"Sorting {len(hex_values)} items...")
        hex_values.sort()

        # Write to new file
        print(f"Writing results to {output_filename}...")
        with open(output_filename, 'w') as outfile:
            for value in hex_values:
                outfile.write(value + '\n')

        end_time = time.time()
        duration = end_time - start_time
        print(f"--- Success! ---")
        print(f"Total time: {duration:.2f} seconds")
        print(f"Processed file saved as: {output_filename}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

INPUT_FILE = '/mnt/c/Users/neoro/pwnedpasswords.txt' 
OUTPUT_FILE = 'processed_data.txt'

if __name__ == "__main__":
    process_hex_file(INPUT_FILE, OUTPUT_FILE)
