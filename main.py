from paxos.acceptor import Acceptor
from paxos.proposer import Proposer
# a1= Acceptor("A1")
# print("prepare:",a1.prepare(50))
# print("accept:", a1.accept(50,"pizza"))
# print("prepare:",a1.prepare(100))

# print("promise:",a1.proposal_promise)
# print("accept proposal:",a1.proposal_acc)
# print("accepted value:",a1.value_acc)
def data(acceptors):
    res= []
    for acc in acceptors:
        res.append(acc.display())
    return res

a1= Acceptor("A1")
a2= Acceptor("A2")
a3= Acceptor("A3")
acceptors=[a1,a2,a3]

a1.prepare(20)
proposal_num= 100
value= "Pizza"
p1= Proposer(proposal_num,value,acceptors)

res= p1.prorose()
print(res)

print(data(acceptors))

