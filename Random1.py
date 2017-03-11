    # import libs

import random

    # define vars

i = 0
Heads = 0
Tails = 0
Edge = 0

    # begin loop - assumes equal probabilites for all three results

for i in range(24):
  decider = random.randrange(3)
  if decider == 0:
    print("Heads")
    Heads = Heads + 1
  elif decider == 1:
    print("Tails")
    Tails = Tails + 1
  elif decider == 2:
    print ("On the Edge")
    Edge = Edge + 1
    
      # print result

print ("")
print ("# of Heads: ", Heads)
print ("")
print ("# of Tails:", Tails)
print ("")
print ("# on the Edge: ", Edge)



