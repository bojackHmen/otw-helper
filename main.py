#!usr/bin/env python
import subprocess

print("OverTheWire CTF helper v1 - bojxk")

lvl = input("Enter Level: ")
key = input("Enter Key: ")

f = open(f"lvl{lvl}", "w")
f.write(key)
f.close()

subprocess.call(f"sshpass -p `cat lvl{lvl}` ssh bandit{lvl}@bandit.labs.overthewire.org -p 2220",shell=True)
