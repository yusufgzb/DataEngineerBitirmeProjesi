Nifi

sudo apt-get install openjdk-8-jdk


wget https://archive.apache.org/dist/nifi/1.13.2/nifi-1.13.2-bin.tar.gz

tar -xzvf nifi-1.13.2-bin.tar.gz

nano nifi-1.13.2/conf/nifi.properties


cd nifi-1.13.2/bin/


./nifi.sh start


./nifi.sh status
