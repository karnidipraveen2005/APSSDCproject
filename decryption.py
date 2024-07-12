import cv2
import os
import hashlib
# Path to the image containing the hidden data
encrypted_image_path = r"C:\Users\Praveen\Desktop\cybersecurity\hidden_image.jpg"
# Read the encrypted image
img_encrypted = cv2.imread(encrypted_image_path)
if img_encrypted is None:
    print(f"Error: Encrypted image not found ")
    exit()
password=input("Enter passcode:")
hash_object=hashlib.sha256(password.encode())
hashed_password=hash_object.digest()
extracted_image_path = r"C:\Users\Praveen\Desktop\cybersecurity\extracted_image.jpg"
# Initialize an image for the extracted data (same size as encrypted image)
img_extracted = img_encrypted.copy()

# Extract the hidden image from the encrypted image
for y in range(img_encrypted.shape[0]):
    for x in range(img_encrypted.shape[1]):
        for c in range(img_encrypted.shape[2]):
            # Extract the LSB (Least Significant Bit) from each pixel in encrypted image
            pixel_encrypted = img_encrypted[y, x, c]
            pixel_extracted = (pixel_encrypted & 1) * 255  # Set LSB to full intensity (either 0 or 255)

            # Update extracted image pixel with the extracted value
            img_extracted[y, x, c] = pixel_extracted


cv2.imwrite(extracted_image_path, img_extracted)
print(f"Hidden image has been extracted and saved to '{extracted_image_path}'.")
os.startfile(extracted_image_path)
