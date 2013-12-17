============================
Dimagi - Applicant Exercises
============================

*December 17, 2013 4:45pm*

System
======
- ubuntu 12.04.3 LTS ($ cat /etc/lsb-release)
- python 2.7.3 ($ python -V)
- django 1.5.5 final ($ echo "import django; print django.VERSION" | python)
- virtualenv 1.10.1 ($ virtualenv --version)

Django project
==============

- coding style: PEP8
- layout: `github.com/morenopc/django-twoscoops-project <https://github.com/morenopc/django-twoscoops-project>`_

adapt from: Two Scoops of Django by Daniel Greenfeld book::

    $ django-admin.py startproject --template=https://github.com/morenopc/django-twoscoops-project/zipball/develop --extension=py,rst,html,sh dimagi

Getting start
=============

setting local project::

    $ dimagi-project$ ./scripts/local.sh

runserver::

    $ dimagi-project$ ./scripts/runserver.sh
