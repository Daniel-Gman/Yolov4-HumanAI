import os
import zipfile
from PIL import Image
from io import BytesIO

# Path to the zip file
zip_path = r'C:\Users\Leina\OneDrive\Bureaublad\yolo-ai\yolo-opencv-detector-main\yolo-opencv-detector-main\yolov4-tiny\obj.zip'

# Folder where the converted JPGs will be saved
output_folder = r'C:\Users\Leina\OneDrive\Bureaublad\yolo-ai\yolo-opencv-detector-main\yolo-opencv-detector-main\yolov4-tiny\converted_jpg'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Open the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # Loop through the files in the zip
    for file_info in zip_ref.infolist():
        if file_info.filename.endswith('.png'):
            # Read the file
            with zip_ref.open(file_info) as file:
                # Open image from the file object
                img = Image.open(BytesIO(file.read()))

                # Convert PNG to JPG by removing the alpha channel
                rgb_img = img.convert('RGB')

                # Construct the output filename by changing .png to .jpg
                output_filename = os.path.basename(file_info.filename).replace('.png', '.jpg')

                # Save the new image in the output folder
                rgb_img.save(os.path.join(output_folder, output_filename), 'JPEG')

print("Conversion completed!")
