# tsuru-docker-service

**Tsuru Docker Service (TDS)** provides easy to use, powerful and flexible manager of Tsuru's services (tsuru.io) using Docker server.


# Requirements

TODO: Docker host and mongodb (that can be inside docker)


# Usage

To use TDS we must perform the following steps:

 - [Get the demo app](#get-demo)
 - [Create Tsuru app for the service](#create-tsuru-app)
 - [Configure the app](#configure-app)
 - [Deploy the app](#deploy-service-app)
 - [Create Tsuru service](#create-tsuru-service)
 - [Create service instance](#create-service-instance)
 - [Bind the service's instance to your app](#bind-service)


## <a name="get-demo"></a>Get the demo app
You can get [the demo app](demo/) running the following commands on your workdir:

```bash
git clone https://github.com/juliomfreitas/tsuru-docker-service.git
cp -r tsuru-docker-service/demo my-docker-service
cd my-docker-service/
```

> NOTE: Now your workdir will be **./my-docker-service/**.

> NOTE²: Instead of 'my-docker-service' set the dir name with a name that make sense for you context.


## <a name="create-tsuru-app"></a>Create Tsuru app for the service

Now you have to create a Tsuru app that will run your service manager.

```bash

tsuru app-create docker-service python -t myteam -o mypool
```

> NOTE: Execute **tsuru app-create --help** to see all options.


## <a name="configure-app"></a>Configure the app

Not you have to set the environment variables that define what resources your
service will use.

The TDS requires the following variables:

 - `MONGODB_ENDPOINT` - E.g: "mongodb://$DOCKER_HOST:27017/"
 - `DOCKER_ENDPOINT` - E.g: "http://$DOCKER_HOST:2375"

> NOTE: Security is not the scope of this tutorial. You must assert that the $DOCKER_HOST and MongoDB service don't receive access of outside your infrastructure. To see how you the do it on top of AWS EC2 [click here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html).



## <a name="deploy-service-app"></a>Deploy the app

## <a name="create-tsuru-service"></a>Create Tsuru service

## <a name="create-service-instance"></a>Create service instance

## <a name="bind-service"></a>Bind the service's instance to your app

