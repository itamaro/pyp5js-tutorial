def setup():
    fill("red")
    size(400, 400)

def draw():
    background(200)
    diameter = sin(frame_count / 60) * 50 + width / 2
    fill("magenta")
    ellipse(width / 2, height / 2, diameter, diameter/2)
    y = sin(7.3 * frame_count / 60) * 10 + 100
    x_offset = sin(frame_count / 3.7) * 15
    eye(100 + x_offset, y)
    eye(300 - x_offset, y)
    
def eye(x, y):
    w = 100
    no_stroke()  # turn off the stroke
    fill(255) # white
    ellipse(x, y, w, w * 0.6)  # x, y, w, h
    fill(255, 0, 0)  # red
    circle(x, y, w / 2)  # x, y, diameter
    fill(0)  # black
    circle(x, y, w * 0.1)  # pupil
