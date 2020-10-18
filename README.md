# Data definition

### Task 1

# Required

* Python 3,8+
* Docker

### Optional
* psql (PostgreSQL) 12.4

# Initial setup

We have provided a simple Docker setup for you, which will start a
PostgreSQL instance populated with the assignment data. You don't have
to use it, but you might find it convenient.

You can execute the provided Dockerfile by running:

```bash
docker build -t ratestask .
```

This will create a container with the name *ratestask*, which you can
start in the following way:

```bash
docker run -p 0.0.0.0:5432:5432 --name ratestask ratestask
```

To star container run

```bash
docker start ratestask
```


# Before you start

Please provide following environment variables:  

Required
* FLASK_APP=rates.py

* DATABASE_URL - connection link to your database - postgresql://user:password@localhost:5432/database_name

* APP_SETTINGS - webapp.config.DevelopmentConfig - for development

* OPENEXCHANGERATES_URL - url to open exchange rates site (eg. https://openexchangerates.org/api/latest.json)
* APP_ID - your app id on open exchange rates site
  
Optional
* FLASK_ENV="${FLASK_ENV:=development}" - only for development

### Create virtual environment and install requirements
Create virtual environment, aka ```venv```

```bash
python3 -m venv path/to/your/venv
```

and activate it

```bash
. path/to/venv/bin/activate
```

install requirements

```bash
pip install -r requirements.txt
```

#### Run command  

```bash
flask run
```

### Task 2
 
I'd like to base my example on AWS.

We could send data or batches to s3 directly from front-end. Then use SQS that notifies SNS which notifies AWS Lambda.  
SQS can be skipped, but using it will ensure, that no messages are lost. We could then send notification to Lambda that divides batches for smaller bites of data.  
If batches are small enough we may skip that initial Lambda and send notification to Lambdas that process data and put it into database.  

Factors we need to take into consideration:  
* User experience, time needed to load file and how long user needs to stay on site after uploading file.  
* Will Lambda process batches in 45-60 minutes, before it terminates itself.  
* Lambda's cooldowns.  
* Idempotent operations on database.  
* It might by exaggeration, but S3 file size limit, in case we will provide files bigger than 5 terabytes :)