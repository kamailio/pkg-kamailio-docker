#!/bin/bash
find . -name Dockerfile -exec dirname {} \; | \
  grep -v -e 'rpm' | \
  jq -R . | sed 's#./##g' | jq -cs .
