from PIL import Image, ImageEnhance

# Load the image
image_path = "/mnt/data/merdeiros.png"
image = Image.open(image_path)

# Enhance the skin tone by adjusting the brightness, contrast, and color
enhancer = ImageEnhance.Color(image)
image_enhanced = enhancer.enhance(0.5)  # Adjust the factor to change the skin tone

# Save the enhanced image
enhanced_image_path = "/mnt/data/merdeiros_enhanced.png"
image_enhanced.save(enhanced_image_path)

enhanced_image_path
