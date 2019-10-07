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
					if os.path.isfile("init.txt")=="true":
						liste=[]
						i=2
						f_init=open("init.txt", "r")
						for line in f_init:
							line=line.strip()
							if i%2==0:
								os.remove(line)
							i=i+1
						os.remove("init.txt")
					suite3=0
					while suite3==0:
						nbre_repas=input("Combien de types de repas voulez-vous ? ")
						if nbre_repas in range(1,100):
							suite2=0
							while suite2==0:
								print ("Choisissez la priorité de vos types de repas :")
								print ("1 - La même pour tous")
								print ("2 - Personnalisé (choisir le \% de chaque types)")
								proportion=input()
								if str(proportion)=="1" or str(proportion)=="2":
									proptotal=100
									for i in range(1,nbre_repas):
										type_repas=input("Choisissez le nom de votre "+str(i)+"e type : ")
										f_type = open(type_repas, "w")
										f_type.write("premier repas")
										f_type.write("\n")
										f_type.write("deuxième repas")
										f_type.close()
										f_init = open("init.txt", "w")
										f_init.write(str(type_repas))
										f_init.write("\n")
										f_init.close()
										if str(proportion)=="2":
											ok=0
											while ok==0:
												propperso=input("Quel pourcentage souhaitez-vous donner à ce type ? (entre 0 et "+proptotal") ")
												if propperso in range(0,proptotal):
													if proptotal-propperso<0:
														propperso=proptotal
													else:
														proptotal=proptotal-propperso
													f_init = open("init.txt", "w")
													f_init.write(str(propperso))
													f_init.write("\n")
													f_init.close()
													ok=1
												else:
													print ("Merci de choisir un pourcentage entre 0 et "+proptotal)
													pass
										else:
											proptotal//nbre_repas=propequit
											f_init=open("init.txt", "w")
											f_init.write(str(propequit))
											f_init.close()
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
			if os.path.isfile("init.txt")=="true":
				f_init=open("init.txt", "r")
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
				sorted(prop_repas.items(), key=lambda t: t[0])




			else:
				print ("Vous n'avez pas de fichiers de base.")
				pass


		suite=1

	else:
		print ("Merci de taper 1 ou 2 pour faire votre choix.")
		pass