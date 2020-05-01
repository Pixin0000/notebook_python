class Der:
    def __init__(self,x ):
        self.x = x
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
            print("原本為"+str(con)+"e^"+ str(xcon) + "x^"+str(xpow)+","+"後來為"+str(cons)+"e^"+ str(xcon)+ "x^"+str(xpow))
a = Der("x")
#a.dx(3,"x+1",-2,2)
a.dex(3,2)
a.ex(2 , 2 , 2)