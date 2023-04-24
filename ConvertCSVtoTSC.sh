#!/bin/bash
echo "Insert the CSV file to convert to TSV"
read File
#loop to iterate through the file to turn it into tsv
for i in "$File";
do
sed  's/,/\t/g' "$File"
done
