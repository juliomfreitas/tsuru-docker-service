[![Build Status](https://travis-ci.org/juliomfreitas/tsuru-docker-service.svg?branch=master)](https://travis-ci.org/juliomfreitas/tsuru-docker-service)


# tsuru-docker-service

**Tsuru Docker Service (TDS)** provides easy to use, powerful and flexible manager of Tsuru's services (tsuru.io) using Docker server.


# Requirements

TODO: Docker host and mongodb (that can be inside docker)


# Usage

To use TDS we must perform the following steps:

 - [Clone this repository](#clone-repo)
 - [Create Tsuru app for the service](#create-tsuru-app)
 - [Configure the app](#configure-app)
 - [Deploy the app](#deploy-service-app)
 - [Create Tsuru service](#create-tsuru-service)
 - [Create service instance](#create-service-instance)
 - [Bind the service's instance to your app](#bind-service)


## <a name="clone-repo"></a>Clone this repository

```bash
git clone https://github.com/juliomfreitas/tsuru-docker-service.git
cd tsuru-docker-service/
```

## <a name="create-tsuru-app"></a>Create Tsuru app for the service

Now you have to create a Tsuru app that will run your service manager.

```bash
tsuru app-create docker-service python -t myteam -o mypool
```

> NOTE: Execute **tsuru app-create --help** to see all options

The result of the command:

> App "docker-service" has been created!
> Use app-info to check the status of the app and its units.
> Your repository for "docker-service" project is
> **"git@your-domain.com:docker-service.git"**

Above, the returned git repository URL is **"git@your-domain.com:docker-service.git"**. In order to deploy the app you need to set on you environment the returned repository url:

```bash
git remote add tsuru [GIT_REPOSITORY_URL]
```

## <a name="configure-app"></a>Configure the app

Not you have to set the environment variables that define what resources your
service will use.

The TDS requires the following variables:

 - `MONGODB_ENDPOINT` - E.g: "mongodb://$DOCKER_HOST:27017/"
 - `DOCKER_ENDPOINT` - E.g: "http://$DOCKER_HOST:2375"

> NOTE: Security is not the scope of this tutorial. You must assert that the $DOCKER_HOST and MongoDB service don't receive access of outside your infrastructure. To see how you the do it on top of AWS EC2 [click here](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html).



## <a name="deploy-service-app"></a>Deploy the service app

To deploy the service (you already created the `tsuru` remote before) just type:

```bash
git push tsuru master
```


## <a name="create-tsuru-service"></a>Create Tsuru service

## <a name="create-service-instance"></a>Create service instance

## <a name="bind-service"></a>Bind the service's instance to your app

