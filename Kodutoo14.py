
import csv
import random
import string


List=[]
ClassList=[]
Grouplist=[]
#Klassi loomine
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
#csv faili avamine
Ava= input("Faili nimi mida soovite avada: ")
Ava= str(Ava+'.csv')

with open(Ava, 'r',) as fail:
    for Inimene in csv.reader(fail):
        ClassList.append(Person(Inimene[0],Inimene[1],Inimene[2]))

#Tõstan Klassist Listi tagasi
for x in ClassList:
    List.append([x.first_name,x.last_name,x.age])


def NimedKontroll():
    #Kontrollib igat tähte 0 ja 1 veerus
    for x in List:
        #Kontrollib, et ees- ja perekonnanimi sisaldaks tähti ja tühikuid, kui ei sisalda siis prindib järgneva...
        for i in x[0] or x[1]:
            if  not i in (string.ascii_letters + " "+'Õ'+'õ'+'Ä'+'ä'+'Ü'+'ü'+'Ö'+'ö'):
                print("Ees- või perekonnanimes on tundmatu sümbol")
                print(x)
                return False
            else:
                return True
                
                
  
def VanusKontroll():
    #Kontrollib igat numbrit 2 veerus
    for x in List:
        assert 0<int(x[2])<=100, "Ei ole vahemikus 0..100"

    for x in List:
        for i in x[2]:
            #Kontrollib, et vanus oleks number, kui ei ole number siis prindib järgneva...
            if not i in string.digits  :
                print("Vanus sisaldab tundmatut sümbolit")
                print(i)
                return False
            else:
                return True                            

NimedKontroll()
VanusKontroll()

MaxInimesiGrupis= int(input("Maksimaalne number inimesi, mis võib ühes rühmas olla: "))
assert 0<MaxInimesiGrupis<=len(List), "Inimesi on vähem kui rühmi"

#segab grupid ära
random.shuffle(List)


Grouplist=[List[i:i+MaxInimesiGrupis] for i in range(0, len(List), MaxInimesiGrupis)]

Gruppe= int(round(len(List)/MaxInimesiGrupis,0))

loe1=0
loe2=1

"""while loe1<len(Grouplist[0])+1:
    Gnimi="grupp_"+ str(loe2)+".csv"
    with open(Gnimi, 'w') as Gfail:
        csvwriter=csv.writer(Gfail)
        csvwriter.writerows(Grouplist[loe1])
    print(Grouplist[loe1])
    loe2=loe2+1
    loe1=loe1+1"""
   

def Test1():
    if NimedKontroll()== True or VanusKontroll()==True:
        return "Test 1 Passed!"
    else:
        return "Test 1 Failed"
def Test2():
    if NimedKontroll()== True:
        return "Test 2 Passed!"
    else:
        return "Test 2 Failed"


print(Test1())
print(Test2())








