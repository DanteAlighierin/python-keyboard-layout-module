#!/usr/bin/env python3
import subprocess
layout = subprocess.check_output("xset -q|grep LED| awk '{ print $10 }' ", shell=True)
if layout == '00000002':
	print ("en")
if layout=='00001006':
	print ("ru")
