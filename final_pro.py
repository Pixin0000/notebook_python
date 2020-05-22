import sympy as sym
class Der:
    def dex(self,xpow,time):
        con = 1
        for i in range(time):
            con *= xpow
        x = str(con) + "x^" + str(xpow) 
        return x
    def dx(self,con,x,xpow,pow):
        x_list = list(x)
        x_list.insert(1,"^")
        x_list.insert(2,xpow)
        x = "".join([str(i) for i in x_list])
        time = int(input("幾次微分？"))
        cons = con
        pows = pow
        if(pows >= 1):
            while(time <= pows and time != 0):
                    cons = cons * pows * xpow
                    pows -= 1
                    time -= 1
        elif(pows < 1 ):
            for i in range(time):
                cons = cons * pows * xpow
                pows -= 1
        if(time > pow and pow > 1):
            self.add = print("0")
        else:
            self.add = print("原本為"+ str(con)+"("+str(x)+")"+"^"+str(pow)+","+"微分後為"+str(cons)+"("+str(x)+")"+"^"+str(pows))
    def ex(self,con,xcon,xpow):
            time = int(input("微分幾次"))
            cons = con
            for i in range(time):
                cons *= xpow * xcon
            print("原本為"+str(con)+"e^"+ "(" + str(xcon) + "x^"+str(xpow)+ ")"+","+"後來為"+str(cons)+"x^"+str(time)+"e^"+ "(" + str(xcon)+ "x^" +str(xpow) + ")")
    def inte(self,xcon,sym,xpow,low,max):
        x1 = (xcon/(xpow+1))*max**(xpow+1)
        x2 = (xcon/(xpow+1))*low**(xpow+1)
        x = x1 - x2
        print("原本為"+str(xcon)+str(sym)+"^"+str(xpow)+"後來為"+str(xcon/(xpow+1))+str(sym)+"^"+str(xpow+1)+"="+str(x))
a = Der()
e = 0
for i in range(0,10):
    for j in range(0,10,-1):
        x = 1
        e += (x**i) / j
        print(j)
        if(j==0):
            i += 1
print(e)
x = sym.symbols('x')
#a.dx(3,"x-12",2,2)
#a.ex(2 , 2 , 2)
a.inte(10,x,2,1,10)
#print(sym.diff(((x-12)/2)**4,x,2)