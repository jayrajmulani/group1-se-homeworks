def the():
    return True  
      
def sym(Self , entropy, mode,sym=None):
        sym=Sym()
        for i,x in("a","a","a","a","b","b","c"):
            sym.add(Self,x)
            mode,entropy=sym.mid(Self),sym.div(Self)
            entropy=(1000*entropy)//1/1000
            
            return mode=="a" and 1.37 <= entropy and entropy <=1.38
    
def enum(Self,mid,div,num=None):
    num=Num()
    for i in range(1,101):
        num.add(i)
    mid,div=num.mid(Self), num.div(Self)
    print(mid,div)
    return 50 <=mid and mid<=52 and 30.5< div and div<32

def bignum(Self , num=None):
    num=Num()
    the.nums = 32
    for i in range(1,1001):
        num.add(i)
    mid,div =num.mid(Self),num.div(Self)
    return 50<= mid and mid <=52 and 30.5 < div and div<32
