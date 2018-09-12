#!/bin/bash
PYENV_HOME=$WORKSPACE/.venv
#if [ -d $PYENV_HOME ]; then
#    rm -rf $PYENV_HOME
#fi

#PATH=$WORKSPACE/.venv/bin:/usr/local/bin:$PATH
if [ ! -d ".venv" ]; then
	virtualenv -p python3 $PYENV_HOME
fi
#source $PYENV_HOME/bin/activate
cd $WORKSPACE
. ./.venv/bin/activate

echo "Virtualenv activated"
pip --version
pip install nosexcover
pip install pylint
echo "Installed default requirements"
# pip install --quiet $WORKSPACE/  # where your setup.py lives
pip3 install -r $WORKSPACE/requirements.txt
echo "Installed user requirements."
export PYTHONPATH=$WORKSPACE

nosetests --with-xcoverage --with-xunit --cover-package=. --cover-erase
pylint -f parseable freesm/ | tee pylint.out
