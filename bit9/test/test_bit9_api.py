#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Josh Maine'


# Example Usage #############################################################################
# repper = Bit9Api()

# Win 7 SP1 - calc.exe [ md5:60B7C0FEAD45F2066E5B805A91F4F0FC ]
calc_exe_md5 = "a31691f0078652207ea0b463342b464f"
notepad_exe_md5 = "5e28284f9b5f9097640d58a73d38ad4c"

# Bit9 Basic
#print colorama.Back.BLUE + colorama.Fore.BLACK + ":::::::: What is our Usage? ::::::::" + colorama.Style.RESET_ALL
#repper.lookup_usageinfos()
#print colorama.Back.BLUE + colorama.Fore.BLACK + "::::::: Tell Me All You Know :::::::" + colorama.Style.RESET_ALL

# out = repper.lookup_md5(calc_exe_md5)
#print colorama.Back.BLUE + colorama.Fore.BLACK + ":::::::: Trust Level? ::::::::" + colorama.Style.RESET_ALL
##decrip = out.json()['hashinfo']['peheadermetadata']['description']
#print colorama.Fore.GREEN + colorama.Style.BRIGHT + "\t" + out.json()['hashinfo']['trust'] + colorama.Style.RESET_ALL
#
#out = repper.lookup_md5(notepad_exe_md5)
## Example of how to print out specific info
#if out.status_code == requests.codes.ok:
#    print colorama.Back.BLUE + colorama.Fore.BLACK + ":::::::: What is this file? ::::::::" + colorama.Style.RESET_ALL
#    decrip = out.json()['hashinfo']['peheadermetadata']['description']
#    print colorama.Fore.GREEN + colorama.Style.BRIGHT + "\t" + decrip + colorama.Style.RESET_ALL

# Try a bad hash
# repper.lookup_md5("60B7C0FEAD45F2066E5B805A91F4F0FD")

# Bit9 Extended
# repper.lookup_scanresults(calc_exe_md5)
# repper.lookup_certificates(calc_exe_md5)
# repper.lookup_files(calc_exe_md5)
# repper.lookup_packages(calc_exe_md5)