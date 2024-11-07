from math import *
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'SimSun'
plt.rcParams['axes.unicode_minus'] = False

class drawAb:
    def __init__(self) -> None:
        pass
        self.fig, self.ax = plt.subplots() 



    def solve80(self, n, varepsilon, theta, r, r1, l, ee):
        return 2*n*((sin(varepsilon*pi/n))/sin(theta/2) + 
                    (1-varepsilon)*(pi/n)+
                    ((ee + r)/l) *(0.5*pi + pi/n - theta/2 + tan(0.5*pi+theta/2))
                    ) * l * 0.001

    def solve84(self, n, varepsilon, theta, r, r1, l, ee):
        return 2*n*((sin(varepsilon*pi/n))/sin(theta/2) + 
                    (1-varepsilon)*(pi/n)+
                    (r+r1)/l *(0.5*pi + pi/n - theta/2 + tan(0.5*pi+theta/2))
                    - (r1 - ee) / l * (pi/n)) * l * 0.001

    def solve86(self, n, varepsilon, theta, r, r1, l, ee):
        return 2*n*((1-varepsilon)*pi/n +
                    ((ee + r)/l)*(pi/n + asin(
                        sin(varepsilon*pi/n)/((ee + r)/l)
                    ))) * l * 0.001


    def drawallpiv(self, number, n, varepsilon, theta, r, r1, l, ystar, L):
        t = 0
        elist = []
        solvelist = []
        while 1:
            
            ee = t * 8
            
            if ee <=  8:
                solvelist.append(self.solve84(n, varepsilon, theta, r, r1, l, ee) * L)
                t = t + 0.125
                elist.append(ee)
            elif ee <= (ystar * l- r):
                solvelist.append(self.solve80(n, varepsilon, theta, r, r1, l, ee) * L)
                t = t + 0.125
                
                elist.append(ee)
            elif ee <= 53.56:
                solvelist.append(self.solve86(n, varepsilon, theta, r, r1, l, ee) * L)
                t = t + 0.125

                elist.append(ee)        
            else:
                break
        # print(ee)
        # plt.plot(ee, solvelist)
        # ax.scatter(elist, solvelist)
        self.ax.plot(elist, solvelist, label = str(number))

    def picshow(self, xmin = None, xmax = None, ymin = None, ymax = None):
        self.ax.legend( fontsize=14)
        if xmin != None or ymin != None or xmax != None or ymax != None:
            self.ax.set_xlim(xmin, xmax)
            self.ax.set_ylim(ymin, ymax)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.ylabel('Ab', fontsize=14)
        plt.xlabel('e', fontsize=14)
        plt.show()

    def picshow(self, name, xmin = None, xmax = None, ymin = None, ymax = None):
        self.ax.legend( fontsize=14)
        if xmin != None or ymin != None or xmax != None or ymax != None:
            self.ax.set_xlim(xmin, xmax)
            self.ax.set_ylim(ymin, ymax)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.ylabel('Ab', fontsize=14)
        plt.xlabel('e', fontsize=14)
        plt.savefig(name)
# plt.savefig("燃面变化规律图.pdf")
    # for i in elist:
        # print(i)


