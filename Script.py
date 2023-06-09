# Installer des paquets utiles pour Ubuntu
sudo apt-get install ubuntu-restricted-extras build-essential curl git htop python3-pip vim

# Installer des paquets utiles pour le développement et les bibliothèques
sudo apt-get install build-essential curl git htop python3-pip python3-dev python3-venv libssl-dev libffi-dev zlib1g-dev libxml2-dev libxslt1-dev libjpeg-dev libpq-dev libmysqlclient-dev libsqlite3-dev libfreetype6-dev libblas-dev liblapack-dev libatlas-base-dev libhdf5-dev libopenblas-dev liblapacke-dev libboost-all-dev libcurl4-openssl-dev libgtk-3-dev libglfw3-dev libglfw3 libgl1-mesa-dev libglu1-mesa-dev libzmq3-dev libtbb-dev libtiff-dev libjpeg-turbo8-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libx264-dev libxvidcore-dev libcanberra-gtk-module libcanberra-gtk3-module libsm6 libxext6 libxrender-dev

# Installer des paquets utiles pour les tests de pénétration
sudo apt-get install build-essential git ruby ruby-dev libpcap-dev libpq-dev zlib1g-dev libffi-dev libgmp-dev

# Cloner le dépôt Metasploit Framework depuis GitHub
git clone https://github.com/rapid7/metasploit-framework.git

# Se placer dans le répertoire metasploit-framework
cd metasploit-framework

# Installer Ruby Bundler
sudo apt install ruby-bundler

# Installer les dépendances du projet Metasploit Framework
bundle install

# Installer PostgreSQL et créer un utilisateur et une base de données pour Metasploit Framework
sudo apt-get install postgresql
sudo service postgresql start
sudo -u postgres createuser msf -P -S -R -D
sudo -u postgres createdb -O msf msf

# Installer d'autres outils de test de pénétration
sudo apt-get install nmap wireshark john hydra sqlmap aircrack-ng snort fail2ban tcpdump netcat nbtscan onesixtyone nikto

