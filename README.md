# Web Service to host an ML Model for Inference. 
A simple python web service to host a machine learning model inference as an API.

The container trains a simple [text classifier](https://fasttext.cc/docs/en/supervised-tutorial.html) and hosts it for inference as a web service written in [Sanic Framework](https://sanic.readthedocs.io/en/latest/). The data for model training is included in the project. 

---

### Pre-requisites

 1. System should have [docker engine](https://docs.docker.com/install/) installed.
>**Note**: I developed and tested this on Ubuntu-16.04.

---

### Hosting the web service

 1. Build the docker image 
```bash 
docker build --network=host -t ml-inference-api:v1 .
```
2. Check the image 
```bash
docker images
```
<p align="center">    
  <img src="/docs/images/mia-01.png" alt="Docker Images">    
</p>    

3. Run the container
 ```bash
 docker run -d --net=host --name=ml-inference-api ml-inference-api:v1
 ```
 4. Check whether the container is up 
```bash
docker ps
```
<p align="center">    
  <img src="/docs/images/mia-02.png" alt="Running Containers">    
</p>    


>When we run the container two scripts are initiated:
>1. `train.py` which trains the model to be hosted.
>2. `inference.py` which hosts the model as web service.

---

### API Usage
The web services includes the [sanic-openapi](https://github.com/huge-success/sanic-openapi) integration. Thus, we can directly use the swagger portal from web browser to use the API. To open the swagger portal go to your browser and enter `http://localhost:8080/swagger/`. This will open the swagger portal only if the service is hosted properly.
<p align="center">    
  <img src="/docs/images/mia-03.png" alt="Swagger Portal">    
</p>    

To check whether service is up:

 1. Click on the `GET` bar. 

 2. Click on `Try it out`
<p align="center">    
  <img src="/docs/images/mia-04.png" alt="Try It Out">    
</p>   

 3. Click on `Execute`
<p align="center">    
  <img src="/docs/images/mia-05.png" alt="Execute">    
</p>   

 4. If you see the following screen then your service is up.
<p align="center">    
  <img src="/docs/images/mia-06.png" alt="Service Up">    
</p>    

To predict the label of the text:

 1. Click on the `POST` bar. 

 2. Click on `Try it out`
<p align="center">    
  <img src="/docs/images/mia-07.png" alt="Try It Out">    
</p>   

 3. In Edit Value, paste the folllowing json
```json
{
  "source": "swagger",
  "text": "Why should I not put knives in dishwasher?"
}
```
<p align="center">    
  <img src="/docs/images/mia-08.png" alt="Edit Value">    
</p>  

 4. Click on `Execute`

 5. We should see a response similar to the following:
<p align="center">    
  <img src="/docs/images/mia-09.png" alt="Inference Response">    
</p>    

---

### Logs checking
To check the the web service logs we need to get inside the running container. To do so execute the following command:
```bash
docker exec -it ml-inference-api bash
```
Now we are inside the container.

The logs are available in the logs folder in the files `ml-inference-api.log` and `ml-inference-api.err`.

<p align="center">    
  <img src="/docs/images/mia-10.png" alt="Inside container">    
</p>    

---

### Stopping the web service
Run the following command to stop the container:
```bash
docker stop ml-inference-api
```
---
**Author**: [Pranay Chandekar](https://www.linkedin.com/in/pranaychandekar/)