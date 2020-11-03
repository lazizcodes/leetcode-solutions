class Solution(object):    
    def nthUglyNumber(self, n):

        ugly_list = []
        ugly_list.append(1)
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n + 1):
            m = min(ugly_list[p2] * 2, ugly_list[p3] * 3, ugly_list[p5] * 5)
            ugly_list.append(m)
            
            if m == ugly_list[p2] * 2: 
                p2 += 1
            if m == ugly_list[p3] * 3:
                p3 += 1
            if m == ugly_list[p5] * 5:
                p5 += 1
        
        return ugly_list[n - 1]