from PIL import Image, ImageFilter

# Open the image file
img = Image.open('image-manupulation\grogu.jpg')

# Resize the image
width, height = img.size
img = img.resize((width//2, height//2))

# Crop the image
img = img.crop((0, 0, width//2, height//2))

# Rotate the image
img = img.rotate(45)

# Apply a filter to the image
img = img.filter(ImageFilter.BLUR)

# Save the manipulated image
img.save('example_manipulated.jpg')
