import math
import cairo

WIDTH, HEIGHT = 5, 5
PIXELS = 100


surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH*PIXELS, HEIGHT*PIXELS)
ctx = cairo.Context(surface)
ctx.scale(PIXELS, PIXELS)

ctx.rectangle(0, 0, WIDTH, HEIGHT)  # Rectangle(x0, y0, x1, y1)
ctx.set_source_rgb(0.9, 0.9, 0.9)
ctx.fill()

# ctx.translate(0.1, 0.1)  # Changing the current transformation matrix

ctx.move_to(3, 3)
ctx.arc(2.3, 2.3, 1.5, 0, 4*math.pi)
ctx.set_source_rgb(0.9, 0.8, 0)
ctx.fill()

# ctx.translate(0.1, 0.1)  

#olho 1
ctx.move_to(6,6)
ctx.arc(1.85, 2.5, 0.22, 0, 2*math.pi)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

#olho 2
ctx.move_to(9,9)
ctx.arc(2.8, 2.5, 0.22, 0, 2*math.pi)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

#sombrancelha 1
ctx.move_to(6,6)
ctx.line_to(2, 1)
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(0.06)
ctx.stroke()


# ctx.set_source_rgb(1, 1, 0)
# ctx.set_line_width(0.04)
# ctx.stroke()

surface.write_to_png("teste.png")  # Output to PNG

print("File Saved")

