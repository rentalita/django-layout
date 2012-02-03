#!/bin/sh

@OVID@_TESTS=
export @OVID@_TESTS

@OVID@_HOME="$(dirname $0)"
. "${@OVID@_HOME}"/etc/common

cd "${@OVID@_HOME}"

"${@OVID@_BIN}"/python.sh setup.py -q clean "$@"
[ $? != 0 ] && echo "ERROR!!!" && exit 1

find . -name "*~" | xargs rm -f
find . -name "*.pyc" | xargs rm -f

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
