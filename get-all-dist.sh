#!/bin/bash
if [ -n "${1}" ] ; then
  echo "\"${1}\"" | jq -c 'split(",")'
else
  find . -name Dockerfile -exec dirname {} \; | \
    grep -v -e 'rpm' | \
    jq -R . | sed 's#./##g' | jq -cs .
fi
