import sys
import re
import itertools


def readFile(inFileName):
	f = open(inFileName);
	lines = f.readlines()
	f.close()
	return lines;

def createArraysForFile(linesFile):
	posArray =  [];
	negArray =  [];
	for line in linesFile:
		idAndPat = line.split();
		firstPart = idAndPat[0];
		(counter, patID) = firstPart.split(",")
		if patID == "+1":
			posArray.append(line);
		elif patID == "-1":
			negArray.append(line);
		else:
			print "Invalid line: " + line;
	return posArray, negArray;

def updateIds(startIdx, arrToUpdate):
	updatedArray = []
	for item in arrToUpdate:
		(id, line) = item.split(",");
		newIdx = int(startIdx) + int(id);
		item = str(newIdx) + "," + line;
		updatedArray.append(item);
	return updatedArray;

def updateNegIds(startIdx, arrToUpdate):
	updatedArray = []
	newIdx = startIdx;
	for item in arrToUpdate:
		(id, line) = item.split(",");
		newIdx = newIdx + 1;
		item = str(newIdx) + "," + line;
		updatedArray.append(item);
	return updatedArray;

def combinePosArray(p1, p2, p3, p4):
	indexToStart = len(p1);
	print "Index to Start: " + str(indexToStart);
	updatedP2 = updateIds(indexToStart, p2);
	indexToStart = indexToStart + len(updatedP2);

	updatedP3 = updateIds(indexToStart, p3);
	indexToStart = indexToStart + len(updatedP3);

	updatedP4 = updateIds(indexToStart, p4);

	finalPos = [];
	finalPos = p1 + updatedP2 + updatedP3 + updatedP4;
	return finalPos;

def combineNegArray(n1, n2, n3, n4, negStartId):
	indexToStart = negStartId - 1;
	print "Index to Start: " + str(indexToStart);
	updatedN1 = updateNegIds(indexToStart, n1);

	indexToStart = indexToStart + len(n1);
	updatedN2 = updateNegIds(indexToStart, n2);

	indexToStart = indexToStart + len(updatedN2);
	updatedN3 = updateNegIds(indexToStart, n3);

	indexToStart = indexToStart + len(updatedN2);
	updatedN4 = updateNegIds(indexToStart, n4);

	print "Index to Start: " + str(indexToStart);

	finalNeg = updatedN1 + updatedN2 + updatedN3 + updatedN4;
	return finalNeg;

#'TATTTCC:0.136082763488'
def parseLines(linesFile1, linesFile2, linesFile3, linesFile4):
	p1, n1 = createArraysForFile(linesFile1);
	p2, n2 = createArraysForFile(linesFile2);
	p3, n3 = createArraysForFile(linesFile3);
	p4, n4 = createArraysForFile(linesFile4);

	finalPos = combinePosArray(p1, p2, p3, p4);
	negStartId = len(finalPos);
	finalNeg = combineNegArray(n1, n2, n3, n4, negStartId);

	return finalPos, finalNeg;

def writeDataToFile(data, outputFile):
	outFile = open(outputFile , "w")
	for item in data:
		outFile.write(item);
	outFile.close();

def combinePosNegFiles(posFileName, negFileName, combinedFileName):
	filenames = [posFileName, negFileName];
	with open(combinedFileName, 'w') as outfile:
		for fname in filenames: 
			with open(fname) as infile: 
				for line in infile: 
					outfile.write(line)

## Program starts here.
## Input is HuR and TTP data files with k-mers.
def generateCombinedModel(HuR_Train_Features_File, TTP_Train_Features_File, 
	HuR_TTP_Combined_Features_File):
	
	linesFile1 = ""
	linesFile2 = ""

	if HuR_Train_Features_File != None:
		linesFile1 = readFile(HuR_Train_Features_File);
  

	if TTP_Train_Features_File != None:	
		linesFile2 = readFile(TTP_Train_Features_File);
   
	combinedFeatureFName = HuR_TTP_Combined_Features_File;

	linesFile3 = []; 
	linesFile4 = [];

	posFileName = "posFeatures.txt";
	negFileName = "negFeatures.txt";


	posArray, negArray = parseLines(linesFile1, linesFile2, linesFile3, linesFile4);
	writeDataToFile(posArray, posFileName);
	writeDataToFile(negArray, negFileName);
	combinePosNegFiles(posFileName, negFileName, combinedFeatureFName);
