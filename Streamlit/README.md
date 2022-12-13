Streamlit app

Install Docker

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install docker.io

sudo apt-get update

sudo docker -v

-----------


sudo docker build . -t streamlit-image

sudo docker run -p 8080:8080 --name streamlit-container streamlit-image

