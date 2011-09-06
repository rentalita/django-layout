Django Layout -- A recommended Django project layout.
===

Django Layout is a recommended Django project layout with built-in
support for [nose](http://readthedocs.org/docs/nose/en/latest/),
[lighttpd](http://www.lighttpd.net/), and
[bootstrap](http://twitter.github.com/bootstrap/).

## CREATE NEW DJANGO PROJECT

For example, assuming `example-project` exists on GitHub and contains
a `master` and `unstable` branch, run these commands to create a new
Django project on the `unstable` branch.

    wget https://raw.github.com/gist/1196048/django-create-project.sh
    sh -e ./django-create-project.sh git@github.com:example/example-project.git example

Push the new Django project to GitHub.

    cd example
    git add .
    git commit -m "initial import"
    git push --all

## BUILD

This runs `python setup.py develop`.

    ./build.sh

## TEST

This uses `nosetests` to run the unit tests, and enables the built-in
coverage report.

    ./tests.sh
    sensible-browser ./src/python/example/cover/index.html

## SETUP

This creates a dummy SSL cert and an initial database. Also,
`django-migrate.sh` must be run anytime the Django models change.

    ./bin/make-ssl-cert.sh
    ./bin/django-migrate.sh

## USAGE

    ./bin/lighttpd.sh start

    sensible-browser http://localhost:8080

    ./bin/lighttpd.sh stop

## INSTALL

There is nothing to install.

## DEBUG

Several addtional scripts are provided in `./bin`. For example,
`python.sh` allows you to do things like `import example` straight
from the command-line.

## REQUIREMENTS

As tested on Ubuntu 11.04.

 * [python 2.7](http://www.python.org/)
 * [python-setuptools 0.6](http://packages.python.org/distribute/)
 * [python-nose 1.0](http://code.google.com/p/python-nose/)
 * [python-coverage 3.4](http://nedbatchelder.com/code/coverage/)
 * [python-django 1.3](http://www.djangoproject.com/)
 * [lighttpd 1.4](http://www.lighttpd.net/)
 * [python-flup 1.0](http://www.saddi.com/software/flup/)
 * [spawn-fcgi 1.6](http://redmine.lighttpd.net/projects/spawn-fcgi)
 * [sqlite3 3.7](http://www.sqlite.org/)
 * [ssl-cert 1.0](http://www.openssl.org/)

## OPTIONAL

 * [pylint 0.23](http://www.logilab.org/project/pylint)

## CONTRIBUTE

https://github.com/software6/django-layout

## LICENSE

Django Layout is brought to you by [Software 6](http://software6.net/)
and is in the public domain.
