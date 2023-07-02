from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

FONT_SIZE = 62 
FONT_COLOR = (255, 255, 255)  # white
SHADOW_OFFSET = 5

def openImage(file:str) -> Image:
    image = Image.open(file)
    image.resize((1280,720))
    image.save("./image_temp.png", dpi=(72,72))
    return Image.open("./image_temp.png")

def loadFont() -> ImageFont:
    return ImageFont.truetype("assets/Orbitron-Bold.ttf", FONT_SIZE)

def calculateTextPosition(image:Image, text:str, font:ImageFont) -> tuple:
    _,_ ,text_width, text_height = font.getbbox(text)
    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2
    return (x,y)

def addShadow(image:Image, text:str, font:ImageFont, x:int, y:int) -> Image:
    shadow_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_image)
    shadow_position = (x + SHADOW_OFFSET, y + SHADOW_OFFSET)
    shadow_draw.text(shadow_position, text, font=font, fill=(0, 0, 0, 128))
    return Image.alpha_composite(image.convert("RGBA"), shadow_image)

def drawText(image:Image, text:str, font:ImageFont, x:int, y:int) -> Image:
    draw = ImageDraw.Draw(image)
    draw.text((x, y), text, font=font, fill=FONT_COLOR, spacing=21)
    return image

def saveImage(image:Image, output_path:str):
    image.save(output_path)
    os.remove("./image_temp.png")

if __name__ == "__main__":
    file = "./white_image.png"
    image = openImage(file)

    font = loadFont()
    print(image.info.get('dpi'))

    text = "FILM 1 - EIKICHI ONIZUKA"
    x_pos, y_pos = calculateTextPosition(image, text, font)

    image = addShadow(image, text, font, x_pos, y_pos)

    image = drawText(image, text, font, x_pos, y_pos)

    saveImage(image, "./image_modifier.png")
