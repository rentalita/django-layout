#!/bin/sh -e

DJANGO_LAYOUT_HOME="$(dirname $0)"
DJANGO_LAYOUT_TMPL="${DJANGO_LAYOUT_HOME}"/django-layout

PROJECT_PATH="$1"

if [ "${PROJECT_PATH}" = "" ]; then
    echo "Usage: $(basename $0) path/to/name-of-project"
    exit 1
fi

PROJECT_NAME="$(basename "${PROJECT_PATH}")"
PROJECT_TEMP="$(mktemp -d)"

tar -C "${DJANGO_LAYOUT_TMPL}" -cf - $(cd "${DJANGO_LAYOUT_TMPL}"; find .) | \
    $(tar -C "${PROJECT_TEMP}" -xf -)

LOWER_NAME="${PROJECT_NAME}"

LOWER_NAME="$(echo "${LOWER_NAME}" | perl -pe '$_ = lc;')"
UPPER_NAME="$(echo "${LOWER_NAME}" | perl -pe '$_ = uc;')"
FIRST_NAME="$(echo "${LOWER_NAME}" | perl -pe '$_ = ucfirst;')"

RETURN_TO="$(pwd)"

cd "${PROJECT_TEMP}"

find . -type f -print0 | xargs -0 perl -pi -e "s/\@OVID\@/${UPPER_NAME}/g;"
find . -type f -print0 | xargs -0 perl -pi -e "s/\@ovid\@/${LOWER_NAME}/g;"
find . -type f -print0 | xargs -0 perl -pi -e "s/\@Ovid\@/${FIRST_NAME}/g;"

for d in $(find . -type d -name "*ovid*"); do
    mv $d $(echo $d | perl -p -e "s/ovid/${LOWER_NAME}/g;")
done

for d in $(find . -type d -name "*OVID*"); do
    mv $d $(echo $d | perl -p -e "s/OVID/${UPPER_NAME}/g;")
done

for d in $(find . -type d -name "*Ovid*"); do
    mv $d $(echo $d | perl -p -e "s/Ovid/${FIRST_NAME}/g;")
done

for f in $(find . -type f -name "*OVID*"); do
    mv $f $(echo $f | perl -p -e "s/OVID/${UPPER_NAME}/g;")
done

for f in $(find . -type f -name "*ovid*"); do
    mv $f $(echo $f | perl -p -e "s/ovid/${LOWER_NAME}/g;")
done

for f in $(find . -type f -name "*Ovid*"); do
    mv $f $(echo $f | perl -p -e "s/Ovid/${FIRST_NAME}/g;")
done

./bin/update-secret-key.sh

cd "${RETURN_TO}"

if [ ! -d "${PROJECT_PATH}" ]; then
    mkdir "${PROJECT_PATH}"
fi

tar -C "${PROJECT_TEMP}" -cf - $(cd "${PROJECT_TEMP}"; find .) | \
    $(tar -C "${PROJECT_PATH}" -xf -)
