from PIL import Image

image1 = Image.open(r'F:\image.png')

im1 = image1.convert('RGB')

im1.save(r'F:\converted.pdf')