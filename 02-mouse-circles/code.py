def setup():
    size(500, 500)

def draw():
    v = sin(frame_count/10)
    fill(128 + 128 * v, 0, 128 - 128 * v)
    diameter = sin(frame_count / 60) * 50 + v / 2
    ellipse(mouse_x, mouse_y, diameter, diameter)
