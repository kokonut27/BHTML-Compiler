import os, sys, time, re
import string


fp = input('FilePath: ')

def parse(file):
  print("i started parsing!!!")
  if '.bhtml' in file:
    pass
  else:
    raise Exception("The file is not a 'bhtml' file")
  try:
    f = open(file,'r')
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

  def docTAG():
    try:
      if '<!DOCTYPE bhtml>' in lines:#this way is more recommended
        bhtmldoc = True
      elif '<!doctype bhtml>' in lines:
        bhtmldoc = True
      elif '<!doctype BHTML>' in lines:
        bhtmldoc = True
      elif '<!DOCTYPE BHTML>' in lines:
        bhtmldoc = True
      else:
        pass
    except:
      pass

  def aTAG():
    try:
      #lines = lines.replace(' ','') PUT DELETE SPACES FUNCTION HERE
      if ('<a href = "' in lines):
          wrd = '<a href = "'
          res = lines.partition(wrd)[2]
          split_string = res.split("\">", 1)
          res = split_string[0]
          print(res) # been doing too much js
          #print(lines)
          os.system(f"touch {res}.bhtml") # creates file
          ee = lines.partition(f'<a href = "{res}">')
          f = ee[2]
          f = str(f)
          f = f.replace('</a>','')
          #print(f)
         # try:
          
          
          #except:
           # raise Exception("ERROR")
          print("BEFORE")
          print(res)
          #parse(f"{res}.bhtml")
          print("AFTER")
          # code here, it means it passed with href tag
      elif ('<a id = "'):
        pass
      
      else:
        pass
    except:
      raise Exception("ERROR")

  def pTAG():
    try:
        if '</p>' in lines:#maybe replace </p> with </>?
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

          wait_until("</p>", 0)
          split_string = res.split("</p>", -1)
          res = split_string[0]
          print(res)
        else:
          pass
    except:
      raise Exception("ERROR")

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

    if "</p>" in lines:
      pTAG()

    if "<a href" in lines:
      aTAG()



    elif lines in string.whitespace:#i might remove this
      pass
    
    elif type(lines) == str:#if the code inside index.bhtml is string, it prints, like regular html
      print(str(lines))

parse(fp)