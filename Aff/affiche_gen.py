from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageTk
import os

FONT_SIZE = 62 
FONT_COLOR = (255, 255, 255)  # white
SHADOW_OFFSET = 5

settings: tuple[int, int, bool]

def openImage(file:str) -> Image:
    image = Image.open(file)
    image.resize((1280,720))
    image.save("./assets/image_temp.png", dpi=(72,72))
    return Image.open("./assets/image_temp.png")

def loadFont() -> ImageFont:
    return ImageFont.truetype("assets/Orbitron-Bold.ttf", FONT_SIZE)

def calculateTextPosition(image:Image, text:str, font:ImageFont) -> tuple:
    _,_ ,text_width, text_height = font.getbbox(text)
    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2
    
    return (x, 280 +y)


def addShadow(image:Image, text:str, font:ImageFont) -> Image:
    shadow_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_image)
    _, _, text_width, text_height = font.getbbox(text)
    if text_width > 1180:
        top, bot = clac_bot_and_top(text)

        x, y = calculateTextPosition(image, top, font)

        shadow_position = (x + SHADOW_OFFSET, y - text_height + SHADOW_OFFSET)
        shadow_draw.text(shadow_position, top, font=font, fill=(0, 0, 0, 128))
    else:
        bot = text
        
    x, y = calculateTextPosition(image, bot, font)
    shadow_position = (x + SHADOW_OFFSET, y + SHADOW_OFFSET)
    shadow_draw.text(shadow_position, bot, font=font, fill=(0, 0, 0, 128))

    return Image.alpha_composite(image.convert("RGBA"), shadow_image)

def clac_bot_and_top(text:str) -> tuple:
    bot = ""
    top = ""
    words = text.split(" ")
    for i in range(0, len(words)):
        print(" ".join(words[i:]))
        print(round(len(text) * 0.4) < len(bot))
        if len(text) * 0.55 < len(top) and (len(" ".join(words[i:]))) < 1080:
            bot += words[i] + " "
        else:
            top += words[i] + " "
    return (top, bot)  

def drawText(image:Image, text:str, font:ImageFont) -> Image:
    draw = ImageDraw.Draw(image)
    _, _, text_width, text_height = font.getbbox(text)
    if text_width > 1180:
        top, bot = clac_bot_and_top(text)

        x, y = calculateTextPosition(image, top, font)
        draw.text((x, y - text_height), top, font=font, fill=FONT_COLOR, spacing=21)
    else:
        bot = text

    x, y = calculateTextPosition(image, bot, font)
    draw.text((x, y), bot, font=font, fill=FONT_COLOR, spacing=21)
    
    return image

def addLogoF(image:Image) -> Image:
    logo = Image.open("./assets/logo.png")
    # logo = logo.resize((int(logo.width * 0.5), int(logo.height * 0.5)))
    
    if settings[2] == True:
        image.paste(logo, (1150,0))
    else:
        image.paste(logo, (35, 0))
    return image

def addLogoS(image:Image) -> Image:
    logo = Image.open("./logo.png")
    width, height = logo.size[0] * (settings[0] / 100), logo.size[1] * (settings[0] / 100)
    print('w : ' + str(settings[0] / 100), "h : " + str(logo.size[0]))
    logo = logo.resize((int(width), int(height)))

    if settings[2] == True:
        image.paste(logo, (settings[1], settings[1]), mask=logo)
    else:
        image.paste(logo, (image.width - logo.size[0] - settings[1], settings[1]), mask=logo)
    return image

def renderImage(file:str, text, settings_: tuple[int, int, bool] = (50, 35, True)) -> Image:
    global settings 
    settings = settings_
    image = openImage(file)

    font = loadFont()
    print(image.info.get('dpi'))

    text = text # 34 characters

    image = addShadow(image, text, font)
    image = drawText(image, text, font)
    image = addLogoF(image)
    image = addLogoS(image)
    return image

def saveImage(image:Image, fileName:str):
    os.mkdir("./png") if not os.path.exists("./png") else None
    os.mkdir("./webp") if not os.path.exists("./webp") else None

    image.save("./png/" + fileName + ".png", dpi=(72,72))
    image.save("./webp/" + fileName + ".webp", dpi=(72,72))

