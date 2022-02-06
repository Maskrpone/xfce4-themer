from PIL import Image
from PIL import ImageColor
import os

name = input("What is the name of the theme ? :")

print("folder creation...")

os.system("mkdir "+ name)
os.system("mkdir " + name + "/" + "xfwm4/")

PATH = name + "/" + "xfwm4/"

hex1 = input("what color do you want for active windows ? : ")
rgb1 = ImageColor.getcolor(hex1, "RGB")

hex2 = input("what color do you want for inactive windows ?  : ")
rgb2 = ImageColor.getcolor(hex2, "RGB")

print("width : 10, height : 3, color for active windows : " + hex1 + ", color for inactive windows : " + hex2)
print("Generating theme...")

#bars active
active = ["bottom-active.png", "close-active.png", "close-prelight.png", "close-pressed.png", "hide-active.png", "hide-prelight.png", "hide-pressed.png", "maximized-active.png", "maximized-prelight.png", "maximized-pressed.png", "title-1-active.png", "title-2-active.png", "title-3-active.png", "title-4-active.png", "title-5-active.png"]

for i in range(len(active)):
	image = Image.new("RGB",(10,3) , rgb1)
	print(active[i])
	image.save(PATH + active[i], "png")

#bars inactive
inactive = ["bottom-inactive.png", "close-inactive.png", "hide-inactive.png", "maximized-inactive.png", "title-1-inactive.png", "title-2-inactive.png", "title-3-inactive.png", "title-4-inactive.png", "title-5-inactive.png"]

for i in range(len(inactive)):
	image = Image.new("RGB", (10,3), rgb2)
	print(inactive[i])
	image.save(PATH + inactive[i], "png")

#left right active

image = Image.new("RGB",(3,10) , rgb1)
image.save(PATH + "right-active.png", "png")
print("right-active.png")
image = Image.new("RGB",(3,10) , rgb2)
image.save(PATH + "right-inactive.png", "png")
print("right-inactive.png")
image = Image.new("RGB",(3,10) , rgb1)
image.save(PATH + "left-active.png", "png")
print("left-active.png")
image = Image.new("RGB",(3,10) , rgb2)
image.save(PATH + "left-inactive.png", "png")
print("left-inactive.png")

image = Image.new("RGB",(3,3) , rgb1)
image.save(PATH + "bottom-right-active.png", "png")
print("bottom-right-active.png")
image = Image.new("RGB",(3,3) , rgb2)
image.save(PATH + "bottom-right-inactive.png", "png")
print("bottom-right-inactive.png")
image = Image.new("RGB",(3,3) , rgb1)
image.save(PATH + "bottom-left-active.png", "png")
print("bottom-left-active.png")
image = Image.new("RGB",(3,3) , rgb2)
image.save(PATH + "bottom-left-inactive.png", "png")
print("bottom-left-inactive.png")

image = Image.new("RGB",(3,3) , rgb1)
image.save(PATH + "top-right-active.png", "png")
print("top-right-active.png")
image = Image.new("RGB",(3,3) , rgb2)
image.save(PATH + "top-right-inactive.png", "png")
print("top-right-inactive.png")
image = Image.new("RGB",(3,3) , rgb1)
image.save(PATH + "top-left-active.png", "png")
print("top-left-active.png")
image = Image.new("RGB",(3,3) , rgb2)
image.save(PATH + "top-left-inactive.png", "png")
print("top-left-inactive.png")

#themerc creation

os.system("touch " + PATH + "themerc")

os.system("echo 'button_offset=0' >> "+ PATH + "themerc")
os.system("echo 'button_spacing=0' >> "+ PATH + "themerc")
os.system("echo 'full_width_title=true' >> "+ PATH + "themerc")
os.system("echo 'title_shadow_active=false' >> "+ PATH + "themerc")
os.system("echo 'title_shadow_inactive=false' >> "+ PATH + "themerc")
os.system("echo 'title_horizontal_offset=0' >> "+ PATH + "themerc")
os.system("echo 'active_text_color=" + hex1 + "' >> "+ PATH + "themerc")
os.system("echo 'active_text_shadow_color=" + hex1 + "' >> "+ PATH + "themerc")
os.system("echo 'inactive_text_color=" + hex1 + "' >> "+ PATH + "themerc")
os.system("echo 'inactive_text_shadow_color="+ hex1 +"' >> "+ PATH + "themerc")
os.system("echo 'shadow_delta_height=2' >> "+ PATH + "themerc")
os.system("echo 'shadow_delta_width=0' >> "+ PATH + "themerc")
os.system("echo 'shadow_delta_x=0' >> "+ PATH + "themerc")
os.system("echo 'shadow_delta_y=-2' >> "+ PATH + "themerc")
os.system("echo 'shadow_opacity=80' >> "+ PATH + "themerc")
os.system("echo 'show_app_icon=false' >> " + PATH + "themerc")
os.system("echo 'button_layout=|HMC' >> " + PATH + "themerc")

print("themerc created.")
print("theme finished.")