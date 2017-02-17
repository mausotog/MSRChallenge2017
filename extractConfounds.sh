#!/bin/bash
lastCommit=""
datasetFile=./travistorrent_11_1_2017.csv
while read dataRow; do
commit=$(echo $dataRow | cut -d "," -f20)
if [[ $commit != $lastCommit ]]
then
pushedAt=$(echo $dataRow | cut -d "," -f42)
year=$(echo $pushedAt | cut -d "-" -f1)
#  if [ "$year" == "2014" ] || [ "$year" == "2015" ] || [ "$year" == "2016" ] || [ "$year" == "2017" ]
 # then
  jobStatus=$(echo $dataRow | cut -d "," -f43)
  at1=$(echo $dataRow | cut -d "," -f24)
  at2=$(echo $dataRow | cut -d "," -f26)
  at3=$(echo $dataRow | cut -d "," -f27)
  at4=$(echo $dataRow | cut -d "," -f28)
  at5=$(echo $dataRow | cut -d "," -f29)
  at6=$(echo $dataRow | cut -d "," -f30)
  at7=$(echo $dataRow | cut -d "," -f31)
  at8=$(echo $dataRow | cut -d "," -f35)
  byCoreTeamMember=$(echo $dataRow | cut -d "," -f39)
  echo "$commit,$pushedAt,$at1,$at2,$at3,$at4,$at5,$at6,$at7,$at8,$jobStatus,$byCoreTeamMember" >> confoundData1.csv
  #fi
  lastCommit=$commit
fi
done <$datasetFile 


