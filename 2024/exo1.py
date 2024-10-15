#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))


for line in lines[1:]:
    
    if line[:2] == "42" and sum(map(int, list(line))) == 75 :
        print(line)
        break
    
        