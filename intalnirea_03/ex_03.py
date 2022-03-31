# Given the set: animals1 = {"wolf", "cheetah", "elephant", "crocodile"},
# add the following list of animals to it: lst1 = ["horse", "chimpanzee"]
# and then return only elements unique between set animals1 and set
# animals2 = {"jaguar", "horse", "wolf", "crocodile"}
# => {"cheetah", "elephant", "chimpanzee", "jaguar"}
'''
animals1 = {"wolf", "cheetah", "elephant", "crocodile"}
lst1 = ["horse", "chimpanzee"]
animals2 = {"jaguar", "horse", "wolf", "crocodile"}
for elem in lst1:
    animals1.add(elem)
print(animals1)
print(animals1 ^ animals2)'''
populatie = input('Populatia =')
if populatie.find('mil')>=0 :
   populatie = float(populatie.strip('mil')) * 1_000_000
   print(int(populatie))
elif populatie.find('bil') >=0 :
     populatie = float(populatie.strip('bil')) * 1_000_000_000
     print(int(populatie))

else:
    print(int(populatie))
