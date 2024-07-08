
s = 1  # random seed

def setup():
    size(700, 980)
    
def draw():
    random_seed(s)
    background(0, 0, 100)
    for _ in range(3):
        grid(100, 6, 8)


def grid(off_x, cols, rows):
    stroke(255)
    w = (width - 2 * off_x) / cols
    off_y = (height - w * rows) / 2  # margin v
    for j  in range(rows):
        y = off_y + j * w + w / 2
        r = random_int(0, 128)
        g = random_int(128, 255)
        b = random_int(0, 255)
        for i in range(cols):
            x = off_x + i * w + w / 2
            m = random_int(1, 6)
            if m == 1:
                fill(r, g, b, 128)
                ra = random(w / 20, w / 2)
                rb = random(1, w / 2)
                np = random_int(4, 10)
                star(x, y, ra, rb, np)
            elif 1 < m < 4:
                fill(255, 64)
                dr = random_int(0, 1) * w / 2
                rect(x - dr, y - dr, w / 2, w / 2)
            elif 4 <= m < 6:
                fill(200, 64)
                rect(x - w / 2, y - w / 2, w, w)
            else:
                fill(r, g, b, 64)
                circle(x, y, random_int(1, 2) * w / 4)
                

def star(cx, cy, ra, rb, np, start_ang=0):  # estrela
    step = TWO_PI / np  # passo
    begin_shape()
    for i in range(np):  # for each tip/point
        ang = start_ang + step * i # angle
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex(ax, ay)
        bx = cx + cos(ang + step / 2.0) * rb
        by = cy + sin(ang + step / 2.0) * rb
        vertex(bx, by)
    end_shape(CLOSE)
    
def mouse_pressed():
    global s
    s = s + 1
    print(f'random seed: {s}')
    
def key_pressed():
    if key == 's':
        save_frame(f'output-{s}.png')
        print('saved png')
    
    
