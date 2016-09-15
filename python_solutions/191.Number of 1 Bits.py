def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """

    def decToBi(n):
		num = []
		while (n != 0):
			num.append(n % 2)
			n = n / 2
		
		num.reverse()
		return num

    return sum(decToBi(n))


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    return bin(n).count('1')


def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while(n != 0):
    	if n%2 == 1: count +=1
    	n /= 2

    return count