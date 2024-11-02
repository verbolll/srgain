from math import *
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = 'SimSun'
plt.rcParams['axes.unicode_minus'] = False
# s/l0  
def solve(n, varepsilon, theta, r, r1, l):
    return 2*n*((sin(varepsilon*pi/n))/sin(theta/2) + 
                (1-varepsilon)*(pi/n)+
                (r+r1)/l *(0.5*pi + pi/n - theta/2 + tan(0.5*pi+theta/2))
                - pi*r1/(n*l)) * l
# print(solve(7, 0.8, 2*((23.523/180)*pi), 5.4, 10, 73.66))
# print(solve(8, 0.8, 2*((26.225/180)*pi), 3.975, 8, 74.965))

# s/l*
def solve1(n, varepsilon, theta, r, r1, l):
    return 2*n*((sin(varepsilon*pi/n))/sin(theta/2) + 
                (1-varepsilon)*(pi/n)+
                (r+r1)/l *(0.5*pi + pi/n - theta/2 + tan(0.5*pi+theta/2))
                ) * l
# print(solve1(7, 0.8, 2*((23.523/180)*pi), 5.4, 10, 73.66))
# print(solve1(7, 0.8, 2*((27.276/180)*pi), 3.975, 8, 74.965))

def y(n, varepsilon, theta):
    return sin(varepsilon*pi/n) / cos(theta)
# # print(y(3, 0.4, 0.428478))
# print(y(3, 0.4, 0.428478))
# print(y(4, 0.5, 0.492532))
# print(y(5, 0.6, 0.543321))
# print(y(6, 0.7, 0.585209))
# print(y(7, 0.7, 0.620639))
# print(y(7, 0.8, 0.620639))
# print(y(8, 0.8, 0.457712))

def m(a, l, rho, mpeff):
    return a*0.01*l*rho*100 + mpeff

# print(m(1.5549032, 1.369833, 1.77, 106.0058))
# print(m(1.628, 1.408, 1.77, 103.903))
# print(m(1.408, 1.410, 1.77, 103.903))
# print(m(1.990, 1.410, 1.77, 103.903))
# print(m(2.197, 1.408, 1.77, 103.903))
# print(m(1.625, 1.432, 1.77, 103.903))
# print(m(2.412, 1.405, 1.77, 103.903))
# print(m(1.857, 1.426, 1.77, 103.903))


def solve80(n, varepsilon, theta, r, r1, l, ee):
    return 2*n*((sin(varepsilon*pi/n))/sin(theta/2) + 
                (1-varepsilon)*(pi/n)+
                ((ee + r)/l) *(0.5*pi + pi/n - theta/2 + tan(0.5*pi+theta/2))
                ) * l * 0.001

def solve84(n, varepsilon, theta, r, r1, l, ee):
    return 2*n*((sin(varepsilon*pi/n))/sin(theta/2) + 
                (1-varepsilon)*(pi/n)+
                (r+r1)/l *(0.5*pi + pi/n - theta/2 + tan(0.5*pi+theta/2))
                - (r1 - ee) / l * (pi/n)) * l * 0.001

def solve86(n, varepsilon, theta, r, r1, l, ee):
    return 2*n*((1-varepsilon)*pi/n +
                ((ee + r)/l)*(pi/n + asin(
                    sin(varepsilon*pi/n)/((ee + r)/l)
                ))) * l * 0.001

fig, ax = plt.subplots() 

def drawallpiv(nn, n, varepsilon, theta, r, r1, l, ystar, L):
    t = 0
    elist = []
    solvelist = []
    while 1:
        
        ee = t * 8
        
        if ee <=  8:
            solvelist.append(solve84(n, varepsilon, theta, r, r1, l, ee) * L)
            t = t + 0.125
            elist.append(ee)
        elif ee <= (ystar * l- r):
            solvelist.append(solve80(n, varepsilon, theta, r, r1, l, ee) * L)
            t = t + 0.125
            
            elist.append(ee)
        elif ee <= 53.56:
            solvelist.append(solve86(n, varepsilon, theta, r, r1, l, ee) * L)
            t = t + 0.125

            elist.append(ee)        
        else:
            break
    # print(ee)
    # plt.plot(ee, solvelist)
    # ax.scatter(elist, solvelist)
    ax.plot(elist, solvelist, label = str(nn), )
drawallpiv(1, 3, 0.4, 17.347*2/180 *pi, 3.975, 8, 74.965, 0.426, 1.408)
drawallpiv(2, 4, 0.5, 20.159*2/180 *pi, 3.975, 8, 74.965, 0.408, 1.410)
drawallpiv(3, 5, 0.6, 22.735*2/180 *pi, 3.975, 8, 74.965, 0.399, 1.410)
drawallpiv(4, 6, 0.7, 25.1*2/180 *pi, 3.975, 8, 74.965, 0.396, 1.408)
drawallpiv(5, 7, 0.7, 23.877*2/180 *pi, 3.975, 8, 74.965, 0.338, 1.432)
drawallpiv(6, 7, 0.8, 27.276*2/180 *pi, 3.975, 8, 74.965, 0.395, 1.405)
drawallpiv(7, 8, 0.8, 26.225*2/180 *pi, 3.975, 8, 74.965, 0.344, 1.426)
ax.legend( fontsize=14)
ax.set_xlim(-5, 55)
ax.set_ylim(0, 1.5)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylabel('Ab', fontsize=14)
plt.xlabel('e', fontsize=14)
# plt.show()
plt.savefig("燃面变化规律图.pdf")
    # for i in elist:
        # print(i)


