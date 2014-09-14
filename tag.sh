#!/bin/sh

echo "-= Creating ctags for project =-"
ctags -R -o tags --python-kinds=-i *

