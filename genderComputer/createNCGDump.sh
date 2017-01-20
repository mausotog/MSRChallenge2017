#!/bin/bash

rm -f NCGDataSet.csv
#datasetFile=../3ParamsHead.csv
datasetFile=../travisTorrent3ParamsNoRepeat.csv
while read dataRow
do
projectName=$(echo $dataRow | cut -d "," -f1)
commitHash=$(echo $dataRow | cut -d "," -f2)
commitSite=https://github.com/"$projectName"/commit/"$commitHash"
echo $commitSite
developerNCG=$(python ExtractNCG.py $commitSite)
echo "$developerNCG"
echo "$developerNCG" >> NCGDataSet.csv
done < $datasetFile 

