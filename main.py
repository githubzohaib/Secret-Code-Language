st = input ("Enter Message: ")
words = st.split(" ")
coding = input("\n1 for Coding or 0 for Decoding: ")
coding = True if (coding=="1") else False
print(coding)
if (coding):
  nwords = []
  for word in words:
    if (len(word) >= 3):
      import random
      import string
      r1 = random.choice(string.ascii_letters)
      r2 = random.choice(string.ascii_letters)
      stnew = r1 + word[1:] + word[0] + r2
      nwords.append(stnew)

    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3):
      stnew = word[1:-1]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))    
      