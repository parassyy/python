def draw_line(ch):
    def draw(size):
        print(ch*size)
    return draw

draw_star=draw_line("*")
draw_star(20)
