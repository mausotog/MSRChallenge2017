#!/bin/bash

#This is to check how many lines in this file end with ,t
#sed 's/echo/echo\n/g' wekaConfoundData.arff | grep -c ",t"

cd /tmp/confoundData/
tech=./wekaConfoundData.arff
techSoc=./wekaConfoundAndSocData.arff
outputT=/tmp/confoundData/evenNumberPassedAndNotTech.arff
outputTS=/tmp/confoundData/evenNumberPassedAndNotTechAndSoc.arff

rm -f $outputT
rm -f $outputTS

#datasetFile=./travistorrent_11_1_2017.csv
counter=1
for i in `seq 1 371223`; #371223
do
  #echo $i
  command="sed '"$i"q;d' $tech"
  #echo $command
  lineT=`eval $command`
  #echo $lineT
  if [[ $lineT == *",t" ]]
  then
    number=$RANDOM
    let "number %= 2"
	#echo $number
	if [ $number == 0 ] && [  "$counter" -le 94921 ]
	then
      echo $lineT >> $outputT
      command="sed '"$i"q;d' $techSoc"
      lineTS=`eval $command`
	  echo $lineTS >> $outputTS
	  counter=$((counter+1))
	fi
  elif [[ $line == *",f" ]]
  then
      echo $lineT >> $outputT
      command="sed '"$i"q;d' $techSoc"
      lineTS=`eval $command`
	  echo $lineTS >> $outputTS
  else
      echo $lineT >> $outputT
      command="sed '"$i"q;d' $techSoc"
      lineTS=`eval $command`
	  echo $lineTS >> $outputTS
  fi
done 



