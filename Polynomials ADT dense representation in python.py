class poly1():
    def __init__(self, coef):
        self.coef = coef
        self.degree = len(coef)

    def print_poly1(self):
        for i in range(self.degree):
            if i == self.degree - 1:                        # Determine if it is a constant term
                if self.coef[i] != 0.0:
                    if self.coef[i] >= 0:                   # Determine the sign of a constant term
                        print(" + ", end='')
                    else:
                        print(" - ", end='')
                    print("%0.2f" % (abs(self.coef[i])))
                else:                                       # line-up without output if constant term is 0
                    print()
            else:
                if self.coef[i] != 0.0:
                    if i == 0:
                        print("%0.2f x^%d" % (self.coef[i], self.degree - i - 1), end='')
                    else:
                        if self.coef[i] >= 0:
                            print(" + ", end='')
                        else:
                            print(" - ", end='')
                        print("%0.2f x^%d" % (abs(self.coef[i]), self.degree - i - 1), end='')


def poly1_add(a,b):
    z = []                  # list to contain the result of two polynomial additions
    apos = bpos = 0         # current positions of two polynomials
    degree_a = a.degree     # polynomial a's degree (ex. degree2, degree3 ...)
    degree_b = b.degree     # polynomial b's degree 

    while (apos < degree_a) or (bpos < degree_b):
        if degree_a > degree_b:
            z.append(a.coef[apos])
            apos += 1
            degree_a -= 1
        elif degree_a == degree_b:              # if the two polynomials have the same order of the currently located terms
            z.append(a.coef[apos]+b.coef[bpos]) # add the coefficients of the two terms
            apos += 1
            bpos += 1
        else:
            z.append(b.coef[bpos])
            bpos += 1
            degree_b -= 1
    return poly1(z)

def poly1_mul(a, b):
    x = []                  # the highest order term of a * the whole polynomial of b
    degree_a = a.degree
    degree_b = b.degree

    apos = 0
    for i in range(degree_b):
        x.append(a.coef[apos] * b.coef[i])
    for i in range(degree_a - 1):
        x.append(0)

    x = poly1(x)
    degree_a -= 1
    apos += 1

    while(apos < a.degree):
        y = []              # the term below the highest order term of a * the whole polynomial of b
        for i in range(degree_b):
            y.append(a.coef[apos] * b.coef[i])
        for i in range(degree_a - 1):
            y.append(0)
        y = poly1(y)

        x = poly1_add(x, y) # a + b
        apos += 1
        degree_a -= 1
    return x

a = list(map(float, input("Insert A(X) : ").split(' ')))
b = list(map(float, input("Insert B(X) : ").split(' ')))

a = poly1(a)
b = poly1(b)
c = poly1_add(a, b)
d = poly1_mul(a, b)

print('A(X) is ', end='')
a.print_poly1()
print('B(X) is ', end='')
b.print_poly1()
print('A(X) + B(X) is ', end='')
c.print_poly1()
print('A(X) * B(X) is ', end='')
d.print_poly1()

