#!/bin/bash

rm -f augmentedDataSet.csv
datasetFile=./travisTorrent3Params.csv
while read dataRow
do
projectName=$(echo $dataRow | cut -d "," -f1)
commitHash=$(echo $dataRow | cut -d "," -f2)
commitSite=https://github.com/"$projectName"/commit/"$commitHash"
echo $commitSite
developerData=$(python ExtractDeveloper.py $commitSite)
developerData=$(echo ${developerData//[[:blank:]]/})
developerData=$(echo ${developerData//[[:blank:]]/})
developerData=${developerData::-26}
echo $developerData
echo "$dataRow$developerData" >> augmentedDataSet.csv
done < $datasetFile 

