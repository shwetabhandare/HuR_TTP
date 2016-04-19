import createPrefixFeatures
import combineFeatureVectors
import sys

HuRLines = ""
TTPLines = ""
# Program starts here.
if sys.argv[1] != "":
	HuRLines = createPrefixFeatures.readFile(sys.argv[1]);
	HuRPrefix = sys.argv[2]
	HuROutputFile = sys.argv[3];

if sys.argv[4] != "":
	TTPLines = createPrefixFeatures.readFile(sys.argv[4]);
	TTPPrefix = sys.argv[5]
	TTPOutputFile = sys.argv[6];

CombinedFile = sys.argv[7];

if HuRLines != "":
	createPrefixFeatures.createPrimeFeatures(HuRLines, HuRPrefix, HuROutputFile);

if TTPLines != "":
	createPrefixFeatures.createPrimeFeatures(TTPLines, TTPPrefix, TTPOutputFile);

if HuRLines != "" and TTPLines != "":
	combineFeatureVectors.generateCombinedModel(HuROutputFile, TTPOutputFile, CombinedFile);

if HuRLines == "":
	combineFeatureVectors.generateCombinedModel(None, TTPOutputFile, CombinedFile);

if TTPLines == "":
	combineFeatureVectors.generateCombinedModel(HuROutputFile, None, CombinedFile);	
