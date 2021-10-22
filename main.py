from replit import clear
from art import logo
print(logo)
over=False
def chec(dicc):
  a=0
  b=""
  for k in dic:
    if dicc[k]>a:
      a=dicc[k]
      b=k # print(a,b)

  print(a,".rs is the highest bid amount by",b)
  #print(listt)
  place=listt.index(a)
  for i in range(place+1,len(listt)):
    if listt[i]==a:
      print("But wait TIE between",b,"and",listt[i-1])
    else:
      pass
  
dic={}
listt=[]
while not over:
  n=input("Whats your name:")
  b=int(input("Type your bid amount: rs."))
  dic[n]=b
  listt+=n,b
  ovr=input("Do you see other people who's gonna bid after you  'y' or 'no':").lower()
  if ovr=="no":
    over=True
    print("Ok Good luck")
  else:
    clear()
# print(dic)
chec(dic)






