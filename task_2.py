import turtle

def draw_tree(branch_length, level, angle=20):
    if level == 0:
        return

    turtle.forward(branch_length)
    turtle.left(angle)

    draw_tree(branch_length * 0.8, level - 1, angle)

    turtle.right(angle * 2)

    draw_tree(branch_length * 0.8, level - 1, angle)

    turtle.left(angle)
    turtle.backward(branch_length)

def initialize_turtle():
    turtle.up()
    turtle.left(90)
    turtle.backward(300)
    turtle.down()
    turtle.speed('fastest')

def pythagoras_tree(level):
    initialize_turtle()
    draw_tree(100, level)
    turtle.done()

# Test
pythagoras_tree(8)