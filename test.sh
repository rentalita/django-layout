#!/bin/sh

@OVID@_TESTS=1
export @OVID@_TESTS

@OVID@_HOME="$(dirname $0)"
. "${@OVID@_HOME}"/etc/common

cd "${@OVID@_HOME}"

"${@OVID@_BIN}"/django-migrate.sh

"${@OVID@_BIN}"/nosetests.sh "$@"
[ $? != 0 ] && echo "ERROR!!!" && exit 1

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
