
class Acceptor:
    def __init__(self,name):
        self.name=name
        self.proposal_promise=None
        self.proposal_acc=None
        self.value_acc= None

    def display(self):
        return {
        "name:":self.name,
        "promise number:":self.proposal_promise,
        "proposal number":self.proposal_acc,
        "value:":self.value_acc

        }    
    def prepare(self,proposal_num):
        if self.proposal_promise is not None and proposal_num<= self.proposal_promise:
            return None
        self.proposal_promise= proposal_num
        return {
            "promised":True,
            "accepted proposal": self.proposal_acc,
            "accepted value": self.value_acc
        }
    def accept(self,proposal_num,val):
        if self.proposal_promise is not None and proposal_num< self.proposal_promise:
            return False
        self.proposal_promise= proposal_num
        self.proposal_acc= proposal_num
        self.value_acc= val
        return True

