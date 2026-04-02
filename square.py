import turtle

def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

if __name__ == '__main__':
    draw_square(100)