This assignment is submitted by Mandar Dhake (21111405-mkdhake21@iitk.ac.in).
This assignment contain 4 code files, 7 sub-folders and 1 Makefile.

To run entire assignment, we have to enter the command:

>> make run

Dependencies:-
This assignment needs following packages or libraries to be installed to run it.
1.pandas
2.numpy
3.gensim
4.os
5.collections
6.pickle
7.matplotlib
8.re

Q1=>
	Input:
		In order to run Q1 python script please run the script from the directory containing the hi folder i.e. the dataset required for Q1.
		The command to split the dataset:
			split -l 6500000 hi.txt
		hi folder has the folders 50,100 containing the model names and their data.
		Word Similarity dataset is provided with this zip.
	Output:
		The output of Q1 is stored in Q1Output folder with folder names for appropriate models.

Q2=>
	Input:
		The NER_Datasets folder contains the given dataset that has to be preprocessed.
	Output:
		The data after preprocessing is stored in NER-CSV folder.

Q3=>
	Input:
		Q3 input file is splitted in 127 files from command line since it is over 20gb in size.
		Please provide the path to the main directory containing these files.
		The Q3-preproc python notebook pre-processes these files and returns the pickle files.
		To run these please run all the cells of the python notebook named Q3-preproc.ipynb and as required enter the appropriate path to the files.
		Pre-processing is already done and pickle files for respective outputs are already generated and provided with this.
		Pickle files are present in the Q3PKL folder.
		The Q3-main python script processes these pickle files and returns the top 100 of required entities and the plots.
	Output:
		The output of Q3 is stored in Q3Output folder.
		The text files containing these top 100 are stored in Q3OutputTexts folder.
		The plots are stored in Q3OutputPlots folder.
		From the plots, We can see that this follows Zipfian Distribution.

Code Files=>
Q1.py:
	Runs Q1 completely.
Q2.py:
	Runs Q2 preprocessing.
Q3-preproc.ipynb:
	Runs Q3 preprocessing.
Q3-main.py:
	Runs Q3 important code.

After extracting the zip switch to this directory and then enter the head command mentioned above to run the codes.

The main zip contains 3 python scripts(.py) for each question and one python notebook(.ipynb) for preprocessing of Q3.

All the codes are documented well for better understanding.