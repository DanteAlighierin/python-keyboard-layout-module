#!/usr/bin/env python
import commands
layout= commands.getoutput("xset -q|grep LED| awk '{ print $10 }' ")
if layout == '00000002':
  print ("en")
if layout=='00001006':
  print ("ru")