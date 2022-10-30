
class Soution:
    
    def fun(self, str: str) -> int:
        str = str.strip()
        
        if not str:
            return 0
        #set intial vaue to false
        negative = False
        out = 0
        
        if str[0] == "-":
            negative= True
        if str[0] =="+":
            negative = False
        elif not str[0].isnumeric:
            return 0
        else:
            out = ord(str[0]) - ord("0")
            for i in range(1, len(str)):    
                if str[i].isnumeric():
                    out = out*10 + (ord(str[i]) - ord("0"))        
                    if not negative and out >= 2147483647:
                        return 2147483647
                    if negative and out >= 2147483647:
                        return -2147483647
                else:
                    break
            if not negative:
                return out
            else:
                return -out

a = Soution()
print(a.fun("  153 adje"))
print(a.fun("   adje  77"))


        