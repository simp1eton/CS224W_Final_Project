#!/bin/bash
for f in input3-*.txt ; do
  sed -i '' '2d' "${f}"
done
