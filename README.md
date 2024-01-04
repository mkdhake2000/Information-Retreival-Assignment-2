# **Assignment Submission by Mandar Dhake (21111405-mkdhake21@iitk.ac.in)**

This assignment contains 4 code files, 7 sub-folders, and 1 Makefile.

To run the entire assignment, use the command:

```bash
>> make run
```


## **Dependencies:**
This assignment requires the following packages or libraries to be installed:
1. pandas
2. numpy
3. gensim
4. os
5. collections
6. pickle
7. matplotlib
8. re

## **Q1=>**
### **Input:**
In order to run the Q1 Python script, please run the script from the directory containing the `hi` folder (i.e., the dataset required for Q1). The command to split the dataset:
```bash
split -l 6500000 hi.txt
```
The `hi` folder contains the folders `50` and `100` containing the model names and their data. The Word Similarity dataset is provided with this zip.

### **Output:**
The output of Q1 is stored in the `Q1Output` folder with folder names for appropriate models.

## **Q2=>**
### **Input:**
The `NER_Datasets` folder contains the given dataset that needs to be preprocessed.

### **Output:**
The data after preprocessing is stored in the `NER-CSV` folder.

## **Q3=>**
### **Input:**
The Q3 input file is split into 127 files from the command line since it is over 20GB in size. Please provide the path to the main directory containing these files. The `Q3-preproc` Python notebook pre-processes these files and returns the pickle files. To run these, execute all the cells of the Python notebook named `Q3-preproc.ipynb` and enter the appropriate path to the files as required. Pre-processing is already done, and pickle files for respective outputs are generated and provided with this. Pickle files are present in the `Q3PKL` folder. The `Q3-main` Python script processes these pickle files and returns the top 100 of required entities and the plots.

### **Output:**
The output of Q3 is stored in the `Q3Output` folder. The text files containing these top 100 are stored in `Q3OutputTexts` folder. The plots are stored in `Q3OutputPlots` folder. From the plots, we can see that this follows a Zipfian Distribution.

## **Code Files=>**
1. `Q1.py`: Runs Q1 completely.
2. `Q2.py`: Runs Q2 preprocessing.
3. `Q3-preproc.ipynb`: Runs Q3 preprocessing.
4. `Q3-main.py`: Runs Q3 important code.

After extracting the zip, switch to this directory and then enter the head command mentioned above to run the codes.

The main zip contains 3 Python scripts (.py) for each question and one Python notebook (.ipynb) for preprocessing of Q3.

All the codes are well-documented for better understanding.
