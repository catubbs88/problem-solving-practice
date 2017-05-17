def line(n):
    drawn_line = ('#' * n)
    return drawn_line


#def square(n):
#    drawn_square = ''
#    for i in n:
#        drawn_square = drawn_square + line(n) + "\n"
#    return drawn_square

def square(n):
    drawn_square = rectangle(n, n)
    return drawn_square


def rectangle(width, height):
    drawn_rectangle = ''
    for i in range(1, height+1):
        drawn_rectangle = drawn_rectangle + line(width)
        if i != height:
            drawn_rectangle = drawn_rectangle + "\n"
    return drawn_rectangle


def stairs(n):
    drawn_stairs = ''
    for i in range(1, n+1):
        drawn_stairs = drawn_stairs + line(i)
        if i != n:
            drawn_stairs = drawn_stairs + "\n"
    return drawn_stairs


def space_line(spaces, hashes):
    drawn_space_line = (' ' * spaces) + ('#' * hashes)
    return drawn_space_line


def stairs_reverse(n):
    drawn_stairs_reverse = ''
    for i in range(1, n+1):
        drawn_stairs_reverse = drawn_stairs_reverse + space_line((n-i), i)
        if i != n:
            drawn_stairs_reverse = drawn_stairs_reverse + "\n"
    return drawn_stairs_reverse


def sideways_triangle(n):
    drawn_sideways_triangle = ''
    drawn_sideways_triangle = drawn_sideways_triangle + stairs(n)
    for i in range (n-1, 0, -1):
        drawn_sideways_triangle = drawn_sideways_triangle + "\n" + line(i)
    return drawn_sideways_triangle


def triangle(n):
    drawn_triangle = ''
    for i in range(n):
        drawn_triangle = drawn_triangle + space_line((n- 1 - i), (i * 2 + 1))
        if i != n-1:
            drawn_triangle = drawn_triangle + "\n"
    return drawn_triangle


def diamond(n):
    drawn_diamond = ''
    drawn_diamond = drawn_diamond + triangle(n)
    for i in range(n-1, -1, -1):
        drawn_diamond = drawn_diamond + "\n" + space_line((n- 1 - i), (i * 2 + 1))
    return drawn_diamond