# Sketch from Grid Template file
# The grid itself is based on Villares' code from the Domestika course, edited
# 20240720

thisfile = (Path(__file__).stem).replace(" ","-") # current file name
seed = 4  # random seed
margin = 180 
gw = 600 # grid width
gh = 900 # grid height
gc = 4 # grid columns
gr = 6 # grid rows

def setup():
    size(gw + 2 * margin, gh + 2 * margin) # width, height
    
def draw():
    global seed, margin, gw, gh
    random_seed(seed)
    background(80, 80, 120) # RGB
    #grid(margin, margin, gc, gr, gw) # use this instead of code below to draw once
    for _ in range(6): # draw the grid multiple times in the same place
        grid(margin, margin, gc, gr, gw)

def grid(off_x, off_y, cols, rows, gs):
    w = gs / cols # grid width divided by number of columns => cell width AND height
    halfw = w / 2 # heavily used, so why not have a variable for readability
    for j  in range(rows):
        stroke(255, 16) # white stroke with lowered opacity (0-255 range)
        y = off_y + (j * w) + halfw # sets cell starting point: off_y is the left margin, j moves it down to next row, half w places it in center of cell
        r = random_int(0, 128) # color settings (0-255 range)
        g = random_int(64, 192)
        b = random_int(0, 255)
        for i in range(cols):
            x = off_x + (i * w) + halfw # sets cell starting point: off_x is the top margin, i moves it across the row, half w places it in center of cell
            m = random_int(1, 6) # random choice of grid fill style
            if m < 4: # style 1: small square, upper left or lower right quadrant
                dr = random_int(0, 1) * halfw # 0 = lower right, 1 = upper left
                fill(r, g, b, 32)
                rect(x - dr, y - dr, halfw, halfw) 
            elif 4 <= m < 6: # style 2: full cell square
                fill(r, g, b, 32)
                rect(x - halfw, y - halfw, w, w) # move draw point to upper left corner
            else: # style 3: random diameter circle
                fill(r, g, b, 64)
                stroke(255, random_int(96,128))
                circle(x, y, random_int(1, 6) * w / 3)
                
def mouse_pressed():
    global seed
    seed = seed + 1
    print(f'random seed: {seed}')
    
def key_pressed():
    if key == 's':
        save_frame(f'{thisfile}-seed-{seed}.png')
        print('saved png')
    

