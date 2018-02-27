from PIL import Image, ImageFilter, ImageDraw, ImageFont

baby = Image.open('Cat03.jpg')
print baby.size
print baby.format

# baby.thumbnail((150,150))
# baby = baby.resize((10,150))
# baby.save('baby_thumb.jpg')

# baby = baby.filter(ImageFilter.GaussianBlur(5))
# baby.save('blurred_baby.png')

canvas = ImageDraw.Draw(baby)
# canvas.rectangle([20,20,300,300], fill=(255,0,0))

font = ImageFont.truetype('/Library/Fonts/Brush Script.ttf',200)
canvas.text((30,1200), "gimme da gorbage", font = font, fill = (0,255,255))
baby.save('redbaby.jpg')
