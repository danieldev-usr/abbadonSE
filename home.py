#import
import os
import time
#cores
RED='\033[0;31m'
HEADER='\033[95m'
OKBLUE='\033[94m'
OKGREEN='\033[92m'
WARNING='\033[93m'
FAIL='\033[91m'
BOLD='\033[1m'
UNDERLINE='\033[4m'
ENDC='\033[0m'
#entrada
def cls():os.system("clear")
print(OKBLUE + "Produced by wan...")
time.sleep(0.5)
print("Free...")
time.sleep(0.5)
print("Welcome!")
time.sleep(0.5)
cls()
#banner
bnn = open('textbanner.txt', 'r')
bn = bnn.read()
print(RED + bn)
print(OKBLUE + "Não me responsabilizo por" + RED + " seus atos")
print(OKBLUE + "Created by Wan" + RED +" 10/27/22")
print(OKBLUE + "Python Lang -" + RED + " Educação")
print(" ")
print(OKGREEN + '#'*15 + " ENGENHARIA SOCIAL " + "#"*15)
print(f""" {WARNING}
--------------------------------------------------
-[0] Help / Erros                                -
-[1] Dicas para melhorar linguagem corporal      -
-[2] Microexpressão - Evitar/Detectar mentiras   -
-[3] A arte de enganar - Seja persuasivo         -
-[4] Importancia da engenharia social no hacking -
-[5] Hardware Hacking ferramentas (especial)     -
--------------------------------------------------
""")
print(" ")
#codigo
while True:
	x = input(">>> ")
	
	if x == "clear":
		cls()
		
	elif x == "1":
		print(" ")
		lngc = open('dicaslangcorp.txt', "r")
		abln = lngc.read()
		print(HEADER + abln)
		print(" ")
		
	elif x == "2":
		print(" ")
		absp = open('micro.txt', 'r')
		sps = absp.read()
		print(HEADER + sps)
		print(" ")
		
	elif x == "3":
		print(" ")
		ss = open("persu.txt", "r")
		ssa = ss.read()
		print(HEADER + ssa)
		print(" ")
		
	elif x == "4":
		print(" ")
		imp = open('imp.txt', 'r')
		impopn = imp.read()
		print(HEADER + impopn)
		print(" ")
		
	elif x == "5":
		print(" ")
		asx = open("hardware.txt", "r")
		asxc = asx.read()
		print(HEADER + asxc)
		print(" ")
		
	elif x == "0":
		print(f""" {OKBLUE}
	 	-?-?-?-?-?-?-?-?-?-?-?-?-?-?-?-?
	 	-?Telegram - @BaalZevuv6      -?
	 	-?Instagram - @metalheadkkkk  -?
	 	-?Comandos internos ->        -?
	 	-?'clear'                     -?
	 	-?'exit'                      -?
	 	-?-?-?-?-?-?-?-?-?-?-?-?-?-?-?-?
		""" + WARNING)
		
	elif x == "exit":
		exit()
		
	else:
		print(f"'{x}' não existe...")