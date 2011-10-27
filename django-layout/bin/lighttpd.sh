#!/bin/sh

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

print_usage_and_die()
{
    echo "Usage: $(basename $0) [start | stop | restart]"
    exit 1
}

OPTION="$1"

case "${OPTION}" in
    start)
	    lighttpd -f "${@OVID@_ETC}"/lighttpd.conf
	;;
    stop)
	    [ -f "${@OVID@_RUN}"/lighttpd.pid ] && \
	        kill $(cat "${@OVID@_RUN}"/lighttpd.pid)
	;;
    restart)
            "$0" stop
            "$0" start
	;;
    *)
	    print_usage_and_die
	;;
esac

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
