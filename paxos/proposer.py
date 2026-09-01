
class Proposer:
    def __init__(self,proposal_num,value, acceptors):
        self.proposal_num= proposal_num
        self.value= value
        self.acceptors= acceptors

    def prepare(self):
        res=[]
        for acceptor in self.acceptors:
            isAcept= acceptor.prepare(self.proposal_num)
            if isAcept is not None:
                res.append(isAcept)
        return res
    def isMajority(self,real_acceptor):
        return real_acceptor>len(self.acceptors)//2

    def prorose(self):
        res= len(self.prepare())
        if not self.isMajority(res): return None
        acc= self.isAccepted()
        if not self.isMajority(acc): return None
        return self.value 
    
    def isAccepted(self):
        cnt= 0
        for acc in self.acceptors:
            isAccepted= acc.accept(self.proposal_num,self.value)
            if isAccepted: cnt+=1
        return cnt