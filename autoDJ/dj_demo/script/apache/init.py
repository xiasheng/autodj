
import os

os.system('cp dj_demo /etc/apache2/sites-available/')
os.system('a2dissite *')
os.system('a2ensite dj_demo')
os.system('apachectl restart')

