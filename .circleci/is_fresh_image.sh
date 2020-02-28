#!/bin/sh

set -x
check_updates="yum --quiet check-update";
if zypper --version &>/dev/null; then
    pkg_manager="zypper --quiet list-updates";
elif dnf --version &>/dev/null; then
    pkg_manager="dnf --quiet check-update";
fi

${check_updates} | tee /tmp/yum.log
update_list_lines=$(cat /tmp/yum.log | wc -l)
echo "Update log have ${update_list_lines} lines"
if [ "${update_list_lines}" -gt 20 ]; then
    exit 1;
fi
