
import os
import random
import math

suite=0
while suite==0:
	print ("Voulez-vous initialiser vos fichiers de base ou les utiliser ?")
	print ("1 - Initialiser")
	print ("2 - Utiliser")
	ini=input()
	if str(ini)=="1" or str(ini)=="2":
		if ini==str("1"):
			suitebis=0
			while suitebis==0:
				print ("Vous êtes sûr de vouloir initialiser vos fichiers ?")
				print ("(Attention, si vous avez déjà des fichiers existants ils vont être réinitialisés)")
				print ("1 - Oui")
				print ("2 - Non")
				ini=input()
				if str(ini)=="1":
					suitebis=1
					print ("1 - Vous utilisez un OS Linux")
					print ("2 - Vous utilisez un OS Windows")
					systeme=input()
					if str(systeme)=="1":
						os.system("rm -rf fichier_base")
						os.mkdir("fichier_base")
					elif str(systeme)=="2":
						os.system("rmdir fichier_base /S /Q")
						os.mkdir("fichier_base")
					else:
						suitebis=0
						pass

#					if os.path.isfile("fichier_base/.init")=="true":
#						
#						liste=[]
#						i=2
#						f_init=open("fichier_base/init", "r")
#						for line in f_init:
#							line=line.strip()
#							if i%2==0:
#								os.remove(line)
#							i=i+1
#						os.remove("fichier_base/init")
					suite3=0
					while suite3==0:
						nbre_repas=input("Combien de types de repas voulez-vous ? ")
						if int(nbre_repas) in range(1,100):
							suite2=0
							#f_init = open("fichier_base/.init", "w")
							#f_init.write(nbre_repas)
							#f_init.close()
							while suite2==0:
								print ("Choisissez la priorité de vos types de repas :")
								print ("1 - La même pour tous")
								print ("2 - Personnalisé (choisir le pourcentage de chaque types)")
								proportion=input()
								if str(proportion)=="1" or str(proportion)=="2":
									proptotal=100
									for i in range(0,int(nbre_repas)):
										type_repas=input("Choisissez le nom de votre "+str(i+1)+"e type : repas ")
										f_type = open("fichier_base/"+str(type_repas), "w")
										f_type.write("premier repas")
										f_type.write("\n")
										f_type.write("deuxième repas")
										f_type.close()
										
										if str(proportion)=="2":
											ok=0
											while ok==0:
												prop=input("Quel pourcentage souhaitez-vous donner à ce type ? (entre 0 et "+str(proptotal)+") ")
												if int(prop) in range(0,int(proptotal)+1):
													proptotal=int(proptotal)-int(prop)
													ok=1
												else:
													print ("Merci de choisir un pourcentage entre 0 et "+str(proptotal))
													pass
										else:
											prop=int(proptotal)//int(nbre_repas)
									
										f_init = open("fichier_base/init", "a")
										f_init.write(str(type_repas))
										f_init.write("\n")
										f_init.write(str(prop))
										f_init.write("\n")
										f_init.close()


									#	f_tmp = open("fichier_base/"+str(i), "w")
									#	f_tmp.write(str(type_repas))
									#	f_tmp.write("\n")
									#	f_tmp.write(str(prop))
									#	f_tmp.close()
									suite2=1
								else:
									print ("Merci de choisir entre 1 et 2")
									pass
							suite3=1
						else:
							print ("Vous n'avez qu'à choisir le nombre de votre choix.")
							pass
				else:
					pass
		else:
			#utilisation fichier deja existant
			if os.path.isfile("fichier_base")=="true":
				f_init=open("fichier_base/init", "r")
				liste_repas=[]
				liste_prop=[]
				i=2
				for line in f_init:
					line=line.strip()
					if i%2==0:
						liste_repas.append(line)
					else:
						liste_prop.append(line)
					i=i+1
				chiffre=int(input("Combien de repas voulez-vous ? "))
				prop_repas={x:y for x,y in zip(liste_prop,liste_repas)}
				sorted(prop_repas.items(), key=lambda t: t[0], reverse=True)
				liste_repas = []
				liste_prop = []
				for k, v in prop_repas.items():
					liste_prop.append(k)
					liste_repas.append(v)
				chiffre=int(input("Combien de repas voulez-vous ? "))
				i=0
				for line in range(0,len(a)):
					n_repas=chiffre*int(liste_prop[0])//100
					if str(n_repas)>0:
						print ("  __________________")
						print (" ()_________________)")
						print (" ")
						print ("	"+str(liste_repas[i])+"	")
						print ("  __________________")
						print (" ()_________________)")
						print (" ")
						fich=open("fichier_base/"+str(liste_repas[i]), "r")
						repas_plat=[]
						for plat in fich:
							plat=plat.strip()
							repas_plat.append(plat)
						for abc in range(0,n_repas):
							plat=random.choice(repas_plat)
							print ("	-> "+str(plat))
							repas_plat.remove(plat)
					i=i+1
			else:
				print ("Vous n'avez pas de fichiers de base.")
				pass

	else:
		print ("Merci de taper 1 ou 2 pour faire votre choix.")
		pass