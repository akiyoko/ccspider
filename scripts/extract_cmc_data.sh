#!/bin/bash

DIR_BASE=$(cd $(dirname ${0}); pwd)
TARGET_FILE=${DIR_BASE}/symbols.txt

# Delete old CSVs
rm -f ${DIR_BASE}/../downloads/*.csv

# Scraping currency prices
for line in `cat ${TARGET_FILE} | grep -v ^#`
do
  echo ${line}
  scrapy crawl cmc -a symbol=${line}
done
