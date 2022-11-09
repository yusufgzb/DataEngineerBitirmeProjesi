Kafka
nohup bin/zookeeper-server-start.sh config/zookeeper.properties &
nohup bin/kafka-server-start.sh config/server.properties &

bin/kafka-topics.sh --create --topic ornek --bootstrap-server localhost:9092

bin/kafka-console-consumer.sh --topic ornek --from-beginning --bootstrap-server localhost:9092
bin/kafka-console-producer.sh --topic ornek --bootstrap-server localhost:9092
bin/kafka-topics.sh --bootstrap-server=localhost:9092 –list
bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic ornek
