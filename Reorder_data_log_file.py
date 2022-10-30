# from curses.ascii import isdigit


class Soution:
    
    def reorderlogfile(self, logs: list[str]) -> list[str]:
        
        res1, res2 = [], []
        for log in logs:
            if (log.split()[1]).isdigit():
                res2.append(log)
            else:
                res1.append(log.split())
        res1.sort(key = lambda x: x[0] )
        res2.sort(key = lambda x: x[1:])
        
        for i in range(len(res1)):
            res1[i] = (" ".join(res1[i]))
        res1.extend(res2)
        return res1
    
a = Soution()
print(a.reorderlogfile(["dig1 23", "let1 asd", "dig2 3 5", "let2 own kit", "let3 ddw"]))
