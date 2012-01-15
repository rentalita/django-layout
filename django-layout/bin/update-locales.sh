#!/bin/sh

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

LOCALES="es"

for locale in ${LOCALES}; do
    (
        cd "${@OVID@_HOME}"
        "${@OVID@_BIN}"/django-manage.sh makemessages -l "${locale}" -e .html -e .txt -e .js
        "${@OVID@_BIN}"/django-manage.sh compilemessages -l "${locale}"
    )
done

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
