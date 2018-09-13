#!/bin/bash
PYENV_HOME=$WORKSPACE/.venv

if [ ! -d ".venv" ]; then
	virtualenv -p python3 $PYENV_HOME
fi
cd $WORKSPACE
. ./.venv/bin/activate

echo "Virtualenv activated"
pip --version
pip install nosexcover
pip install pylint
echo "Installed default requirements"
pip3 install -r $WORKSPACE/requirements.txt
echo "Installed user requirements."
export PYTHONPATH=$WORKSPACE

nosetests --cover-inclusive --with-xcoverage --with-xunit --cover-erase --cover-package=engine,ui,bin
pylint -f parseable freesm/ --ignore=lib,bin,venv | tee pylint.out
