Streamlit app

Install Docker

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-get update

sudo apt-get install docker-ce

docker -v

-----------


docker build . -t streamlit-image

docker run -p 8080:8080 --name streamlit-container streamlit-image

