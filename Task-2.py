from urllib.request import urlretrieve  # Download image from URL
from PIL import Image

def encrypt_decrypt(image_url, key, mode):
  """Encrypts or decrypts an image using pixel manipulation (download first).

  Args:
      image_url: URL of the image to process.
      key: A secret integer used for encryption/decryption.
      mode: 'encrypt' or 'decrypt'
  """
  # Download image from URL and store with a temporary filename
  filename = "temp_image.png"
  urlretrieve(image_url, filename)

  img = Image.open(filename)
  width, height = img.size
  pixels = img.load()

  for i in range(width):
    for j in range(height):
      r, g, b = pixels[i, j]  # Extract red, green, blue values
      if mode == 'encrypt':
        new_r = (r + key) % 256
        new_g = (g + key) % 256
        new_b = (b + key) % 256
      else:
        new_r = (r - key) % 256
        new_g = (g - key) % 256
        new_b = (b - key) % 256
      pixels[i, j] = (new_r, new_g, new_b)

  img.save(f"{filename[:-4]}_{mode}.png")  # Save with encryption/decryption suffix

  # Delete temporary image file
  import os
  os.remove(filename)

def main():
  """Prompts user for input and performs encryption/decryption."""
  print("Image Encryption Tool")
  image_url = input("Enter image URL: ")
  key = int(input("Enter secret key (integer): "))
  mode = input("Choose (encrypt/decrypt): ")

  if mode.lower() in ['encrypt', 'decrypt']:
    encrypt_decrypt(image_url, key, mode.lower())
    print(f"Image {mode}ed successfully!")
  else:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
  main()
