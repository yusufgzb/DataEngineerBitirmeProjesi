Streamlit app
docker build . -t streamlit-image
docker run -p 8080:8080 --name streamlit-container streamlit-image

