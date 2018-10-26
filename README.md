
## ARCHER python course

Welcome to the ARCHER python course. ARCHER https://www.archer.ac.uk/ is
the UK national supercomputing service.

#### Local details for Newcastle December 2018

Timetable; location; local announcements.

#### What you will need

- Your Laptop (Windows/MacOS/Linux) and eduroam credetials to connect to wifi
- Anaconda distribution of Python Version 3.5 or above. This may be downloaded
  from https://www.continuum.io/
- The course material should be downloaded from this repository
```
$ git clone http://github.com/EPCCed/archer-python.git
```

For this last stage you will require a git client (Linux/MacOS should have
one installed; Windows users may use e.g., Git for Windows from
https://gitforwindows.org/).

#### Contents

Lecture content is intended to be run via jupyter-lab and may be found
the `lectures` sub-directory. E.g., once you have downloaded the 
respository, from the directory containing this README run the command
```
$ jupyter-lab
```
and use the file navigation bar on the left to move to the lectures.

#### Examples

Thematic exmaple in examples/cfd

Archer examples in examples/mpi4py-archer


#### TODO

- contributing model
- license code/content
- public repository tests
- complete clean-up of cfd example
- add newcastke interest lecture
- complete user-intro
- consider scipy split?


#### ARCHER

Pending X-windows? Instructions on ssh -l <acount-name> login.archer.ac.uk?

We recommend the Anaconda distribution, as this provides a simple mechanism
to download all the python packages we will be interested in for the purposes
of the course. If you have an insisting installation of python, you should
note that the course will require at least: numpy, matplotlib, scipy, and
jupyter. BASH TERMINAL via jupyter.

* For Windows: An ssh client, and an X-window implementation. These are
conveniently supplied together by, e.g., MobaXterm
http://mobaxterm.mobatek.net

For MacOS/Linux

* ssh (usually installed as a default)

* X-window implementation, e.g., XQuartz http://www.xquartz.org
(note Mac-style terminal windows are not enough).

