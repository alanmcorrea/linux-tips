#!/bin/bash

find /ebusiness/shared/applications/webj-aplb/appfiles/spme/arquivos/Fotos -type f -name '*.JPG' > /ebusiness/shared/applications/webj-aplb/appfiles/spme/arquivos/UPPERCASE_LIST.txt

while read mv_file
do
   
  mv_file_without_ext=$(echo "$mv_file" | cut -f 1 -d '.')

  echo $mv_file
  
  mv "$mv_file_without_ext.JPG" "$mv_file_without_ext.jpg"
  
done < /ebusiness/shared/applications/webj-aplb/appfiles/spme/arquivos/UPPERCASE_LIST.txt
