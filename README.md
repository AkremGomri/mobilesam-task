# Internship Take Home Assignment - Software Engineer

This repository is an assignment which is designed to assess my software engineering skills in the context of an internship application to SpaceSence.

I have forked the repository, and made the changes to answear the quesion.

## How to Run the Code

### Without Using Docker (Recommanded)

1. **Clone the project locally and move to the project**

```bash
  git clone https://github.com/AkremGomri/mobilesam-task.git
  cd mobilesam-task
```

2. **Create a Virtual Environment and Activate It**

```bash
python -m venv venv
venv\Scripts\activate  # On Linux or MacOs use `source venv/bin/activate`
```

3. **Install the Requirements**

```bash
pip install -r requirements.txt
```

4. **Run the Server**
```bash
uvicorn main:app --reload # --reload is an option
```

5. **Test the functionality**
   
At this point, you are free to choose whichever tool you prefer to interact with the APIs, however, I recommend using Swagger UI since it is already integrated with FastAPI.

***Swagger:***

Open a web browser and navigate to http://localhost:8000/docs to access the Swagger UI interface and interact with the FastAPI server running inside the Docker container.
Enjoy exploring the functionality of the API with Swagger UI!

Note: Processing the image might take up to a minute, so be patient.

### Using Docker (Not tested)

1. **Clone the project locally and move to the project directory:**
    ```bash
    git clone https://github.com/AkremGomri/mobilesam-task.git
    cd mobilesam-task
    ```

2. **Build the Docker image:**
    ```bash
    docker build -t mobilesam-task .
    ```

3. **Run the Docker container:**
    ```bash
    docker run -d -p 8000:8000 mobilesam-task
    ```

4. **Open a web browser and navigate to `http://localhost:8000/docs` to access the Swagger UI interface and interact with the FastAPI server running inside the Docker container.**

## Task Overview

**Title:** MobileSam Segmentation Model Service

**Expected Time to Complete:** 4 hours

**Objective:** Develop a FastAPI service to deploy the MobileSam segmentation model, containerize the service with Docker, and ensure efficient interaction with the model on the CPU.

**Background:**
MobileSam is a machine learning model specialized in image segmentation on CPUs. Your task is to create a microservice that allows users to interact with this model via an API. You should find the script `main.py` in this repository, which contains the MobileSam model and a function `segment_everything` that takes an image as input and returns the segmentation result. You can use this function to develop your service. Ignore the default parameters of the function for now.

## Task Description

- **Develop a Microservice:** Use a Python API framework (we suggest FastAPI) to expose the MobileSam segmentation model as a RESTful API.
  
- **Model Integration:** Incorporate the MobileSam segmentation model into your service. It should process image inputs and return segmentation results.
  
- **API Endpoints:** Create a POST endpoint `/segment-image` to accept an image file, process it through MobileSam, and return the segmentation result.
  
- **Documentation:** Provide clear instructions for setting up, running, and interacting with the service in a README.md file.

- **[Bonus]** Docker Familiarity: Containerize your service using Docker.


## Authors

- **Issuing Company**: [SpaceSense](https://github.com/rohan-spacesense)

- **Contributor**: [Akrem Gomri](https://github.com/AkremGomri/)

