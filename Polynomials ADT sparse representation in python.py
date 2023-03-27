class poly2():
    def __init__(self, coef):
        self.coef_deg = coef        # 다항식의 각 항의 계수와 차수를 나타내는 변수
        self.degree = len(coef)     # 각 다항식의 항의 개수를 나타낼 변수

    def print_poly2(self):
        for i in range(self.degree):
            if i == self.degree - 1:                 # 맨 마지막 항의
                if self.coef_deg[i][0] != 0.0:       # 계수가 0이 아닐 경우
                    if self.coef_deg[i][0] >= 0:     # 항의 부호 판별
                        print(" + ", end='')         # 양수일 경우엔 '+'를
                    else:
                        print(" - ", end='')         # 음수일 경우엔 '-'를

                    if self.coef_deg[i][1] == 0:     # 상수일 경우엔 계수만 출력한다
                        print("%0.2f" % (abs(self.coef_deg[i][0])))
                    else:                            # 상수가 아닐 경우엔 "계수 x^차수"형태로 출력한다.
                        print("%0.2f x^%d" % (abs(self.coef_deg[i][0]), self.coef_deg[i][1]))
                else:
                    print()                          # 맨 마지막 항이 상수가 아니고 계수가 0일 경우엔 아무것도 출력하지 않는다
            else:
                if self.coef_deg[i][0] != 0.0:       # 계수가 0일경우 아무것도 출력하지 않는다
                    if i == 0:                       # 첫 항의 부호를 출력하기 위해 따로 출력
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
    x = []                                                                                           # 최종 결과 값을 담아 줄 빈 리스트 x 선언
    apos = 0
    for i in range(b.degree):
        x.append([a.coef_deg[apos][0]*b.coef_deg[i][0], a.coef_deg[apos][1] + b.coef_deg[i][1]])     # 각 항의 계수끼리는 곱하고, 차수끼리는 더해준다.
    x = poly2(x)                                                                                     # 위 연산의 결과 값을 x에 담아준다
    apos += 1

    while (apos < a.degree):
        y = []                                                                                       # 중간 결과 값을 담아 줄 빈 리스트 y 선언
        for i in range(b.degree):
            y.append([a.coef_deg[apos][0]*b.coef_deg[i][0], a.coef_deg[apos][1] + b.coef_deg[i][1]]) # 위와 같은 방식의 연산 수행
        y = poly2(y)                                                                                 # 위 연산의 결과 값을 y에 담아준다

        x = poly2_add(x, y)                                                                          # x와 y를 더해준 값을 x에 담아준다
        apos += 1
    return x

a = list(map(float, input("수식 A(x)를 입력하세요 : ").split(' ')))
temp = []
for i in range(0, len(a), 2):
    temp.append(a[i:i+2])
a = poly2(temp)

b = list(map(float, input("수식 B(x)를 입력하세요 : ").split(' ')))
temp = []
for i in range(0, len(b), 2):
    temp.append(b[i:i+2])
b = poly2(temp)

c = poly2_add(a, b)
d = poly2_mul(a, b)

print('수식 A(x)은 ', end='')
a.print_poly2()
print('수식 B(x)는 ', end='')
b.print_poly2()
print('수식 A(x) + B(x)는 ', end='')
c.print_poly2()
print('수식 A(x) * B(X)는 ', end='')
d.print_poly2()



