PYTHON = python3

# Defining an array variable
FILES = input output

# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To run all the models type make run"
	@echo "------------------------------------"

# The ${} notation is specific to the make syntax and is very similar to bash's $()
run:
	@pip install gensim
	@pip install matplotlib
	@pip install pandas
	@pip install numpy
	@pip install pickle-mixin
	@echo 'Running Q1.py'
	@${PYTHON} Q1.py
	@echo 'Q1 done successfully. Check Output in 'Q1Output' folder'
	@echo 'Running Q2.py'
	@${PYTHON} Q2.py
	@echo 'Q2 done successfully. Check Output in 'NER-CSV' folder'
	@echo 'Running Q3-main.py'
	@${PYTHON} Q3-main.py
	@echo 'Q3 done successfully. Check Output in 'Q3OutputTexts' and 'Q3OutputPlots' folder'

