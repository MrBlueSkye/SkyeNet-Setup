#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print ('''
                        
\033[1;32mStarting SkyeNet-Setup...\033[1;m

                                                                                                                              
 @@@@@@   @@@  @@@  @@@ @@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@              @@@@@@   @@@@@@@@  @@@@@@@  @@@  @@@  @@@@@@@ 
@@@@@@@   @@@  @@@  @@@ @@@  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@@@@             @@@@@@@   @@@@@@@@  @@@@@@@  @@@  @@@  @@@@@@@@
!@@       @@!  !@@  @@! !@@  @@!       @@!@!@@@  @@!         @@!               !@@       @@!         @@!    @@!  @@@  @@!  @@@
!@!       !@!  @!!  !@! @!!  !@!       !@!!@!@!  !@!         !@!               !@!       !@!         !@!    !@!  @!@  !@!  @!@
!!@@!!    @!@@!@!    !@!@!   @!!!:!    @!@ !!@!  @!!!:!      @!!    @!@!@!@!@  !!@@!!    @!!!:!      @!!    @!@  !@!  @!@@!@! 
 !!@!!!   !!@!!!      @!!!   !!!!!:    !@!  !!!  !!!!!:      !!!    !!!@!@!!!   !!@!!!   !!!!!:      !!!    !@!  !!!  !!@!!!  
     !:!  !!: :!!     !!:    !!:       !!:  !!!  !!:         !!:                    !:!  !!:         !!:    !!:  !!!  !!:     
    !:!   :!:  !:!    :!:    :!:       :!:  !:!  :!:         :!:                   !:!   :!:         :!:    :!:  !:!  :!:     
:::: ::    ::  :::     ::     :: ::::   ::   ::   :: ::::     ::               :::: ::    :: ::::     ::    ::::: ::   ::     
:: : :     :   :::     :     : :: ::   ::    :   : :: ::      :                :: : :    : :: ::      :      : :  :    :      
                                                                                                                              

\033[1;91mRun as root to enable package installations!\033[1;m
		''')
		def inicio1():
			while True:
				print ('''
1) View Categories
2) Something cool (Essentially a placeholder option)
3) Help

			''')

				opcion0 = raw_input("\033[1;36mSkyeNet-Setup# \033[1;m")

				if opcion0 == "2"	:
					placeholderoption = raw_input("\033[1;32mDo you want to see something cool? [y/n]> \033[1;m")
					if placeholderoption == "y":
						cmd1 = os.system("apt install sl && sl")
				elif opcion0 == "3":
					print (''' 
****************** +Commands+ ******************


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mReturn to the Main Menu\033[1;m

\033[1;32mCTRL+c\033[1;m	\033[1;33mExit Installer\033[1;m

		''')


				def inicio():
					while opcion0 == "1":
						print ('''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Personalization
2) Utilities
3) NetSec
4) Games and Media

			 ''')
						print ("\033[1;32mSelect a category. Use 'back' to go back.\n\033[1;m")

						opcion1 = raw_input("\033[1;36mSkyeNet-Setup# \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						while opcion1 == "1":
							print ('''
\033[1;36m=+[ Personalization\033[1;m

 
 1) KDE
 2) Numix Icons
 3) Ranger
 4) VIM
 5) Guake Terminal

 0) Install all items
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it. Use 'back' to go back one page.\n\033[1;m")
							opcion2 = raw_input("\033[1;36mSkyeNet-Setup# \033[1;m")
							if opcion2 == "1":
                                                                cmd = os.system("add-apt-repository ppa:kubuntu-ppa/ppa")
                                                                cmd = os.system("apt update")
								cmd = os.system("apt install kubuntu-desktop")
							elif opcion2 == "2":
                                                                cmd = os.system("add-apt-repository ppa:numix/ppa")
								cmd = os.system("apt install numix-icon-theme-circle")
							elif opcion2 == "3":
								cmd = os.system("apt install ranger")
							elif opcion2 == "4":
								cmd = os.system("apt install vim")
							elif opcion2 == "5":
								cmd = os.system("apt install guake")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
                                                                cmd = os.system("add-apt-repository ppa:numix/ppa")
                                                                cmd = os.system("add-apt-repository ppa:kubuntu-ppa/ppa")
                                                                cmd = os.system("apt update")
								cmd = os.system("apt install kubuntu-desktop numix-icon-theme-circl ranger vim guake")				
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")


						while opcion1 == "2":
							print ('''
\033[1;36m=+[ Utilities\033[1;m

 1) Git
 2) Pip
 3) Python v2
 4) Python v3

 0) Install all items
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it. Use 'back' to go back one page.\n\033[1;m")
							opcion2 = raw_input("\033[1;36mSkyeNet-Setup# \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install git")
							elif opcion2 == "2":
								cmd = os.system("apt install pip")
							elif opcion2 == "3":
								cmd = os.system("apt install python")
							elif opcion2 == "4":
								cmd = os.system("apt install python3")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt install git pip python python3")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "3":
							print ('''
\033[1;36m=+[ NetSec\033[1;m

 1) NMAP
 2) Wifite
 3) Kismet
 4) Airmon-NG
 5) WHOIS
 6) NetDiscover
 7) HashCat
 8) ngrep
 9) WireShark
 10) MDK3
 11) MacChanger

 0) Install all items
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it. Use 'back' to go back one page.\n\033[1;m")
							opcion2 = raw_input("\033[1;36mSkyeNet-Setup# \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install nmap")
							elif opcion2 == "2":
								cmd = os.system("apt install wifite")
							elif opcion2 == "3":
								cmd = os.system("apt install kismet")
							elif opcion2 == "4":
								cmd = os.system("apt install airmon-ng")
							elif opcion2 == "5":
								cmd = os.system("apt install whois")
							elif opcion2 == "6":
								cmd = os.system("apt install netdiscover")
							elif opcion2 == "7":
								cmd = os.system("apt install hashcat")
							elif opcion2 == "8":
								cmd = os.system("apt install ngrep")
							elif opcion2 == "9":
								cmd = os.system("apt install wireshark")
							elif opcion2 == "10":
								cmd = os.system("apt install mdk3")
							elif opcion2 == "11":
								cmd = os.system("apt install macchanger")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt install nmap kismet wifite airmon-ng whois netdiscover hashcat ngrep wireshark mdk3 macchanger")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

						while opcion1 == "4":
							print ('''
\033[1;36m=+[ Games and Media\033[1;m

 1) Super Tux Kart
 2) Alien Arena
 3) Xonotic
 4) Blender
 5) GIMP

 0) Install all items
				 
						''')
							print ("\033[1;32mInsert the number of the tool to install it. Use 'back' to go back one page.\n\033[1;m")
							opcion2 = raw_input("\033[1;36mSkyeNet-Setup# \033[1;m")
							if opcion2 == "1":
								cmd = os.system("apt install supertuxkart")
							elif opcion2 == "2":
								cmd = os.system("apt install alien-arena")
							elif opcion2 == "3":
								cmd = os.system("apt install xonotic")
							elif opcion2 == "4":
								cmd = os.system("apt install blender")
							elif opcion2 == "5":
								cmd = os.system("apt install gimp")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
					                    installallgamesoption = raw_input("\033[1;31mPftt - Install all Games? Are you serious? [y/n]> \033[1;m")
                        				    if installallgamesoption == "y":
						        	print ("\033[1;31mAlright then.\033[1;m")
								cmd = os.system("apt install supertuxkart alien-arena xonotic blender gimp")						
							else:
								print ("\033[1;31mSorry, that was an invalid command!\033[1;m")

								inicio1()

				inicio()
		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
