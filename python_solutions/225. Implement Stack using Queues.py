class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1, self.q2 = [], []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)
        if len(q1) == 1: return None
        else: q2.append(q1.pop(0))

    def pop(self):
        """
        :rtype: nothing
        """
        self.q1.pop()
        for i in range(len(self.q2)-1):
            self.q1.append(self.q2.pop(0))

        self.q1, self.q2 = self.q2, self.q1
        

    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.q1 == [] and self.q2 == []:
            return True
        else: return False