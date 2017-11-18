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
	tree = glob.glob(PathOnC + OrdnerName + "/*")
	ItemsOnC = []
	OrdnerOnC = []

	for item in tree:
		if path.isfile(item):
			print(" ** 📝 \033[92m" + path.split(item)[1] + " gefunden !\033[0m")
			ItemsOnC.append(item)
		else:
			OrdnerOnC.append(item)

	for itemOrdner in OrdnerOnC:
		tree = glob.glob(itemOrdner + "/*")

		for fileItem in tree:
			if path.isfile(fileItem):
				print(" ** 📝 \033[92m" + path.split(itemOrdner)[1] + "/" + path.split(fileItem)[1] + " gefunden !\033[0m")
				ItemsOnC.append(fileItem)

	#print(" ** 🎉 FERTIG! \033[0m **")
	print(" **")

	print("\033[31m *** Liste alle Datein von USB ...\033[0m ")
	tree = glob.glob("./" + OrdnerName + "/*")
	ItemsOnUSB = []
	OrdnerOnUSB = []

	for item in tree:
		if path.isfile(item):
			print(" ** 📝 \033[92m " + path.split(item)[1] + " gefunden !\033[0m")
			ItemsOnUSB.append(item)
		else:
			OrdnerOnUSB.append(item)

	for itemOrdner in OrdnerOnUSB:
		tree = glob.glob(itemOrdner + "/*")

		for fileItem in tree:
			if path.isfile(fileItem):
				print(" ** 📝 \033[92m " + path.split(itemOrdner)[1] + "/" + path.split(fileItem)[1] + " gefunden !\033[0m")
				ItemsOnUSB.append(fileItem)

	print("\033[93m ** 🎉 FERTIG! **\033[0m ")
	print(" ")

	return (ItemsOnC, ItemsOnUSB)

def backupErstellen():
	print("\033[93m \033[4m ***** \033[95mErstelle BackUp Ordner 💾\033[93m *****\033[0m")
	print("\033[31m ** Lösche altes BackUp ❌ (falls vorhanden)\033[0m")

	print("\033[36m ** ✅ -> C \033[0m")
	system("rm -fr {0}/filesync_backup".format(PathOnC))

	print("\033[36m ** ✅ -> USB \033[0m")
	system("rm -fr {0}/filesync_backup".format("."))

	print(" **")

	print("\033[31m ** Neues BackUp erstellen \033[0m 🛁")

	print("\033[92m ** ✅ -> C \033[0m")
	system("cp -R {0}/{1} {0}/filesync_backup".format(PathOnC, OrdnerName))

	print("\033[92m ** ✅ -> USB \033[0m")
	system("cp -R ./{0} filesync_backup".format(OrdnerName))

	print(" ")

def mtimeGenerieren(ItemsOnC, ItemsOnUSB):
	print("\033[93m \033[4m ***** \033[95mGeneriere Array mit mTimes 🕒🛠 \033[93m *****\033[0m")

	print("\033[31m *** Für C \033[0m ")
	cTimes = {}

	for item in ItemsOnC:
		mTime = path.getmtime(item)
		print(" ** 🕑 \033[35m" + path.split(item)[1] + " => \033[36m" + str(mTime) + "\033[0m")
		cTimes[str(item)] = mTime

	print(" **")

	print("\033[31m *** Für USB \033[0m ")
	usbTimes = {}

	for item in ItemsOnUSB:
		mTime = path.getmtime(item)
		print(" ** 🕣 \033[35m" + path.split(item)[1] + " => \033[36m" + str(mTime) + "\033[0m")
		usbTimes[str(item)] = mTime

	print("\033[93m ** 🎉 FERTIG! **\033[0m ")
	print(" ")
	return (cTimes, usbTimes)

def synCzuUSB(ItemsOnC, ItemsOnUSB, cTimes, usbTimes):
	print("\033[93m \033[4m *****\033[95m Synchronisere Dateien (neue Dateien von C zu USB)\033[93m *****\033[0m")

	for item in ItemsOnC:
		itemMTime = cTimes[str(item)]

		#Gibt es diese Datei auch auf dem USB Pfad:

		treeItems = item.split("/")
		unterOrdnerName = treeItems[len(treeItems) - 2]
		fileName =  treeItems[len(treeItems) - 1]

		if unterOrdnerName == OrdnerName:
			itemPfadOnUSB = "./" + OrdnerName + "/" + fileName

			#Vergleichen welche Datei älter ist
			if cTimes[item] > usbTimes.get(itemPfadOnUSB, 0):
				print(" ** \033[93m \033[01m Sync " + str(fileName) + " von C zu USB ! \033[0m")
				bewegeDateiVon(item, itemPfadOnUSB)

			elif cTimes[item] == usbTimes.get(itemPfadOnUSB, 0):
				print(" ** \033[92m \033[01m Datei " + str(fileName) + " ist auf beiden aktuell ! \033[0m")

			else:
				print(" ** \033[93m \033[01m Sync " + str(fileName) + " von USB zu C ! \033[0m")
				bewegeDateiVon(itemPfadOnUSB, item)


		else:
			itemPfadOnUSB = "./" + OrdnerName + "/" + unterOrdnerName + "/" + fileName
			if path.lexists("./" + OrdnerName + "/" + unterOrdnerName + "/"):
				#Ordner existiert aus USB -> Vergleichen welche Datei älter ist

				if cTimes[item] > usbTimes.get(itemPfadOnUSB, 0):
					print(" ** \033[93m \033[01m Sync " + str(unterOrdnerName) + "/" + str(fileName) + " von C zu USB ! \033[0m")
					bewegeDateiVon(item, itemPfadOnUSB)

				elif cTimes[item] == usbTimes.get(itemPfadOnUSB, 0):
					print(" ** \033[92m \033[01m Datei " + str(unterOrdnerName) + "/" + str(fileName) + " ist auf beiden aktuell ! \033[0m")

				else:
					print(" ** \033[93m \033[01m Sync " + str(unterOrdnerName) + "/" + str(fileName) + " von USB zu C ! \033[0m")
					bewegeDateiVon(itemPfadOnUSB, item)

			else:
				#Der Ordner existiert nicht auf dem USB -> erstellen und Datei kopieren
				system("mkdir ./" + OrdnerName + "/" + unterOrdnerName + "/")
				print(" ** \033[93m \033[01m Sync " + unterOrdnerName + "/" + str(fileName) + " von C zu USB ! \033[0m")
				bewegeDateiVon(item, itemPfadOnUSB)

		#Lösche das Item aus dem Array, damit es nicht nochmal bearbeitet wird in der synUSBzuC
		try:
			ItemsOnUSB.remove(itemPfadOnUSB)
			usbTimes[itemPfadOnUSB] = 0
		except ValueError:
			pass

	print("")
	return ItemsOnUSB

def bewegeDateiVon(start, ziel):
	system("cp -f {0} {1}".format(start, ziel))


def synUSBzuC(ItemsOnUSB, cTimes, usbTimes):
	print("\033[93m \033[4m ***** \033[95mSynchronisere neue Dateien von USB\033[93m *****\033[0m")

	for item in ItemsOnUSB:
		#Gibt es diese Datei auch auf C:

		treeItems = item.split("/")
		unterOrdnerName = treeItems[len(treeItems) - 2]
		fileName =  treeItems[len(treeItems) - 1]

		if unterOrdnerName == OrdnerName:
			itemPfadOnC = PathOnC  + OrdnerName + "/" + fileName

			#Vergleichen welche Datei älter ist
			if  usbTimes[item] > cTimes.get(itemPfadOnC, 0):
				print(" ** \033[93m \033[01m Sync " + str(fileName) + " von USB zu C ! \033[0m")
				bewegeDateiVon(item, itemPfadOnC)

			elif usbTimes[item] == cTimes.get(itemPfadOnC, 0):
				print(" ** \033[92m \033[01m Datei " + str(fileName) + " ist auf beiden aktuell ! \033[0m")

			else:
				print(" ** \033[93m \033[01m Sync " + str(fileName) + " von C zu USB! \033[0m")
				bewegeDateiVon(itemPfadOnC, item)

		else:
			itemPfadOnC = PathOnC + OrdnerName + "/" + unterOrdnerName + "/" + fileName
			if path.lexists(PathOnC + OrdnerName + "/" + unterOrdnerName + "/"):
				#Ordner existiert in C -> Vergleichen welche Datei älter ist

				if usbTimes[item] > cTimes.get(itemPfadOnC, 0):
					print(" ** \033[93m \033[01m Sync " + str(unterOrdnerName) + "/"+ str(fileName) + " von USB zu C ! \033[0m")
					bewegeDateiVon(item, itemPfadOnC)

				elif usbTimes[item] == cTimes.get(itemPfadOnC, 0):
					print(" ** \033[92m \033[01m Datei " + str(unterOrdnerName) + "/" + str(fileName) + " ist auf beiden aktuell ! \033[0m")

				else:
					print(" ** \033[93m \033[01m Sync " + str(unterOrdnerName) + "/" + str(fileName) + " von C zu USB! \033[0m")
					bewegeDateiVon(itemPfadOnC, item)

			else:
				#Der Ordner existiert nicht auf C -> erstellen und Datei kopieren
				system("mkdir " + PathOnC + OrdnerName + "/" + unterOrdnerName + "/")
				print(" ** \033[93m \033[01m Sync " + str(fileName) + " von USB zu C ! \033[0m")
				bewegeDateiVon(item, itemPfadOnC)

	if len(ItemsOnUSB) == 0:
		print(" ** Keine da 🤷")
backupErstellen()
iC, iUSB = dateinIndexieren()
mC, mUSB = mtimeGenerieren(iC, iUSB)
iUSB = synCzuUSB(iC, iUSB, mC, mUSB)
synUSBzuC(iUSB, mC, mUSB)