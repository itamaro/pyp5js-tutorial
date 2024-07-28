def setup():
    size(500, 500)
    rect_mode(CENTER)
    frame_rate(5)

def draw():
    random_seed(500)
    background(0)
    no_fill()
    
    number_rc = 11
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
                if (11*j+7*i+int((13+i**2+j)*sin(2*frame_count)*cos(frame_count/2))) % 2 == 0:
                    square(x + xo, y + yo, side)
                else:
                    circle(x + xo, y + yo, side)
