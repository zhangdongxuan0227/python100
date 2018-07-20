#!/bin/bash
path="x/x/x"
FILE1="yourapp1.apk"
FILE2="yourapp2.apk"
keytool -list -printcert -jarfile $path/$file |grep MD5 >$FILE1_MD5.txt
keytool -list -printcert -jarfile $path/$file |grep MD5 >$FILE2_MD5.txt

MD5_diff=`diff $FILE1.certMD5 $FILE2.certMD5`

# if [-z "MD5_diff"]; then
# echo "$FILE1_MD5 == $$FILE2_MD5"	
# fi
if [ "$MD5_diff" = "" ]; then 
echo "$FILE1_MD5 == $$FILE2_MD5"
fi