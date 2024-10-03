from PIL import Image

def encrypt_image(image_path, output_path, operation, value):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            
            if operation == 'add':
                r = (r + value) % 256
                g = (g + value) % 256
                b = (b + value) % 256
            elif operation == 'subtract':
                r = (r - value) % 256
                g = (g - value) % 256
                b = (b - value) % 256
            
            pixels[i, j] = (r, g, b)

    image.save(output_path)
    print(f"Image saved to {output_path}")

def decrypt_image(image_path, output_path, operation, value):
    reverse_op = 'subtract' if operation == 'add' else 'add'
    encrypt_image(image_path, output_path, reverse_op, value)

def main():
    operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt the image:\n").lower()
    
    # Use raw string for the image path
    image_path = r"c:\Users\Admin\Desktop\maulik\image.jpg"  # Your input image path
    output_path = input("Enter the output path for the image:\n")  # Enter output path
    value = int(input("Enter the value for pixel manipulation (e.g., shift value):\n"))
    
    if operation == 'encrypt':
        encrypt_image(image_path, output_path, 'add', value)
    elif operation == 'decrypt':
        decrypt_image(image_path, output_path, 'add', value)
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()
