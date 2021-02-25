#! /bin/shls
ls /
cd krypton
ls -a
cd krypton4
ls
cat README
clear
cat HINT
cat found1
clear
cat found2
clear
cat krypton5
cat HINT
man sed
file found1
echo | sed 's/.\{0\}\(.\).*/\1/;q' found1
echo | sed 's/.\{5\}\(.\).*/\1/;q' found1
echo | sed 's/.\{11\}\(.\).*/\1/;q' found1
clear
echo | sed 's/.\{0\}\(.\).*/\1/;q' found1
echo | sed 's/.\{6\}\(.\).*/\1/;q' found1
clear
echo krypton5