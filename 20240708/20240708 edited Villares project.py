# This is from Alexandre Villares course on Domestika, Unit 3, with a few edits from me.
s = 1  # random seed

def setup():
    size(700, 900)
    
def draw():
    random_seed(s)
    background(45, 15, 100)
    for _ in range(3):
        grid(100, 6, 8)


def grid(off_x, cols, rows):
    stroke(255)
    w = (width - 2 * off_x) / cols
    off_y = (height - w * rows) / 2  # margin v
    for j  in range(rows):
        y = off_y + j * w + w / 2
        r = random_int(0, 128)
        g = random_int(68, 180)
        b = random_int(0, 255)
        a = random_int(30, 94)
        for i in range(cols):
            x = off_x + i * w + w / 2
            m = random_int(1, 6)
            if 1 <= m < 4:
                fill(180, 255, 220, a)
                dr = random_int(0, 1) * w / 2
                rect(x - dr, y - dr, w / 2, w / 2)
            elif 4 <= m < 6:
                fill(220, 180, 255, a)
                rect(x - w / 2, y - w / 2, w, w)
            else:
                fill(r, g, b, a)
                circle(x, y, random_int(1, 8s) * w / 4)
                
    
def mouse_pressed():
    global s
    s = s + 1
    print(f'random seed: {s}')
    
def key_pressed():
    if key == 's':
        save_frame(f'output-{s}.png')
        print('saved png')
    
    
