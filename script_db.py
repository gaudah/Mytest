import os
import sys
username=sys.argv[1]
#dbname=sys.argv[2]

'''
os.system("sudo dpkg -i INSTALL/Postgres/*.deb");
os.system("sudo dpkg -i INSTALL/Apache2/*.deb");
os.system("sudo dpkg -i INSTALL/wsgi/*.deb");
os.system("sudo apt-get --purge remove iceweasel");
os.system("sudo dpkg -i INSTALL/Firefox/*.deb");
os.system("sudo passwd postgres");
#os.system("su - postgres");
#os.system("psql");
#os.system("createuser %s" %(username));
#os.system("createdb %s" %(dbname));
'''
os.system("sudo -u %s psql -c '\i /home/minu/INSTALL/Scripts/db.txt;'" %(username));
#os.system("sudo -u %s psql -c 'create database %s;'" %(dbname));

#os.system("create user %s with superuser" %(username));
#os.system("create database %s" %(username));
#os.system("\q");
#os.system("exit");

'''
os.system("sudo /etc/init.d/apache2 restart");
os.system("sudo cp -vr INSTALL/Project/ /var/www/html/");
os.system("sudo cp INSTALL/Project/wsgi.conf /etc/apache2/conf-available/");
os.system("sudo service  apache2 restart");
os.system("sudo a2enconf wsgi");
os.system("sudo service  apache2 restart");
os.system("sudo a2enmod wsgi");
os.system("sudo service  apache2 restart");
os.system("sudo /etc/init.d/apache2 restart");
#os.system("firefox localhost/alise101");
#os.system("firefox localhost/test_wsgi");'''
