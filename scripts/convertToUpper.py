import os
import sys

fileToConvert = sys.argv[1]

inputFile = open(fileToConvert, "r")
content = inputFile.read()
with open(fileToConvert, "wb") as outputFile:
	outputFile.write(content.upper())
