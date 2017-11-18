# -*- coding: utf-8 -*-

## FileSync ##
from os import path
from os import system
import glob

## Config ##
PathOnC = ""
OrdnerName = "test"

print("\033[46m    //####### ## //        //#######    \033[0m")
print("\033[46m   //        ## //        //            \033[0m")
print("\033[46m  //#####   ## //        //######       \033[0m")
print("\033[46m //        ## //        //              \033[0m")
print("\033[46m//        ## //####### //#######        \033[0m")
print("\033[43m----------------------------------------\033[0m")
print("\033[46m 	  ====  ||  //  /||   //   //===\033[0m")
print("\033[46m 	 //     || //  //||  //   //    \033[0m")
print("\033[46m 	 ====   |##/  // || //   ||     \033[0m")
print("\033[46m  	   //    //  //  ||//     \\     \033[0m")
print("\033[46m 	====    //  //   |//   	   \\=== \033[0m")

def dateinIndexieren():
	print("\033[93m \033[4m *****  \033[95mIndexiere Dateien 🗃 \033[93m *****\033[0m")

	print("\033[31m *** Liste alle Items auf C ... \033[0m")
	tree = glob.glob(PfadAufHDD + OrdnerName + "/*")
	ItemsHDD = []
	unterordner = []

	for item in tree:
		if path.isfile(item):
			print(" ** 📝 \033[92m" + path.split(item)[1] + " gefunden !\033[0m")
			ItemsHDD.append(item)
		else:
			unterordner.append(item)

	for itemOrdner in unterordner:
		tree = glob.glob(itemOrdner + "/*")

		for fileItem in tree:
			if path.isfile(fileItem):
				print(" ** 📝 \033[92m" + path.split(itemOrdner)[1] + "/" + path.split(fileItem)[1] + " gefunden !\033[0m")
				ItemsHDD.append(fileItem)

	#print(" ** 🎉 FERTIG! \033[0m **")
	print(" **")

	print("\033[31m *** Liste alle Datein von USB ...\033[0m ")
	tree = glob.glob("./" + OrdnerName + "/*")
	ItemsUSB = []
	unterordnerAufUSB = []

	for item in tree:
		if path.isfile(item):
			print(" ** 📝 \033[92m " + path.split(item)[1] + " gefunden !\033[0m")
			ItemsUSB.append(item)
		else:
			unterordnerAufUSB.append(item)

	for itemOrdner in unterordnerAufUSB:
		tree = glob.glob(itemOrdner + "/*")

		for fileItem in tree:
			if path.isfile(fileItem):
				print(" ** 📝 \033[92m " + path.split(itemOrdner)[1] + "/" + path.split(fileItem)[1] + " gefunden !\033[0m")
				ItemsUSB.append(fileItem)

	print("\033[93m ** 🎉 FERTIG! **\033[0m ")
	print(" ")

	return (ItemsHDD, ItemsUSB)

def backupErstellen():
	print("\033[93m \033[4m ***** \033[95mErstelle BackUp Ordner 💾\033[93m *****\033[0m")
	print("\033[31m ** Lösche altes BackUp ❌ (falls vorhanden)\033[0m")

	print("\033[36m ** ✅ -> C \033[0m")
	system("rm -fr {0}/filesync_backup".format(PfadAufHDD))

	print("\033[36m ** ✅ -> USB \033[0m")
	system("rm -fr {0}/filesync_backup".format("."))

	print(" **")

	print("\033[31m ** Neues BackUp erstellen \033[0m 🛁")

	print("\033[92m ** ✅ -> C \033[0m")
	system("cp -R {0}/{1} {0}/filesync_backup".format(PfadAufHDD, OrdnerName))

	print("\033[92m ** ✅ -> USB \033[0m")
	system("cp -R ./{0} filesync_backup".format(OrdnerName))

	print(" ")

def mtimeGenerieren(itemsHDD, itemsUSB):
	print("\033[93m \033[4m ***** \033[95mGeneriere Array mit mTimes 🕒🛠 \033[93m *****\033[0m")

	print("\033[31m *** Für C \033[0m ")
	timesHDD = {}

	for item in itemsHDD:
		mTime = path.getmtime(item)
		print(" ** 🕑 \033[35m" + path.split(item)[1] + " => \033[36m" + str(mTime) + "\033[0m")
		timesHDD[str(item)] = mTime

	print(" **")

	print("\033[31m *** Für USB \033[0m ")
	timesUSB = {}

	for item in itemsUSB:
		mTime = path.getmtime(item)
		print(" ** 🕣 \033[35m" + path.split(item)[1] + " => \033[36m" + str(mTime) + "\033[0m")
		timesUSB[str(item)] = mTime

	print("\033[93m ** 🎉 FERTIG! **\033[0m ")
	print(" ")
	return (timesHDD, timesUSB)

def synCzuUSB(itemsHDD, itemsUSB, timesHDD, timesUSB):
	print("\033[93m \033[4m *****\033[95m Synchronisere Dateien (neue Dateien von C zu USB)\033[93m *****\033[0m")

	for item in itemsHDD:
		itemMTime = timesHDD[str(item)]

		#Gibt es diese Datei auch auf dem USB Pfad:

		treeItems = item.split("/")
		unterordnerName = treeItems[len(treeItems) - 2]
		dateiname =  treeItems[len(treeItems) - 1]

		if unterordnerName == OrdnerName:
			dateipfadUSB = "./" + OrdnerName + "/" + dateiname

			#Vergleichen welche Datei älter ist
			if timesHDD[item] > timesUSB.get(dateipfadUSB, 0):
				print(" ** \033[93m \033[01m Sync " + str(dateiname) + " von C zu USB ! \033[0m")
				bewegeDateiVon(item, dateipfadUSB)

			elif timesHDD[item] == timesUSB.get(dateipfadUSB, 0):
				print(" ** \033[92m \033[01m Datei " + str(dateiname) + " ist auf beiden aktuell ! \033[0m")

			else:
				print(" ** \033[93m \033[01m Sync " + str(dateiname) + " von USB zu C ! \033[0m")
				bewegeDateiVon(dateipfadUSB, item)


		else:
			dateipfadUSB = "./" + OrdnerName + "/" + unterordnerName + "/" + dateiname
			if path.lexists("./" + OrdnerName + "/" + unterordnerName + "/"):
				#Ordner existiert aus USB -> Vergleichen welche Datei älter ist

				if timesHDD[item] > timesUSB.get(dateipfadUSB, 0):
					print(" ** \033[93m \033[01m Sync " + str(unterordnerName) + "/" + str(dateiname) + " von C zu USB ! \033[0m")
					bewegeDateiVon(item, dateipfadUSB)

				elif timesHDD[item] == timesUSB.get(dateipfadUSB, 0):
					print(" ** \033[92m \033[01m Datei " + str(unterordnerName) + "/" + str(dateiname) + " ist auf beiden aktuell ! \033[0m")

				else:
					print(" ** \033[93m \033[01m Sync " + str(unterordnerName) + "/" + str(dateiname) + " von USB zu C ! \033[0m")
					bewegeDateiVon(dateipfadUSB, item)

			else:
				#Der Ordner existiert nicht auf dem USB -> erstellen und Datei kopieren
				system("mkdir ./" + OrdnerName + "/" + unterordnerName + "/")
				print(" ** \033[93m \033[01m Sync " + unterordnerName + "/" + str(dateiname) + " von C zu USB ! \033[0m")
				bewegeDateiVon(item, dateipfadUSB)

		#Lösche das Item aus dem Array, damit es nicht nochmal bearbeitet wird in der synUSBzuC
		try:
			itemsUSB.remove(dateipfadUSB)
			timesUSB[dateipfadUSB] = 0
		except ValueError:
			pass

	print("")
	return itemsUSB

def bewegeDateiVon(start, ziel):
	system("cp -f {0} {1}".format(start, ziel))


def synUSBzuC(itemsUSB, timesHDD, timesUSB):
	print("\033[93m \033[4m ***** \033[95mSynchronisere neue Dateien von USB\033[93m *****\033[0m")

	for item in itemsUSB:
		#Gibt es diese Datei auch auf C:

		treeItems = item.split("/")
		unterordnerName = treeItems[len(treeItems) - 2]
		dateiname =  treeItems[len(treeItems) - 1]

		if unterordnerName == OrdnerName:
			dateipfadHDD = PfadAufHDD + OrdnerName + "/" + dateiname

			#Vergleichen welche Datei älter ist
			if  timesUSB[item] > timesHDD.get(dateipfadHDD, 0):
				print(" ** \033[93m \033[01m Sync " + str(dateiname) + " von USB zu C ! \033[0m")
				bewegeDateiVon(item, dateipfadHDD)

			elif timesUSB[item] == timesHDD.get(dateipfadHDD, 0):
				print(" ** \033[92m \033[01m Datei " + str(dateiname) + " ist auf beiden aktuell ! \033[0m")

			else:
				print(" ** \033[93m \033[01m Sync " + str(dateiname) + " von C zu USB! \033[0m")
				bewegeDateiVon(dateipfadHDD, item)

		else:
			dateipfadHDD = PfadAufHDD + OrdnerName + "/" + unterordnerName + "/" + dateiname
			if path.lexists(PfadAufHDD + OrdnerName + "/" + unterordnerName + "/"):
				#Ordner existiert in C -> Vergleichen welche Datei älter ist

				if timesUSB[item] > timesHDD.get(dateipfadHDD, 0):
					print(" ** \033[93m \033[01m Sync " + str(unterordnerName) + "/"+ str(dateiname) + " von USB zu C ! \033[0m")
					bewegeDateiVon(item, dateipfadHDD)

				elif timesUSB[item] == timesHDD.get(dateipfadHDD, 0):
					print(" ** \033[92m \033[01m Datei " + str(unterordnerName) + "/" + str(dateiname) + " ist auf beiden aktuell ! \033[0m")

				else:
					print(" ** \033[93m \033[01m Sync " + str(unterordnerName) + "/" + str(dateiname) + " von C zu USB! \033[0m")
					bewegeDateiVon(dateipfadHDD, item)

			else:
				#Der Ordner existiert nicht auf C -> erstellen und Datei kopieren
				system("mkdir " + PfadAufHDD + OrdnerName + "/" + unterordnerName + "/")
				print(" ** \033[93m \033[01m Sync " + str(dateiname) + " von USB zu C ! \033[0m")
				bewegeDateiVon(item, dateipfadHDD)

	if len(itemsUSB) == 0:
		print(" ** Keine da 🤷")


backupErstellen()
iHDD, iUSB = dateinIndexieren()
mHDD, mUSB = mtimeGenerieren(iHDD, iUSB)
iUSB = synCzuUSB(iHDD, iUSB, mHDD, mUSB)
synUSBzuC(iUSB, mHDD, mUSB)