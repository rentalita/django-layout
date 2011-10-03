#!/bin/sh

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

/usr/sbin/make-ssl-cert /usr/share/ssl-cert/ssleay.cnf \
    "${@OVID@_ETC}"/server.pem --force-overwrite

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
