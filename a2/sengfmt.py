#!/usr/bin/env python3 

# File: sengfmt.py 
# Student Name  :David Wiebe
# Student Number: V00875342
# SENG 265 - Assignment 2

import argparse
import sys
	
def main():
	in_text = open(sys.argv[1], "r")
	out_text = ""
	buff = ""
	tok = ""
	temp = ""
	temp2 = ""
	wid = 10000
	marg = 0
	cap = False
	fmt = False
	buff = in_text.readline()
	while buff:
		temp = buff.split(" ")
		if temp[0] == "?maxwidth":
			if "+" in temp[1]:
				temp[1] = temp[1].strip(" +\n")
				wid = wid + int(temp[1])
			elif "-" in temp[1]:
				temp[1] = temp[1].strip(" -\n")
				wid = wid - int(temp[1])
			else:
				wid = int(temp[1])
				fmt = True
			if wid < 20:
				wid = 20
		elif temp[0] == "?mrgn":
			if "+" in temp[1]:
				temp[1] = temp[1].strip(' +\n')
				marg = marg + int(temp[1])
			elif "-"  in temp[1]:
				temp[1] = temp[1].strip(' -\n')
				marg = marg - int(temp[1])
			else:
				marg = int(temp[1])
			if marg < 0:
				marg = 0
			elif marg > wid - 20:
				marg = wid - 20
			fmt = True
		elif temp[0] == "?fmt":
			if temp[1] == "on\n":
				fmt = True
			elif temp[1] == "off\n":
				fmt = False
		elif temp[0] == "?cap":
			if temp[1] == "on":
				cap == True
			else:
				cap = False
		elif fmt == False:
			out_text = out_text + buff
		elif wid == 10000:
			if buff == "\n":
				out_text = out_text + "\n"
			else:
				temp2 = ""
				for i in range (0, marg):
					temp2 = temp2 + " "
				out_text = out_text + temp2 + buff
		elif temp[0] == "\n":
			if wid != 10000:
				temp2 = justify(temp2.strip(" \n"), wid, marg)
			if cap == True:
				temp2 = temp2.upper()
			out_text = out_text + temp2 + "\n\n"
			temp2 = ""
		else:
			for x in temp:
				if len(temp2) == 0:
					for i in range (0, marg):
						temp2 = temp2 + " "
				if len(temp2.rstrip(" \n")) + len(x.strip(" \n")) < wid:
					if len(temp2) == marg:
						temp2 = temp2 + x.strip(" \n")
					else:
						temp2 = temp2 + " " + x.strip(" \n")
				else:
					if wid != 10000:
						temp2 = justify(temp2.strip(" \n"), wid, marg)
					if cap == True:
						temp2 = temp2.upper()
					out_text = out_text + temp2 + "\n"
					temp2 = ""
					for i in range(0, marg):
						temp2 = temp2 + " "
					temp2 = temp2 + x.strip(" \n")
		buff = in_text.readline()		
	if len(temp2) > marg:
		if cap == True:
			temp2 = temp2.upper()
		if wid != 10000:
			temp2 = justify(temp2.strip(" \n"), wid, marg)
		out_text = out_text + temp2
	out_text = out_text.rstrip('\n')
	print(out_text)



def justify(text, wid, marg):
	temp = text.split(" ")
	if len(temp) == 1:
		for x in range(0, marg):
			text = " " + text
		return text
	text = ""
	for x in range(0, marg):
		text = text + " "
	length = marg
	for x in temp:
		length += len(x)
	i = 0
	while length < wid:
		temp[i] = temp[i] +  " "
		i += 1
		length += 1
		if i >= len(temp) - 1:
			i = 0
	for x in temp:
		text = text + x
	return text



if __name__ == "__main__": 
	main() 
