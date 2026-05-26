import sys
from pyfiglet import Figlet
import random

"""
sys.argv is a list of command line arguments
 - sys.argv[0] = file name
 - sys.argv[1] = first argument
 - sys.argv[2] = second argument
 - etc
"""

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
  text = input("Input: ")
  figlet.setFont(font=random.choice(fonts))
  print(figlet.renderText(text))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
  if sys.argv[2] not in fonts:
    sys.exit("Invalid usage")

  text = input("Input: ")
  figlet.setFont(font=sys.argv[2])
  print(figlet.renderText(text))
else:
  sys.exit("Invalid usage")