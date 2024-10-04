
# Simple Image Compression Script

This Python script compresses images in the `input` directory and outputs the compressed images to the `output` directory. It uses the `Pillow` library to handle image processing and supports multiple formats such as `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.webp`.

## Features

- Compresses images by reducing their quality while maintaining reasonable visual fidelity.
- Automatically converts images from RGBA (if present) to RGB to ensure compatibility with file formats like JPEG.
- Supports a variety of image formats including JPG, PNG, BMP, and WEBP.
- Displays compression statistics such as original size, compressed size, and percentage of compression for each image.
- Creates an `output` directory if it doesn’t exist.

## Requirements

- Python 3.x
- [Pillow](https://pillow.readthedocs.io/en/stable/) (PIL Fork)

## Installation

1. Clone or download this repository.
2. Install the required dependencies using `pip`:

   ```bash
   pip install Pillow
   ```

## Usage

1. Place the images you want to compress in the `input` folder located in the same directory as the script.
2. Run the script using the command:

   ```bash
   python script.py
   ```

3. Compressed images will be saved in the `output` directory.

## Configuration

- The default compression quality is set to `85`. You can modify this value in the `main()` function if you need to adjust the quality.
- The script processes all images in the `input` directory with the supported formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.webp`.

## Output

For each image processed, the script will display the following information:

- Original size in bytes
- Compressed size in bytes
- Compression percentage

Additionally, after processing all images, a summary will be printed showing:

- Total number of successfully compressed images
- Total number of images that failed to compress

## Example Output

```
Processing: example.jpg
Original size: 3,543,234 bytes
Compressed size: 2,345,123 bytes
Compression: 33.83%

Compression Complete!
Successfully compressed: 10 images
Failed to compress: 0 images
```
