import os, sys
os.system("git pull")
try:
    __import__("GREEN").menu_a()
except Exception as e:
    exit(str(e))
  
