#!/bin/sh -e

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

${ASROOT} logrotate --state "${@OVID@_RUN}"/logrotate.state \
    "${@OVID@_ETC}"/logrotate.conf "$@"

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
