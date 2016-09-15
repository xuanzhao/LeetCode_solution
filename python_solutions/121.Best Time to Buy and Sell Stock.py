def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_prof = 0
    day_in = -1
    day_out = -1
    lis = []
    change = False

    for i in range(len(prices)):
        change = False
        for o, p in enumerate(prices[i+1:]):
            if prices[i] < p:
                if max_prof < p - prices[i]:
                    max_prof = p - prices[i]
                    day_in = i
                    day_out = i + o + 1
                    change = True
            lis.append(p)

        if change == False and len(lis) > 0:
            if len(lis) == 1: return max_prof
            i = 0
            while(lis[i] >= lis[i+1]):
                if i+1 == len(lis)-1 :
                    return max_prof
                i += 1
        lis = []
                    
    return max_prof

# %time maxProfit(a)
# CPU times: user 41.8 s, sys: 796 ms, total: 42.6 s
# Wall time: 42.9 s



def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    max = 0
    day_in = -1
    day_out = -1
    
    for i in range(len(prices)):
        for o, p in enumerate(prices[i+1:]):
            if prices[i] < p:
                if max < p - prices[i]:
                    max = p - prices[i]
                    day_in = i
                    day_out = i + o + 1

    
    return max


# %time maxProfit(a)
# CPU times: user 26.8 s, sys: 163 ms, total: 27 s
# Wall time: 27.2 s


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    max_prof = 0
    min_day = 0
    day_in = -1
    day_out = -1
    
    for i in range(len(prices)):
        min_day = prices[i]
        day_in = i
        for o, p in enumerate(prices[i+1:]):
            if prices[i] < p:
                if max_prof < p - prices[i]:
                    max_prof = p - prices[i]
                    day_out = i + o + 1
            elif p < min_day:
                min_day = p
                day_in = i + o + 1

        if day_out != -1:
            if min_day == prices[i]: return max_prof
            elif (day_out - day_in) > 0: return max_prof + (prices[i] - min_day)
    
    return max_prof

# CPU times: user 25.5 s, sys: 145 ms, total: 25.6 s
# Wall time: 25.8 s
# Out[150]: 3


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    def loop(prices):

        max_prof = 0
        min_day = 0
        day_in = -1
        day_out = -1
        reduced_prices = []
        prev_p = None

        for i in range(len(prices)):
            min_day = prices[i]
            day_in = i
            for o, p in enumerate(prices[i+1:]):
                if prev_p == p: continue
                elif prices[i] < p:
                    if max_prof < p - prices[i]:
                        max_prof = p - prices[i]
                        day_out = i + o + 1
                elif p < min_day:
                    min_day = p
                    day_in = i + o + 1

                reduced_prices.append(p)
                prev_p = p

            if day_out != -1:
                if min_day == prices[i]: return max_prof
                elif (day_out - day_in) > 0: return max_prof + (prices[i] - min_day)
        
        return loop(reduced_prices)

    return loop(prices)


# CPU times: user 25.5 s, sys: 447 ms, total: 25.9 s
# Wall time: 26.2 s
# Out[158]: 3

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    max_prof = 0
    min_day = 0
    day_in = -1
    day_out = -1
    
    prev_p = None
    reduced_prices = []
    for i, item in enumerate(prices):
        if prev_p == item: continue
        elif prev_p > item and (i+1) < len(prices) and item > prices[i+1]: continue
        else: 
            reduced_prices.append(item)
            prev_p = item

    for i in range(len(reduced_prices)):
        min_day = reduced_prices[i]
        day_in = i
        for o, p in enumerate(reduced_prices[i+1:]):
            if reduced_prices[i] < p:
                if max_prof < p - reduced_prices[i]:
                    max_prof = p - reduced_prices[i]
                    day_out = i + o + 1
            elif p < min_day:
                min_day = p
                day_in = i + o + 1

        if day_out != -1:
            if min_day == reduced_prices[i]: return max_prof
            elif (day_out - day_in) > 0: return max_prof + (reduced_prices[i] - min_day)
    
    return max_prof


# CPU times: user 4.88 ms, sys: 1.91 ms, total: 6.79 ms
# Wall time: 5.35 ms
# Out[191]: 3

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    min_in = 100000
    max_prof = 0

    for item in prices:
        if item < min_in:
            min_in = item
        elif item - min_in > max_prof:
            max_prof = item - min_in

    return max_prof


# CPU times: user 2.76 ms, sys: 1.34 ms, total: 4.1 ms
# Wall time: 3.15 ms
# Out[193]: 3













