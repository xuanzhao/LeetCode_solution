class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1, self.s2 = [], []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.s2 == []:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())

        self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.s2 == []:
            for i in range(len(self.s1)):
                self.s2.append(self.s1.pop())
        
        return self.s2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.s1 and not self.s2