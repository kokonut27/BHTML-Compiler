import os, sys, time, re
from flask import Flask


fp = input('FilePath: ')
if '.bhtml' in fp:
  pass
else:
  raise Exception("The file is not a 'bhtml' file")
try:
  f = open(fp,'r')
except:
  raise Exception("There is no such file")

content = f.read()
colist = content.split("\n")
'''
load = 0
for i in colist:
  if i:
    load+=1
'''

os.system('clear')
while True:
  inp = input('> ')
  if inp == 'run':
    while " " in inp:
      inp = inp.replace(" ","")
    if inp == 'run':
      break
  elif inp == 'run-project':
    while " " in inp:
      inp = inp.replace(" ","")
    if inp == 'run-project':
      break
  elif inp == 'bhtml index.bhtml':
    while " " in inp:
      inp = inp.replace(" ","")
    if inp == 'bhtml index.bhtml':
      break
  elif inp == 'index.bhtml':
    while " " in inp:
      inp = inp.replace(" ","")
    if inp == 'index.bhtml':
      break
  else:
    os.system(str(inp))

'''
num=0
while num < load:
  print("Compiling... |")
  time.sleep(0.08)
  os.system('clear')
  print("Compiling... \ ")
  time.sleep(0.08)
  os.system('clear')
  print("Compiling... -")
  time.sleep(0.08)
  os.system('clear')
  print("Compiling... |")
  time.sleep(0.08)
  os.system('clear')
  print('Compiling... /')
  time.sleep(0.08)
  os.system('clear')
  num+=1
'''

def check():
    df = re.findall("(?<=[AZaz])?(?!\d*=)[0-9.+-]+", lines)
    df = str(df)

def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
  mustend = time.time() + timeout
  while time.time() < mustend:
    if somepredicate(*args, **kwargs): return True
    time.sleep(period)
  return False

allvars = {}
line = 0
read_line=0
getChar1 = "none"
getChar2 = "none"
getChar3 = "none"
var1 = "Undefined variable"
input1 = "Undefined input"
input2 = "Undefined input"
input3 = "Undefined input"

def pTAG():
  try:
    if '</p>' in lines:
      wrd = '<p>'
      res = lines.partition(wrd)[2]
      res = res.replace('</p>', '')
      #res = res.replace(' ', '')
      res = res.replace('{getChar1}', getChar1)
      res = res.replace('{getChar2}', getChar2)
      res = res.replace('{getChar3}', getChar3)
      res = res.replace("{{input1}}", input1)
      res = res.replace("{{input2}}", input2)
      res = res.replace("{{input3}}", input3)
      res = res.replace("{{var1}}", var1)

      if "{{" in res:
        if "}}" in res:
          start = "{{"
          end = "}}"
          check = res[res.find(start) + len(start):res.rfind(end)]
          
          if check in allvars:
            res = res.replace('{{','')
            res = res.replace('}}','')
            e = allvars[check]
            res = res.replace(check, str(e))
          else:
            exit()#add error
      
      split_string = res.split("</p>", -1)
      res = split_string[0]
      print(res)
    
    else:
      exit()
  except:
    exit()

def h1TAG():
  pass



newvar = 0
file = open(fp)
readline2 = 0
for lines in file.readlines():
  if "<!--" in lines:
    wait_until("-->", 0)
    readline2=1
  if readline2 == 1:
    continue
  
  line+=1
  lines = lines.replace('\n','')
  lines = lines.replace('\t','')

  if lines == '': 
    pass
  elif "<!--" in lines:
    wait_until("-->", 0)
    pass
  lines = lines.rstrip()

  if "<p>" in lines:
    pTAG()

while True:#if this runs, the program in index.bhtml successfully ran
  inp = input('> ')
  os.system(str(inp))