#!/bin/sh -e

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
        "${@OVID@_BIN}"/django-manage.sh celeryd_multi -q start default -E \
            --logfile="${@OVID@_LOG}"/celeryd-%n.log \
            --pidfile="${@OVID@_RUN}"/celeryd-%n.pid
	;;
    stop)
        "${@OVID@_BIN}"/django-manage.sh celeryd_multi -q stop default \
            --pidfile="${@OVID@_RUN}"/celeryd-%n.pid
	;;
    restart)
            "$0" stop
            "$0" start
	;;
    *)
	    print_usage_and_die
	;;
esac

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
