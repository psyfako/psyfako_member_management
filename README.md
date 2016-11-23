# psyfako_member_management
blablabla leute müssen verwaltet werden


![erstes konzept](./stuff/whiteboard_2016-08-08.jpg)


## requirements

Django==1.10
django-phonenumber-field==1.1.0
django-tagulous==0.11.1


## install copy pasta

sudo -s

#sudo pip3 install mysqlclient fails with mysql_config not found
apt-get install libmysqlclient-dev

#without pip3 it will not going to work for python3
pip3 install mysqlclient
pip3 install django-allauth
pip3 install django-configurations
pip3 install django-phonenumber-field
pip3 install django-tagulous