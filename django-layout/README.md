Django @Ovid@ -- A Django project created by Django Layout.
===

Django @Ovid@ is...

## BUILD

This runs `python setup.py develop` (more or less).

    ./build.sh

## TEST

This uses `nosetests` to run the unit tests, and enables the built-in
coverage report.

    ./tests.sh
    sensible-browser ./src/python/@ovid@/cover/index.html

## SETUP

This creates a dummy SSL cert and an initial database. Also,
`django-migrate.sh` must be run each time the Django models change.

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
`python.sh` allows you to do things like `import @ovid@` straight from
the command-line.

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
 * [jquery 1.5](http://www.jquery.com/)

## OPTIONAL

 * [pylint 0.23](http://www.logilab.org/project/pylint)
