from fractions import Fraction

# return the y intercept given y intercept form
def get_y_intercept(m, x, b):
    return m*x+b

# takes a slope-intercept form as first 3 params
def slope_solve_b(m, pair: tuple):
    return ((m*pair[0])*-1)+pair[1]

# takes point-intercept form and returns y-intercept form
def point_form_to_y_form(my, mx, mb):
    mx *= -1
    m = Fraction(mx, my)
    mb /= my
    return (m, mb)