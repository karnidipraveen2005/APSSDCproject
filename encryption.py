import cv2
import os
import hashlib
#  the cover image
cover_image_path = r"C:\Users\Praveen\Desktop\cybersecurity\stock.jpg"
img1 = cv2.imread(cover_image_path)
img1 = cv2.imread(cover_image_path)
if img1 is None:
    print("Image not found. check the file path and make sure the image exists")
    exit()
# the image you want to hide
secret_image_path = r"C:\Users\Praveen\Desktop\cybersecurity\car.jpg"
img2 = cv2.imread(secret_image_path)
img2 = cv2.imread(secret_image_path)
if img2 is None:
    print("Image not found. check the file path and make sure the image exists")
    exit()
password=input("Enter passcode:")
hash_object=hashlib.sha256(password.encode())
hashed_password=hash_object.digest()
d={}
c={}


# Hide img2 in img1
for y in range(img1.shape[0]):
    for x in range(img1.shape[1]):
        for c in range(img1.shape[2]):
            # Extract the pixel values
            pixel_cover = img1[y, x, c]
            pixel_secret = img2[y, x, c]

            # Modify the least significant bit (LSB) of cover pixel to embed secret pixel
            new_pixel_cover = (pixel_cover & 254) | (pixel_secret >> 7)

            # Update cover image pixel with modified value
            img1[y, x, c] = new_pixel_cover

output_image_path = r"C:\Users\Praveen\Desktop\cybersecurity\hidden_image.jpg"
cv2.imwrite(output_image_path, img1)
os.startfile(output_image_path)
print(f"Message has been encoded into '{output_image_path}'.")
