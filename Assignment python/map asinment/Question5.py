from collections import OrderedDict
def remove_duplicate(Urvik):
  return "".join(OrderedDict.fromkeys("Urvik"))
     
print(remove_duplicate("My Name Is Urvik patel"))
print(remove_duplicate("mr.patel"))
