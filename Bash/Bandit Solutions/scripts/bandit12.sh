#! /bin/shls
ls
man gzip
man mv
man mkdir
mkdir /tmp/sol
man cp
cp data.txt /tmp/sol/data.txt
cd tmp/sol
cd /tmp/sol
man xxd
xxd -r data.txt data.out
ls
man mv
man bzip2
mv data.out data.gz
gzip -d data.gz
file data
bzip2 -d data
file data.out
mv data.out data.gz
gzip -d data.gz
ls
file data
man tar
tar -xf data 
ls
file data6.bin
bzip2 -d data6.bin
file data6.bin.out
ls
tar -x data6.bin.out
ls
file data8.bin
mv data8.bin data8.gz
gzip -d data8.gz
ls
cat data8
