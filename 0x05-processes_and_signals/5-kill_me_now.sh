#!/usr/bin/env bash
# Write a Bash script that kills 4-to_infinity_and_beyond process.

kill -9 "$(pgrep -f "4-to_infinity_and_beyond")"
