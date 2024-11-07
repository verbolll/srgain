import math

class Base:
    """
    计算基础数据
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
    """
    def __init__(self, Id : float, D : float, I : float, Fbar : float, Isp : float, 
                 k : float, pc : float, rco : float, rhop : float, rran :float, n :float, r1, 
                 pa : float = 101325, g : float = 9.8) -> None:
        self.Id = Id
        self.D = D
        self.I = I * 1000 # 输入为KN
        self.Fbar = Fbar * 1000 # KN
        self.Isp = Isp
        self.k = k
        self.g = g
        self.pa = pa
        self.pc = pc * 10**6 # Mpa
        self.rco = rco
        self.rhop = rhop * 1000
        self.rran = rran * 0.001 # mm
        self.n = n
        self.r1 = r1

    def mpeff(self):
        return self.Id * self.I /(self.g * self.Isp) 
    
    def bGamma(self):
        exp = (self.k+1) / (2*(self.k-1))
        underbase = self.k ** 0.5
        return underbase * (2/(self.k+1))**exp

    def cf(self):
        return self.bGamma() * math.sqrt(((2*self.k) / (self.k - 1)) * (1 - (self.pa/self.pc)**((self.k-1)/self.k)))
    
    def at(self):
        return self.Fbar / (self.cf() * self.pc)
    
    def cstar(self):
        return self.Isp * self.g / self.cf()
    
    def knbar(self):
        a20 = self.rran / self.pc**self.n
        return self.pc**(1-self.n) / (self.cstar()*self.rhop*a20)
        
    def sbar(self):
        return self.knbar() * self.at()
    
    def e1(self):
        return self.mpeff() / (self.rhop * self.sbar())
    
    def y1(self):
        """
        此处单位是毫米
        """
        self.r = self.rco * self.D
        self.l = self.D / 2 - self.e1()*1000 - self.r
        self.y0 = self.r / self.l
        return (self.e1()*1000 + self.r ) / self.l
    

# print(Base.__doc__)
    
# x = Base(1.03, 255, 260, 40, 263, 1.19, 6.9, 0.015, 1.77, 8, 0.33)
# print(x.y1())