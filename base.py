import math

class Base:
    """
    ran  燃速
    rco 系数
    """
    def __init__(self, Id : float, D : float, I : float, Fbar : float, Isp : float, 
                 k : float, pc : float, rco : float, rhop : float, rran :float, n :float, 
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
        r = self.rco * self.D
        l = self.D / 2 - self.e1()*1000 - r
        # y0 = r / l
        return (self.e1()*1000 + r ) / l

    
x = Base(1.03, 255, 260, 40, 263, 1.19, 6.9, 0.015, 1.77, 8, 0.33)
print(x.y1())