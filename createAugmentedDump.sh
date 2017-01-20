#!/bin/bash

rm -f augmentedDataSet.csv
#datasetFile=./3ParamsHead.csv
datasetFile=./travisTorrent3ParamsNoRepeat.csv
while read dataRow
do
projectName=$(echo $dataRow | cut -d "," -f1)
commitHash=$(echo $dataRow | cut -d "," -f2)
commitSite=https://github.com/"$projectName"/commit/"$commitHash"
echo $commitSite
developerData=$(python ExtractDeveloper.py $commitSite)
echo "$dataRow$developerData"
echo "$dataRow$developerData" >> augmentedDataSet.csv
done < $datasetFile 

