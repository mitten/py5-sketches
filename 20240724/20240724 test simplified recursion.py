# Recursion is on line 41
# Be sure to put things like no_stroke and rect_mode INSIDE the draw method
# See file 20240720 underlying nonrecursion to see the small square technique in more detail

thisfile = (Path(__file__).stem).replace(" ","-") # current file name
seed = 1  # random seed
margin = 180
gw = 400
gh = 400

def setup():
    size(gw + 2 * margin, gh + 2 * margin) # width, height
    
def draw():
    global seed, margin, gw, gh
    random_seed(seed)
    background(50, 80, 100)
    for _ in range(6): # draw the grid multiple times in the same place
        grid(margin, margin, 4, 4, gw)

def grid(off_x, off_y, cols, rows, gs):
    stroke(255, 64) # white stroke with lowered opacity (0-255 range)
    w = gs / cols # grid size (width) divided by number of columns: cell width/height
    for j  in range(rows):
        y = off_y + (j * w) + (w / 2) # sets cell starting point: off_y is the left margin, j moves it down to next row, half w places it in center of cell
        r = random_int(64, 192) # color settings
        g = random_int(128, 160)
        b = random_int(64, 192)
        for i in range(cols):
            x = off_x + (i * w) + w / 2 # sets cell starting point: off_x is the top margin, i moves it across the row, half w places it in center of cell
            m = random_int(1, 7) # random choice of grid fill style
            if m < 4 : # style 1: small square, upper left or lower right quadrant
                fill(r, g, b, 64)
                dr = random_int(0, 1) * w / 2 # 0 = lower right, 1 = upper left
                rect(x - dr, y - dr, w / 2, w / 2)
                if m <= 1 :
                    circle(x, y, random_int(1, 6) * w / 3)
            elif m == 6:
                fill(200, 5)
                rect(x - w, y - w, w * 2, w * 2)
            #else:
            if random_int(1, 6) == 3 and w > 30: # the greater-than is critical to keep it from infiniting
                grid(x - w / 2, y - w / 2, 2, 2, w)
                                
def mouse_pressed():
    global seed
    seed = seed + 1
    print(f'random seed: {seed}')
    
def key_pressed():
    if key == 's':
        save_frame(f'{thisfile}-seed-{seed}.png')
        print('saved png')
    

