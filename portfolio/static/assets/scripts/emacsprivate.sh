#!/bin/bash

git clone git@github.com:seandjones92/Emacs.git ~/.emacs.d
cd ~/.emacs.d
git update-index --assume-unchanged init.el
