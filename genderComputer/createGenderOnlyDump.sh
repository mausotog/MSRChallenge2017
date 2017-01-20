#!/bin/bash

rm -f genderOnlyDataSet.csv
#datasetFile=../3ParamsHead.csv
datasetFile=../travisTorrent3ParamsNoRepeat.csv
while read dataRow
do
projectName=$(echo $dataRow | cut -d "," -f1)
commitHash=$(echo $dataRow | cut -d "," -f2)
commitSite=https://github.com/"$projectName"/commit/"$commitHash"
echo $commitSite
developerGender=$(python ExtractGender.py $commitSite)
echo "$developerGender"
echo "$developerGender" >> genderOnlyDataSet.csv
done < $datasetFile 

