#!/bin/bash

rm confoundData.csv
rm confoundAndSocData.csv
rm confoundDataNotFound.txt
socData=./confoundDataWithCoreMember.csv
#datasetFile=./travistorrent_11_1_2017.csv
while read dataRow; do
commit=$(echo $dataRow | cut -d "," -f1)
command="grep -rnw 'augmentedDataSet.csv' -e $commit"
#echo $command
socDataRow=`eval $command`
    if [ "$socDataRow" != "" ]
    then
      jobStatus=$(echo $dataRow | cut -d "," -f11)
      pushedAt=$(echo $dataRow | cut -d "," -f2)
      at1=$(echo $dataRow | cut -d "," -f3)
      at2=$(echo $dataRow | cut -d "," -f4)
      at3=$(echo $dataRow | cut -d "," -f5)
      at4=$(echo $dataRow | cut -d "," -f6)
      at5=$(echo $dataRow | cut -d "," -f7)
      at6=$(echo $dataRow | cut -d "," -f8)
      at7=$(echo $dataRow | cut -d "," -f9)
      at8=$(echo $dataRow | cut -d "," -f10)
      byCoreTeamMember=$(echo $dataRow | cut -d "," -f12)
      repositories=$(echo $socDataRow | cut -d "," -f4)
      stars=$(echo $socDataRow | cut -d "," -f5)
      followers=$(echo $socDataRow | cut -d "," -f6)
      following=$(echo $socDataRow | cut -d "," -f7)
      collabProjects=${socDataRow##*,} #$(echo $socDataRow | cut -d "," -f9)
	  echo "$commit,$pushedAt,$at1,$at2,$at3,$at4,$at5,$at6,$at7,$at8,$jobStatus" >> confoundData.csv
      echo "$commit,$pushedAt,$at1,$at2,$at3,$at4,$at5,$at6,$at7,$at8,$byCoreTeamMember,$repositories,$stars,$followers,$following,$collabProjects,$jobStatus" >> confoundAndSocData.csv
	else
      echo "Did not find match in augmentedData for commit $commit"	>> confoundDataNotFound.txt
    fi
done <$socData 


