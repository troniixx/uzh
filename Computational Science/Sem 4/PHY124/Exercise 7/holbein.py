import numpy as np
from PIL import Image

def reveal_skull(input_path, output_path, angle=75):
    img = Image.open(input_path)
    img_array = np.array(img)
    height, width, _ = img_array.shape

    output = np.zeros_like(img_array)
    angle_rad = np.radians(angle)
    
    # Approx location of the skull
    skull_start_y = int(height * 0.75)  # 75% of the image height
    
    # For each row of the image
    for y in range(height):
        # Apply stronger transformation to the skull area
        if y >= skull_start_y:
            # Compression factor based on distance from viewer
            # Simulates from the correct angle
            compression = np.tan(angle_rad)
            
            # Center offset
            center_x = width // 2
            
            for x in range(width):
                # Calculate source x-coordinate with perspective transformation
                # Transforms the elongated skull into proper shape
                offset = (x - center_x)
                src_x = center_x + int(offset * compression)
                
                # Ensure source coordinates are within image boundaries
                if 0 <= src_x < width:
                    output[y, x] = img_array[y, src_x]
        else:
            # Copy the original image for non-skull areas
            output[y] = img_array[y]
    
    result_img = Image.fromarray(output)
    result_img.save(output_path)
    print(f"Transformed image saved to {output_path}")
    
    return result_img

reveal_skull("/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 4/PHY124/Exercise 7/holbein.png", "skull_revealed_83.jpg")