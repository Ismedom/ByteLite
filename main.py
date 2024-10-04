# 
# 
from PIL import Image
import os
import sys

# 
# 

def compress_image(input_path, output_path, quality):
    try:
        with Image.open(input_path) as img:
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            img.save(output_path, optimize=True, quality=quality)
            
            original_size = os.path.getsize(input_path)
            compressed_size = os.path.getsize(output_path)
            compression_percent = (original_size - compressed_size) / original_size * 100
            
            print(f"\nProcessing: {os.path.basename(input_path)}")
            print(f"Original size: {original_size:,} bytes")
            print(f"Compressed size: {compressed_size:,} bytes")
            print(f"Compression: {compression_percent:.2f}%")
            
    except IOError as e:
        print(f"Error processing {input_path}: {str(e)}")
        return False
    
    return True
# 
# 
# 



def process_directory(input_dir, output_dir, quality):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.webp')
    successful = 0
    failed = 0

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            if compress_image(input_path, output_path, quality):
                successful += 1
            else:
                failed += 1
    
    GREEN = "\033[92m"
    RESET = "\033[0m"

    print(f"\n{GREEN}Compression Complete!{RESET}")
    print(f"{GREEN}Successfully compressed: {successful} images{RESET}")
    print(f"{GREEN}Failed to compress: {failed} images{RESET}")
    
# 
# 
# 

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(script_dir, "input")
    output_dir = os.path.join(script_dir, "output")
    
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        sys.exit(1)
    
    compression_quality = 85
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Compression quality: {compression_quality}")
    
    process_directory(input_dir, output_dir, compression_quality)

# 
# 
# 


if __name__ == "__main__":
    main()
