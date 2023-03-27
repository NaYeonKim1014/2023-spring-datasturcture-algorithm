class poly2():
    def __init__(self, coef):
        self.coef_deg = coef        # a variable representing the coefficients and orders of each term of a polynomial
        self.degree = len(coef)     # variables to represent the number of terms in each polynomial

    def print_poly2(self):
        for i in range(self.degree):
            if i == self.degree - 1:                 # the last term's
                if self.coef_deg[i][0] != 0.0:       # if the coefficient is not zero
                    if self.coef_deg[i][0] >= 0:     # determining the sign of a term
                        print(" + ", end='')         # if it's a positive number, use "+"
                    else:
                        print(" - ", end='')         # if it's a negative number, use "-"

                    if self.coef_deg[i][1] == 0:     # if constant, only coefficients are output
                        print("%0.2f" % (abs(self.coef_deg[i][0])))
                    else:                            # if it is not a constant, output it in the form of 'coefficient x^ order'
                        print("%0.2f x^%d" % (abs(self.coef_deg[i][0]), self.coef_deg[i][1]))
                else:
                    print()                          # if the last term is not a constant and the coefficient is 0, nothing is printed
            else:
                if self.coef_deg[i][0] != 0.0:       # if the coefficient is zero, nothing is printed
                    if i == 0:                       # output separately to output the sign in the first term
                        print("%0.2f x^%d" % (self.coef_deg[i][0], self.coef_deg[i][1]), end="")
                    else:
                        if self.coef_deg[i][0] >= 0:
                            print(" + ", end='')
                        else:
                            print(" - ", end='')
                        print("%0.2f x^%d" % (abs(self.coef_deg[i][0]), self.coef_deg[i][1]), end="")

def poly2_add(a,b):
    z = []
    apos = bpos = 0
    term_a = a.degree
    term_b = b.degree

    while(apos < term_a) and (bpos < term_b):
        if a.coef_deg[apos][1] > b.coef_deg[bpos][1]:
            z.append([a.coef_deg[apos][0], a.coef_deg[apos][1]])
            apos += 1
        elif a.coef_deg[apos][1] == b.coef_deg[bpos][1]:
            z.append([a.coef_deg[apos][0] + b.coef_deg[bpos][0], a.coef_deg[apos][1]])
            apos += 1
            bpos += 1
        else:
            z.append([b.coef_deg[bpos][0], b.coef_deg[bpos][1]])
            bpos += 1

        if apos >= term_a:
            while bpos < term_b:
                z.append([b.coef_deg[bpos][0], b.coef_deg[bpos][1]])
                bpos += 1
        elif bpos >= term_b:
            while apos < term_a:
                z.append([a.coef_deg[apos][0], a.coef_deg[apos][1]])
                apos += 1
    return poly2(z)

def poly2_mul(a, b):
    x = []                                                                                           # empty list x declaration to contain final result values
    apos = 0
    for i in range(b.degree):
        x.append([a.coef_deg[apos][0]*b.coef_deg[i][0], a.coef_deg[apos][1] + b.coef_deg[i][1]])     # The coefficients of each term are multiplied, and the order is added.
    x = poly2(x)                                                                                     # Put the result value of the above operation in x
    apos += 1

    while (apos < a.degree):
        y = []                                                                                       # Empty list y declaration to contain intermediate result values
        for i in range(b.degree):
            y.append([a.coef_deg[apos][0]*b.coef_deg[i][0], a.coef_deg[apos][1] + b.coef_deg[i][1]]) # Perform operations in the same manner as above
        y = poly2(y)                                                                                 # Put the result value of the above operation in y

        x = poly2_add(x, y)                                                                          # Put the value added by x and y
        apos += 1
    return x

a = list(map(float, input("Input A(x) : ").split(' ')))
temp = []
for i in range(0, len(a), 2):
    temp.append(a[i:i+2])
a = poly2(temp)

b = list(map(float, input("Input B(x) : ").split(' ')))
temp = []
for i in range(0, len(b), 2):
    temp.append(b[i:i+2])
b = poly2(temp)

c = poly2_add(a, b)
d = poly2_mul(a, b)

print('A(x) is ', end='')
a.print_poly2()
print('B(x) if ', end='')
b.print_poly2()
print('A(x) + B(x) is ', end='')
c.print_poly2()
print('A(x) * B(X) is ', end='')
d.print_poly2()



