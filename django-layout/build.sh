#!/bin/sh

@OVID@_TESTS=
export @OVID@_TESTS

@OVID@_HOME="$(dirname $0)"
. "${@OVID@_HOME}"/etc/common

cd "${@OVID@_HOME}"

if [ ! -f setup.cfg ]; then
        sed -e "s#\@prefix\@#${@OVID@_HOME}#g;" setup.cfg.in > setup.cfg
fi

TARGET="$@"
TARGET="${TARGET:-develop}"

"${@OVID@_BIN}"/python.sh setup.py -q "${TARGET}"
[ $? != 0 ] && echo "ERROR!!!" && exit 1

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
