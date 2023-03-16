from functools import reduce
import numpy as np
num = "-60x^2-5x+30" #put input
denum = "12x^2-27x+6" #put input

def turntolist(numordenum):
  numordenum = numordenum.replace("-","+-")
  numordenum = numordenum.split("+")
  if "True" in numordenum or "False" in numordenum:
    raise Exception("NiceTry")
  result = []
  for i in numordenum:
    toappend = ""
    alpha_inserted = False
    digit_inserted = False
    expo = 0
    for j in i:        
      if j.isdigit() and digit_inserted == False:
        toappend += j
        digit_insterted = True  
      elif j == "-" :
        toappend+= "-"
      elif j.isalpha() or j == "^":
        alpha_inserted = True
        digit_inserted = True
      elif j.isdigit() and digit_inserted == True:
        expo += int(j)
    while len(result) < expo+1:
      result.append(0)
    if alpha_inserted == True and expo == 0:
      expo = 1
    if toappend == "" or toappend == "-":
      toappend += "1"
      result[expo] = int(toappend)
    else:
      result[expo] = int(toappend)
  return result
  
####################
num = turntolist(num)
denum = turntolist(denum)
#if len(denum) <= len(num):
  #raise Exception("Dont be lazy and do the long fraction")
################################################################################
def gcd_list(nums):
  return (np.gcd.reduce(nums))

def findfactors(n):
  result = []
  for i in range(1, int(n**0.5) + 1): 
    if n % i == 0:   
      result.append(i)
      result.append(n//i)
  return result

def findpairmulti(original_list,  to_multi):
  copy = original_list
  original_list = original_list[:-1]
  answer = []
  length_copy = len(copy)
  for i in original_list:
    copy = copy[1:]
    for j in range(len(copy)):
      if i * copy[j] == to_multi:
        answer += [(i,copy[j])]
  answer = list(set(answer))
  return answer

################################################################################
def factorize(thalist):
  factored = []
  while len(thalist) != 0:
##################### factor ou gcd
    if gcd_list(thalist) != 1:
        gcd = gcd_list(thalist)
        factored += str(gcd)
        thalist = [num // gcd for num in thalist]
##################### factor out x
    while thalist[0] == 0:
      thalist = thalist[1:]
      factored += "x"
##################### when 2x+2 or 4x+2 ect.
    if len([num for num in thalist if num != 0]) == 2: #check for non 0 numbers
      lastlist = [num for num in thalist if num != 0] #get an abrievated list of non 0 numbers so that theres is no extra 0s
      biggestexpo = len(thalist) -1 # get the biggest expo (assuming that the other integer is expo 0)
      if float(lastlist[1] / lastlist[0]).is_integer() and lastlist[0] != 1 and lastlist[0] != -1: #check if the smaller is a diviser of the bigger and != 1
        div = lastlist[0] #store the divider
        factored += str(div) #add constant factor
        factored.append(f"{lastlist[1]//div}x^{biggestexpo} + {lastlist[0]//div}") #add divided factor
        return factored
      elif float(lastlist[0] / lastlist[1]).is_integer() and lastlist[1] != 1 and lastlist[1] != -1: #check if bigger is a diviser of the bigger and != 1
        div = lastlist[1] #store the divider
        factored += str(div) #add constant factor
        factored.append(f"{lastlist[1]//div}x^{biggestexpo} + {lastlist[0]//div}") #add divided factor
        return factored  
      else:
        if lastlist[1] == 1:
          factored.append(f"x^{biggestexpo} + {lastlist[0]}")
        else:
          factored.append(f"{lastlist[1]}x^{biggestexpo} + {lastlist[0]}")
        return factored
#######################
    if len(thalist) == 3 and 0 not in thalist:
      to_add = thalist[1]
      to_multi = thalist[0] * thalist[2]
      add_is_negative = False
      multi_is_negative = False
      if to_multi < 0:
        multi_is_negative = True
        to_multi = to_multi * -1
      factors = findfactors(to_multi)
      if to_add < 0:
        negativefacts = [-1*num for num in factors]
        factors += negativefacts
      if multi_is_negative == True:
        negativefacts = [-1*num for num in factors] 
        factors += negativefacts
        to_multi = to_multi*-1
      multies = findpairmulti(factors, to_multi)
      for pair in multies:
        if pair[0] + pair[1] == to_add:
          roots = list(pair)
      roots0 = roots[0]
      roots1 = roots[1]
      root0n = 0
      root1n = 0
      if roots0 < 0:
        root0n = 1
        roots0 = roots0*-1
      if roots1 < 0:
        root1n = 1
        roots1 = roots1*-1
      rootfac0 = findfactors(roots0)
      rootfac1 = findfactors(roots1)
      if root0n == 1:
        rootfac0 += [-1*num for num in rootfac0]
      if root1n == 1:
        rootfac1 += [-1*num for num in rootfac1]
      for i in rootfac0:
        for j in rootfac1:
          if i*j == thalist[0]:
            newroots = (j,i)
            newcoeff = (int(roots[0]/i),int(roots[1]/j))
      factored.append(f"({newcoeff[0]}x + {newroots[0]})")
      factored.append(f"({newcoeff[1]}x + {newroots[1]})")
      return factored
################################################################################
print(factorize(num))
print(factorize(denum))
