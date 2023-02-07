Kafka

--------------------------------------------------------------------------------------------------------
Elle kurulum

sudo apt-get install openjdk-8-jdk

wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz

tar -xzvf kafka_2.12-3.3.1.tgz

cd  kafka_2.12-3.3.1

sudo nohup bin/zookeeper-server-start.sh config/zookeeper.properties &


sudo nohup bin/kafka-server-start.sh config/server.properties &

sudo bin/kafka-topics.sh --create --topic ornek --bootstrap-server localhost:9092

sudo bin/kafka-console-consumer.sh --topic ornek --from-beginning --bootstrap-server localhost:9092

sudo bin/kafka-console-producer.sh --topic ornek --bootstrap-server localhost:9092

--------------------------------------------------------------------------------------------------------

cd /opt/kafka/

sudo nohup bin/zookeeper-server-start.sh config/zookeeper.properties &

sudo nohup bin/kafka-server-start.sh config/server.properties &


sudo bin/kafka-topics.sh --create --topic ornek --bootstrap-server localhost:9092

sudo bin/kafka-console-consumer.sh --topic ornek --from-beginning --bootstrap-server localhost:9092

sudo bin/kafka-console-producer.sh --topic ornek --bootstrap-server localhost:9092

sudo bin/kafka-topics.sh --bootstrap-server=localhost:9092 –list

sudo bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic ornek


