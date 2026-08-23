#!/usr/bin/env bash
# Setup
venvdir='~/.venvs/py3-12'
if [[ -d $venvdir ]]; then
	python3.12 -m venv $venvdir
	source ~/.venvs/py3-12/bin/activate
	pip install -r requirements.txt
else
	source ~/.venvs/py3-12/bin/activate
fi

# Run each stage
if [[ "$(python --version)" == *' 3.12'* ]]; then
	stages=(
		exploratory_dataset_analysis.py
		train-supervised.py
		train-unsupervised.py
		train-deeplearning.py
		summary-generation.py
	)
	for pyfile in "${stages[@]}"; do
		if [[ -f "${pyfile}" ]]; then
			echo "RUNNING: ${pyfile}"
			python3.12 "${pyfile}"
		else
			echo "!!!!ISSUE!!!!!"
			echo "Missing expected stage: ${pyfile:-UNKNOWN}"
			echo "!!!!ISSUE!!!!!"
			break
		fi
	done
else
	echo "!!!!ISSUE!!!!!"
	echo "Python Version incorrect: please use Python 3.12"
	echo "!!!!ISSUE!!!!!"
fi
