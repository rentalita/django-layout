#!/bin/sh -e

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

"${@OVID@_BIN}"/celeryd.sh start
"${@OVID@_BIN}"/lighttpd.sh start

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
