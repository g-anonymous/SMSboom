#!/bin/bash
clear
echo -e "\e[4;31m Scriptking SCK !!! \e[0m"
echo -e "\e[1;34m Thailand GROUP \e[0m"
echo -e "\e[1;32m ยิงข้อความ \e[0m"
echo "Press Enter To Continue"
read a1
if [[ -s update.speedx ]];then
echo "เช็ค All Requirements Found...."
else
echo 'Installing Requirements....'
echo .
echo .
apt install figlet toilet python curl -y
apt install python3-pip
pip install -r requirements.txt
echo This Script Was Made By SpeedX >update.speedx
echo Requirements Installed....
echo Press Enter To Continue...
read upd
fi
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
figlet TBomb
echo -e "\e[1;34m ผู้จัดทำ By \e[1;32m"
toilet -f mono12 -F border SCK
echo -e "\e[4;34m THE RIPPERHACKER \e[0m"
echo -e "\e[1;34m ติดต่อได้ที่!!!\e[0m"
echo -e "\e[1;32m         FB:ต้า'า จุ้บ'บ \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/c/ScriptKing SCK \e[0m"
echo " "
echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"
echo " "
echo "Press 1 To  Start SMS Bomber "
echo "Press 2 To  Start Call Bomber "
echo "Press 3 To  Update (Works On Linux And Linux Emulators) "
echo "Press 4 To  View Features "
echo "Press 5 To  Exit "
read ch
if [ $ch -eq 1 ];then
clear
echo -e "\e[1;32m"
rm *.xxx >/dev/null 2>&1
python3 bomber.py
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 2 ];then
clear
echo -e "\e[1;32m"
echo 'Call Bomb By SpeedX'> call.xxx
python3 bomber.py call
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 3 ];then
clear
apt install git -y
echo -e "\e[1;34m Downloading Latest Files..."
git clone https://github.com/g-anonymous/Tbomd2
if [[ -s TBomb/TBomb.sh ]];then
cd TBomb
cp -r -f * .. > temp
cd ..
rm -rf  TBomb >> temp
rm update.speedx >> temp
rm temp
chmod +x TBomb.sh
fi
echo -e "\e[1;32m TBomb Will Restart Now..."
echo -e "\e[1;32m All The Required Packages Will Be Installed..."
echo -e "\e[1;34m Press Enter To Proceed To Restart..."
read a6
./TBomb.sh
exit
elif [ $ch -eq 4 ];then
clear
echo -e "\e[1;33m"
figlet TBomb
echo -e "\e[1;34mCreated By \e[1;34m"
toilet -f mono12 -F border SCK
echo  " "
echo -e "\e[1;32m                   Features\e[1;34m"
echo "  [+] Unlimited And Super-Fast Bombing"
echo "  [+] International Bombing"
echo "  [+] Call Bombing "
echo "  [+] Protection List"
echo "  [+] Automated Future Updates"
echo "  [+] Easy To Use And Embed in Code"
echo "Press Enter To Go Home"
read a3
clear
elif [ $ch -eq 5 ];then
clear
echo -e "\e[1;31m"
figlet TBomb
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border SCK
echo " "
exit 0
else
echo -e "\e[4;32m Invalid Input !!! \e[0m"
echo "Press Enter To Go Home"
read a3
clear
fi
done
