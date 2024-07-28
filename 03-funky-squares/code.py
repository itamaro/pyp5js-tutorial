def setup():
    size(500, 500)
    rect_mode(CENTER)
    frame_rate(5)

def draw():
    random_seed(500 * mouse_x + mouse_y)
    background(0)
    no_fill()
    
    number_rc = 5
    w = width / number_rc
    for j in range(number_rc):
        y = j * w  + w / 2
        for i in range(number_rc):
            x = i * w + w / 2
            for _ in range(10):
                xo = random(-2, 2)
                yo = random(-2, 2)
                side = random(10, w)
                stroke(random(255), 128, 255)
                square(x + xo, y + yo, side)
