# A program that draws a picture of the Dartmouth quilt hanging in the Life Sciences Center
# By Ilona Kiss and Alana Juric

from cs1lib_changed import *

# drawing the quilt
def draw_quilt():

    # base background with outside border
    enable_stroke()
    set_stroke_color(.361, 0, .11)
    set_stroke_width(5)
    enable_fill()
    set_fill_color(.082, .02, .278)
    draw_rectangle(0, 0, 800, 800)

    # inner rectangle with border
    set_stroke_color(.404, .404, 0)
    set_stroke_width(20)
    draw_rectangle(30, 30, 740, 740)

    # grass
    disable_stroke()
    set_fill_color(0, .322, 0)
    draw_rectangle(40, 650, 720, 110)
    
    # roof
    set_fill_color(.204, .486, .204)
    draw_rectangle(200, 450, 400, 50)

    # Dartmouth Hall body
    set_fill_color(.933, .969, .863)
    draw_rectangle(200, 500, 400, 150)

start_graphics(draw_quilt)
