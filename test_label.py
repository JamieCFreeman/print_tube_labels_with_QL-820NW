from PIL import Image, ImageDraw, ImageFont

# 300 dpi
DPI = 300

# 12 mm tape ≈ 142 pixels wide
tape_width = 142

# 0.5 inch long
label_length = int(0.5 * DPI)   # 150 pixels

# Landscape orientation
img = Image.new("RGB", (label_length, tape_width), "white")
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("arial.ttf", 34)
except:
    font = ImageFont.load_default()

text = "test"

bbox = draw.textbbox((0,0), text, font=font)
tw = bbox[2]-bbox[0]
th = bbox[3]-bbox[1]

draw.text(
    ((label_length-tw)//2,
     (tape_width-th)//2),
    text,
    fill="black",
    font=font
)

img.save("test.png")
