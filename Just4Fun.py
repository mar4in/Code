import random

class Entry:
	def __int__(a,deutsch,englisch):
		a.deutsch
		a.englisch
	def toString(a):
		return a.deutsch + " - "+a.englisch


eintraege=[]

def eingabe():
	while True:
		deutsch = input("Deutsches Wort: ")
		if deutsch == "#fertig":
			return
		englisch = input ("Englisches Wort: ")
		if englisch == "#fertig":
			return
		eintraege.append(Entry(deutsch, englisch))

def abfrage():
	while True:
		i = random.randint(0,len(eintraege)-1)
		englisch=input("Englische Übersetzung von "+eintraege[i].deutsch+": ")
		if (englisch == "#fertig"):
			return
		if eintraege[i].englisch==englisch:
			print("korrekt")
		else:
			print("leider falsch. Richtige Antwort: "+eintraege[i].englisch)

def printall():
	for eintrag in eintraege:
		print(eintrag.toString)



while True:
	befehl=input("Befehl:")
	if befehl=="eingabe":
		eingabe()
	elif befehl =="abfrage":
		abfrage()
	elif befehl =="beenden":
		break
	elif befehl=="ausgabe":
		printall()
	else:
		print("Keine bekannte ausgabe. Tippe eingabe, abfrage, ausgabe oder beenden.")

print("Fertig")