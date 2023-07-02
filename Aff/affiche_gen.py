from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Load the image
image_path = "path/to/your/image.jpg"
image = Image.open(image_path)

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define the font properties
font_path = "path/to/your/obitron_font.ttf"
font_size = 36
font_color = (255, 255, 255)  # white

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Define the text to be written
text = "Bold Obitron Text"

# Calculate the text position
text_width, text_height = draw.textsize(text, font)
x = (image.width - text_width) // 2
y = (image.height - text_height) // 2

# Define the border properties
border_color = (0, 0, 0)  # black
border_width = 2

# Draw the text shadow
shadow_offset = 4
shadow_color = (0, 0, 0, 128)  # black with transparency
shadow_position = (x + shadow_offset, y + shadow_offset)
draw.text(shadow_position, text, font=font, fill=shadow_color)

# Draw the text on the image
draw.text((x, y), text, font=font, fill=font_color)

# Add a border to the text
border_position = (x - border_width, y - border_width, x + text_width + border_width, y + text_height + border_width)
draw.rectangle(border_position, outline=border_color, width=border_width)

# Apply a slight blur effect to the border and shadow
image = image.filter(ImageFilter.BLUR)

# Save the modified image
output_path = "path/to/save/modified_image.jpg"
image.save(output_path)