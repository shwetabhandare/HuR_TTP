import sys


def readFile(inFileName):
	f = open(inFileName);
	lines = f.readlines()
	f.close()
	return lines;

def writeDataToFile(data, outputFile):
	outFile = open(outputFile , "w")
	for item in data:
		outFile.write(item);
		outFile.write("\n")
	outFile.close();

def parseLines(prefix, lines):
   vectorPrime =  [];
   for line in lines: 
      info = line.split(); 
      newLine = "";
      newLine = info[0] + " ";

      for i in range(1, len(info)):

         kmer,score = info[i].split(":");
         prefix_kmer = prefix + "_" + kmer;
         newLine = newLine + kmer + ":" + score + " " + prefix_kmer + ":" + score + " "

      newLine = newLine + prefix + ":1"
      #newLine = newLine[:-1]
      vectorPrime.append(newLine);
   return vectorPrime;

def createPrimeFeatures(lines, prefix, outputFile):

   vectorPrime = parseLines(prefix, lines);
   writeDataToFile(vectorPrime, outputFile);
