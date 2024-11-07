import math
from scipy.optimize import fsolve
from base import Base

halfThetabaDeg = [24.55, 28.22, 31.13, 33.53, 35.56, 37.31]
halfThetabaRad = [i/180 * math.pi for i in halfThetabaDeg]

class Select(Base):
    """
    药柱筛选
    Id 计算装药量时I的偏差值系数，取值1.01~1.05
    D 外径(mm)
    I 总冲(kNs)
    Fbar 平均推力(kN)
    Isp 理论比冲(s)
    k 燃气绝热指数
    pc 工作压力(Mpa)
    rco 过度圆弧半径系数
    rhop 推进剂密度(g/cm3)
    rran 燃速
    n 压力指数
    r1 星角圆弧半径(mm试取)
    pa = 101325
    g = 9.8
    stand1/2/3/4 筛选标准
    """
    def __init__(self, Id : float, D : float, I : float, Fbar : float, Isp : float, 
                 k : float, pc : float, rco : float, rhop : float, rran :float, n :float, r1, 
                 nstar : int, stand1:float, stand2:float, stand3:tuple, stand4:float,
                 pa : float = 101325, g : float = 9.8) -> None:
        Base.__init__(self, Id, D, I, Fbar, Isp, k, pc, rco, rhop, rran, n, r1, pa, g)
        self.nstar = nstar
        self.stand1 = stand1
        self.stand2 = stand2
        self.stand3 = stand3
        self.stand4 = stand4
        self.resultlist1 = {}
        self.resultlist2 = {}
        self.resultlist3 = {}
        self.resultlist4 = {}
        self.resultlist5 = {}
        self.Aflist = {}
        self.Aplist = {}
        # self.varepsilon = varepsilon

    def method1(self, varepsilon):
        self.pi_nstar = math.pi / self.nstar
        frac_s_l_min = 2*self.nstar*((math.sin(varepsilon * self.pi_nstar))/math.sin(halfThetabaRad[self.nstar - 3]) + (1-varepsilon)*self.pi_nstar)
        frac_s_l_1 = 2*math.pi*(1+self.y1())
        return frac_s_l_1 / frac_s_l_min

    def slove1(self):
        for varepsilon in range(3, 9):
            varepsilon = varepsilon / 10
            self.resultlist1[varepsilon] = self.method1(varepsilon)
        return self.resultlist1

    def method2(self, varepsilon):
        return math.sin(varepsilon * math.pi / self.nstar) / self.y1()

    def slove2(self):
        self.slove1()
        passdic1 = {}
        for k, v in self.resultlist1.items():
            if v <= self.stand1:
                passdic1[k] = self.resultlist1[k]
        for k, v in passdic1.items():
            self.resultlist2[k] = self.method2(k)
        return self.resultlist2
    
    def halftheta(self):
        self.halfthetadic = {}
        self.slove2()
        xi1dic = {}
        for k, v in self.resultlist1.items():
            xi1dic[k] = 1/v 
        for k, v in xi1dic.items():
            frac_s_l_min = 2*self.nstar*((math.sin(k * self.pi_nstar)) \
                                         /math.sin(halfThetabaRad[self.nstar - 3]) + (1-k)*self.pi_nstar)
            frac_s_l_max = frac_s_l_min / v
            def eqslove(i):
                halftheta = i[0]
                return [2 *self.nstar*(
                    math.sin(k*self.pi_nstar)/math.sin(halftheta) +
                    (1-k)*self.pi_nstar+
                    (self.r + self.r1)/self.l *(0.5*math.pi + self.pi_nstar - halftheta + math.tan(math.pi*0.5+halftheta)))-
                    frac_s_l_max
                ]
            halftheta = fsolve(eqslove, [0.1])
            self.halfthetadic[k] = halftheta[0]


    def method3(self, varepsilon):
        std1 = (1-varepsilon)*self.pi_nstar +math.sin(varepsilon*self.pi_nstar)*  \
        (math.cos(varepsilon*self.pi_nstar) - math.sin(varepsilon*self.pi_nstar) * (-1)*math.tan(math.pi*0.5+self.halfthetadic[varepsilon]))
        std2 = math.sin(varepsilon*self.pi_nstar)/math.sin(self.halfthetadic[varepsilon]) + \
        (1 - varepsilon)*self.pi_nstar
        std3 = 0.5*math.pi + self.pi_nstar - self.halfthetadic[varepsilon] + math.tan(math.pi*0.5+self.halfthetadic[varepsilon])
        std4 = (((self.r1)/self.l)**2)*(self.halfthetadic[varepsilon]-math.tan(math.pi*0.5+self.halfthetadic[varepsilon])-0.5*math.pi)

        Ap = (self.nstar * std1 + 2*self.nstar*self.y0*std2 + self.nstar * self.y0**2 *std3 +self.nstar*std4) * (self.l**2)

        Ac = math.pi * self.D**2 / 4

        return (Ac - Ap) / Ac, Ap
        
    def slove3(self):
        self.halftheta()
        passdic2 = {}
        for k, v in self.resultlist2.items():
            if v <= self.stand2:
                passdic2[k] = self.resultlist2[k]
        for k, v in passdic2.items():
            self.resultlist3[k], self.Aplist[k] = self.method3(k)
        return self.resultlist3
        
    def method4(self, varepsilon):
        Af = (varepsilon * math.pi * (1+self.y1())**2 - \
        self.nstar*(math.sin(varepsilon*self.pi_nstar)*(math.sqrt(self.y1()**2 - (math.sin(varepsilon*self.pi_nstar))**2)+\
                    math.cos(varepsilon*self.pi_nstar))) - \
            self.nstar*self.y1()**2*(varepsilon*self.pi_nstar + math.asin((math.sin(varepsilon*self.pi_nstar))/self.y1()))\
        ) * self.l**2
        Ac = math.pi * self.D**2 / 4
        return Af/Ac * 100, Af
    
    def slove4(self):
        self.slove3()
        passdic3 = {}
        for k, v in self.resultlist3.items():
            if v >= self.stand3[0] and v <= self.stand3[1] :
                passdic3[k] = self.resultlist3[k]
        for k, v in passdic3.items():
            self.resultlist4[k], self.Aflist[k] = self.method4(k)

        return self.resultlist4, self.Aflist
    
    def method5(self, ap, af):
        Ac = math.pi * self.D**2 / 4
        return (self.mpeff() /self.rhop) / (Ac - ap - af)
    
    def slove5(self):
        self.slove4()
        passdic4 = {}
        for k, v in self.resultlist4.items():
            if v <= self.stand4:
                passdic4[k] = self.resultlist4[k]
        for k, v in passdic4.items():
            self.resultlist5[k] = self.method5(self.Aplist[k], self.Aflist[k])

        print('af', self.Aflist, 'ap', self.Aplist)
        for k, v in self.halfthetadic.items():
            print(k, v / math.pi * 180)
        # print(self.halfthetadic)

        return self.resultlist5

        
        

# x = Select(1.03, 265, 260, 40, 263, 1.19, 6.9, 0.015, 1.77, 8, 0.33, 8, 8, 1.2, 1, (0.75, 0.85), 5)
# print(x.slove5())
# print(x.halfthetadic)

