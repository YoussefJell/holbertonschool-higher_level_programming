#!/usr/bin/bash
read -e filename
cat $filename | sudo mysql -hlocalhost -uroot -p hbtn_0c_0
