# Transactions API

> This repo is a task task. It's <b>NOT</b> a real project.
> I wanted to make it as fast as I can, and meet the requirements.
## Usage
Basically, I've already deployed the API, so the only thing you have to do is use it.
Open [this](./openapi.yaml) file with Swagger and see it.

## Deployment
<img src="https://developers.redhat.com/sites/default/files/styles/article_feature/public/blog/2014/05/homepage-docker-logo.png?itok=zx0e-vcP"  
width="64" height="64">
### Docker - the simplest method 


Basically do this:
1. Pull the docker image from my Docker Hub: [arseniyohar](https://hub.docker.com/u/arseniyohar). I guess you can do it with: ``` docker pull arseniyohar/transactions ```
2. ```docker run -p $PORT:80 arseniyohar/transactions ```, where <i>$PORT</i> is an environment variable that denotes the exposed port by the app

## Run on your own
1. Clone this repository: <br/>
``` git clone https://github.com/SeeenyaOhar/transactions-api.git ```
2. Install Python and Poetry. You can find Python version in the poetry file, but currently it's <b>```^3.10```</b>
3. Once everything is ready, run this to install all the dependencies. This will basically take every dependency from <i> poetry.lock </i> file and install it for your system: <br/> ``` poetry install ```
4. Now, we have to set up the environment variables(e.g. for JWT signing). You can find these in <b><i>Dockerfile</i></b>.
5. Now you can finally run the app: ``` flask run ```, and you will see something like this:

```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. 
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.0.171:5000
```
### Support
If there is any issue, you can text me here: <b> arseniyohar@gmail.com </b>
