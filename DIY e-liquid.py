import os

def clear():

    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

cbase = int(input('Veuillez faire un choix parmis les bases entre\n 1 70/30\n 2 50/50\n 3 30/70\n 4 20/80\n 5 0/100\n Entrer 1,2,3,4 ou 5\n'))
if cbase > 5:
	print('Ceci n\'ai pas un choix valide')
	exit()
else:
	print('Vous avez choisi', cbase)	
	
if cbase == 1:
	qs = int(input('Veuillez indiquer la quantitée de produit fini souhaitée en ML\n'))
	liquide = qs
	tn = int(input('Veuillez indiquer le taux de nicotine souhaité en ML\n'))
	pvvg = 0.8
	concentration = 12
	concentration2 = concentration * pvvg
	arome = liquide * (concentration2 / 100)
	booster = (liquide * tn) / 20
	base = liquide - (booster + arome)
	myAromeNumber = round(arome, 1)
	myBoosterNumber = round(booster, 1)
	myBaseNumber = round(base, 1)
	clear()
	print('Pour réaliser votre e-liquide il vous faudra : \n', myAromeNumber, 'ML d\'arôme\n', myBoosterNumber, 'ML de booster de nicotine\n', myBaseNumber, 'ML de base en 70/30')
	
if cbase == 2:
	qs = int(input('Veuillez indiquer la quantitée de produit fini souhaitée en ML\n'))
	liquide = qs
	tn = int(input('Veuillez indiquer le taux de nicotine souhaité en ML\n'))
	pvvg = 1
	concentration = 12
	concentration2 = concentration * pvvg
	arome = liquide * (concentration2 / 100)
	booster = (liquide * tn) / 20
	base = liquide - (booster + arome)
	myAromeNumber = round(arome, 1)
	myBoosterNumber = round(booster, 1)
	myBaseNumber = round(base, 1)
	clear()
	print('Pour réaliser votre e-liquide il vous faudra : \n', myAromeNumber, 'ML d\'arôme\n', myBoosterNumber, 'ML de booster de nicotine\n', myBaseNumber, 'ML de base en 70/30')
	
if cbase == 3:
	qs = int(input('Veuillez indiquer la quantitée de produit fini souhaitée en ML\n'))
	liquide = qs
	tn = int(input('Veuillez indiquer le taux de nicotine souhaité en ML\n'))
	pvvg = 1.33333333333333
	concentration = 12
	concentration2 = concentration * pvvg
	arome = liquide * (concentration2 / 100)
	booster = (liquide * tn) / 20
	base = liquide - (booster + arome)
	myAromeNumber = round(arome, 1)
	myBoosterNumber = round(booster, 1)
	myBaseNumber = round(base, 1)
	clear()
	print('Pour réaliser votre e-liquide il vous faudra : \n', myAromeNumber, 'ML d\'arôme\n', myBoosterNumber, 'ML de booster de nicotine\n', myBaseNumber, 'ML de base en 70/30')
	
if cbase == 4:
	qs = int(input('Veuillez indiquer la quantitée de produit fini souhaitée en ML\n'))
	liquide = qs
	tn = int(input('Veuillez indiquer le taux de nicotine souhaité en ML\n'))
	pvvg = 1.46666666666667
	concentration = 12
	concentration2 = concentration * pvvg
	arome = liquide * (concentration2 / 100)
	booster = (liquide * tn) / 20
	base = liquide - (booster + arome)
	myAromeNumber = round(arome, 1)
	myBoosterNumber = round(booster, 1)
	myBaseNumber = round(base, 1)
	clear()
	print('Pour réaliser votre e-liquide il vous faudra : \n', myAromeNumber, 'ML d\'arôme\n', myBoosterNumber, 'ML de booster de nicotine\n', myBaseNumber, 'ML de base en 70/30')
	
if cbase == 5:
	qs = int(input('Veuillez indiquer la quantitée de produit fini souhaitée en ML\n'))
	liquide = qs
	tn = int(input('Veuillez indiquer le taux de nicotine souhaité en ML\n'))
	pvvg = 1.66666666666666
	concentration = 12
	concentration2 = concentration * pvvg
	arome = liquide * (concentration2 / 100)
	booster = (liquide * tn) / 20
	base = liquide - (booster + arome)
	myAromeNumber = round(arome, 1)
	myBoosterNumber = round(booster, 1)
	myBaseNumber = round(base, 1)
	clear()
	print('Pour réaliser votre e-liquide il vous faudra : \n', myAromeNumber, 'ML d\'arôme\n', myBoosterNumber, 'ML de booster de nicotine\n', myBaseNumber, 'ML de base en 70/30')