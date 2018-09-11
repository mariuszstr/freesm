#/bin/bash
PYENV_HOME=$WORKSPACE/.venv
#if [ -d $PYENV_HOME ]; then
#    rm -rf $PYENV_HOME
#fi

PATH=$WORKSPACE/.venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv" ]; then
	virtualenv -p python3 $PYENV_HOME
fi
. venv/bin/activate

echo "Virtualenv activated"
pip --version
pip install --quiet nosexcover
pip install --quiet pylint
echo "Installed default requirements"
# pip install --quiet $WORKSPACE/  # where your setup.py lives
pip install $WORKSPACE/requirements.txt
echo "Installed user requirements."
export PYTHONPATH=$WORKSPACE

nosetests --with-xcoverage --with-xunit --cover-package=freesm --cover-erase
pylint -f parseable freesm/ | tee pylint.out
