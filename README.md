## CSE508_Winter2023_Project_10

## Project Title: Real-Time-Earthquake-Detection-and-Analysis-Using-Twitter-Data

### Description
This project aims to develop a real-time earthquake detection and notification system by analyzing Twitter data using machine learning algorithms. The goal is to provide a cost-effective, timely solution that can quickly and accurately detect seismic events and alert NGOs and monitoring committees, potentially saving lives and mitigating the impact of earthquakes.

## Installation and Setup

### 1. **Run Classification Model**
   - Load the training and test datasets in Google Colab.
   - Execute the `ir_bert_model.py` file located in the `Final Deliverables` folder.

### 2. **Install Docker and Docker Compose**

### 3. **Copy and Save the Model**
   ```bash
   mkdir -p /[your_project_directory]/IR_Project_BE/model/
   cp [your_saved_model_path] /[your_project_directory]/IR_Project_BE/model/
  ```

### For Setting up Kafka and Zookeeper
  ```bash
cd /[your_project_directory]/kafka-docker/
docker compose up -d
  ```

### For running Kafka Producer  nodejs service for real time tweets streaming
  ```bash
cd /[your_project_directory]/kafka-producer/
docker build . --no-cache -t producer-api
docker run -it --init --net="host" -d --name producer-api-ins producer-api
  ```

### For running prediction flask webserver
  ```bash
cd /[your_project_directory]/IR_Project_BE/
docker build . --no-cache -t predict-api
docker run -it --init --net="host" -d --name predict-api-ins predict-api
  ```

### For running map creator flask webserver
  ```bash
cd /[your_project_directory]/MapCreator/
docker build . --no-cache -t map-api
docker run -it --init --net="host" -d --name map-api-ins map-api
  ```

### For running UI of the application
  ```bash
cd /[your_project_directory]/FrontEndWithFireBase/
docker build . --no-cache -t frontend
docker run -it --init --net="host" -d --name frontend-ins frontend
  ```

