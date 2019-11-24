import random
import os
import math

listefat = ['lasagne','hachis parmentier','tartiflette','pizza','ramen','croque monsieur','hot dog','filet americain','flammekuche','chili',
'cordons bleus pdt surg','cordon bleu gratin dauph',
'nuggets gratin dauphinois','nuggets pdt surg',
'risotto chorizo','risotto chorizo','risotto chorizo',
'pate carbo','pate carbo',
'merguez gratin dauph','merguez pdt surg']


listesteack=['steack tomate au four + qqchose','steack concombre tomate','steack haricot','steack petit pois carotte','steack palet de legume','steack purée de carotte','steack pate','steack riz','steack tipiak','steack jardiniere']
listepoulet=['poulet tomate au four + qqchose','poulet concombre tomate','poulet haricot','poulet petit pois carotte','poulet palet de legume','poulet purée de carotte','poulet pate','poulet riz','poulet tipiak','poulet jardiniere']
listeautresain = ['poisson epinard','tomate farcie','jambon pate','pate bolo','thon riz','thon haricot','poisson riz','poele thai au poulet','soupe/salade','taboulé','cereales et legume surg','pate epinard','salade cesar']





chiffre=int(input("Combien de repas voulez-vous ? "))
repasfat=(35*chiffre//100)
repassain=chiffre-repasfat
print (" ")
print ("___________________________________")
print ("___________________________________")
print (" ")
print ("Nombre de repas diet : "+str(repassain))
print (" ")
print ("Nombre de repas fat : "+str(repasfat))
print ("___________________________________")
print ("___________________________________")
suite=input()
print ("  _____________")
print (" ()____________)")
print (" |            |")
print (" | Repas diet |")
print (" |____________|")
print (" ()____________)")
print (" ")
if repassain==0:
	exit()
elif repassain==1:
	platsain=random.choice(listelegume)
	print ("	-> "+str(platsain))
elif repassain==2:
	for i in range(1,2):
		platsain=random.choice(listesteack)
		print ("	-> "+str(platsain))
		listesteack.remove(platsain)
elif repassain==3:
	platsain=random.choice(listesteack)
	print ("	-> "+str(platsain))
	listesteack.remove(platsain)
	platsain=random.choice(listesteack)
	print ("	-> "+str(platsain))
	platsain=random.choice(listepoulet)
	print ("	-> "+str(platsain))
else:
	platsain=random.choice(listesteack)
	print ("	-> "+str(platsain))
	listesteack.remove(platsain)
	platsain=random.choice(listesteack)
	print ("	-> "+str(platsain))
	platsain=random.choice(listepoulet)
	print ("	-> "+str(platsain))
	repassainrestant=repassain-3
	for i in range(0,repassainrestant):
		platsain=random.choice(listeautresain)
		print ("	-> "+str(platsain))
		listeautresain.remove(platsain)
print (" ")
print ("  ____________")
print (" ()___________)")
print (" |           |")
print (" | Repas fat |")
print (" |___________|")
print (" ()___________)")
print (" ")
if repasfat==0:
	suite=input()
	exit()
elif repasfat==1:
	platfat=random.choice(listefat)
	print("	-> "+str(platfat))
else:
	for i in range(0,repasfat):
		platfat=random.choice(listefat)
		print ("	-> "+str(platfat))
		listefat.remove(platfat)
suite=input()
