#!/usr/bin/env bash
# write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
# shellcheck disable=SC2009
ps axuf | grep "bash"
