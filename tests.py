#!/usr/bin/python3

import subprocess, sys, tempfile

tests = [
  [b"p\x19\x88\x8a\xf35b_", "3", b"\\\\\\o///\n"],
  [b"from math import factorial as F#\ntry:n=int(i)-1;print(n*(F(n)%-~n==n))\nexcept:print(sum(map(int,i.split())))", "5", b"4\n"],
  [b"lZ!\x841\xfcv\xba\x04\xac\xe0", "hgfd", b"gack\n\n"]
]

interpreter_path = "python3"

failures = 0

for test in enumerate(tests):
  try:
    temp = tempfile.NamedTemporaryFile()
    temp.write(test[1][0])
    temp.flush()
    result = subprocess.check_output("python3 cinnamon-gum.py %s <<< '%s'" % (temp.name, test[1][1]), shell=True, executable="/bin/bash")
    if result == test[1][2]:
      pass
    else:
      failures += 1
      print("Test " + str(test[0] + 1) + " " + str(test[1][0]) +" failed (incorrect output %s)\n" % result)
  except Exception as e:
    failures += 1
    print("Test " + str(test[0] + 1) + " " + str(test[1][0]) +" failed (exception %s)\n" % e)

if failures:
  sys.exit(1)
else:
  sys.exit(0)
