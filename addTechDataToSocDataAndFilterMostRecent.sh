#!/bin/bash

rm technicalData12.csv
rm bothData12.csv
counter=1
socData=./augmentedDataSet12.csv
#datasetFile=./travistorrent_11_1_2017.csv
while read -r socDataRow _ <&3; do
commitSoc=$(echo $socDataRow | cut -d "," -f2)
commitSoc="\"$commitSoc\""



#echo "Soc:"$commitSoc


for i in `seq $counter 50000`;
do
command="sed '"$i"q;d' ./travistorrent_11_1_2017.csv"
#echo $command
#dataRow="$(command)"
#eval $command
dataRow=`eval $command`
#echo $dataRow
#datasetFile=./travistorrent_11_1_2017TOCUT.csv
#while read -r dataRow <&4; do
commit=$(echo $dataRow | cut -d "," -f20)
jobStatus=$(echo $dataRow | cut -d "," -f43)
#echo $commit
if [ "$commit" == "$commitSoc" ]
then
  pushedAt=$(echo $dataRow | cut -d "," -f41)
  at1=$(echo $dataRow | cut -d "," -f24)
  at2=$(echo $dataRow | cut -d "," -f26)
  at3=$(echo $dataRow | cut -d "," -f27)
  at4=$(echo $dataRow | cut -d "," -f28)
  at5=$(echo $dataRow | cut -d "," -f29)
  at6=$(echo $dataRow | cut -d "," -f30)
  at7=$(echo $dataRow | cut -d "," -f31)
  at8=$(echo $dataRow | cut -d "," -f35)
  byCoreTeamMember=$(echo $dataRow | cut -d "," -f39)
  repos=$(echo $socDataRow | cut -d "," -f4)
  stars=$(echo $socDataRow | cut -d "," -f5)
  followers=$(echo $socDataRow | cut -d "," -f6)
  following=$(echo $socDataRow | cut -d "," -f7)
  collabProjects=$(echo $socDataRow | cut -d "," -f5)
  echo "$commit,$pushedAt,$at1,$at2,$at3,$at4,$at5,$at6,$at7,$at8,$jobStatus" >> technicalData12.csv
  echo "$commit,$pushedAt,$at1,$at2,$at3,$at4,$at5,$at6,$at7,$at8,$jobStatus,$byCoreTeamMember,$repos,$stars,$followers,$following,$collabProjects" >> bothData12.csv
   
#  remainingLines=$((3702596 - $counter))
#  tail -$remainingLines travistorrent_11_1_2017TOCUT.csv >> travistorrent_11_1_2017TOCUTTEMP.csv
#  rm ./travistorrent_11_1_2017TOCUT.csv
#  mv travistorrent_11_1_2017TOCUTTEMP.csv travistorrent_11_1_2017TOCUT.csv
  break
fi
counter=$((counter+1))

done  
#  done 4<$datasetFile
done 3<$socData 


