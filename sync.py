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

