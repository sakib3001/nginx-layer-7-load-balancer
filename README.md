# Nginx-Layer-7-Load-Balancer

This project showcases the implementation of an NGINX load balancer configured for Layer 7 (HTTP) load balancing using Docker containers. Layer 7 load balancing operates at the application layer, allowing more sophisticated traffic management based on the content of the HTTP requests.

## Features
- **Layer 7 Load Balancing:** Distributes HTTP requests based on URL paths, HTTP methods, and other application-level data. This allows for detailed and flexible routing of traffic to various backend services.

- **Content-Based Routing:** Routes traffic based on the content of the request, such as URL paths (/frontend, /backend) or HTTP headers. This enables more granular control over how requests are handled.

- **SSL Termination (Future Enhancement):** Although not yet implemented, future enhancements will include SSL/TLS configuration to secure communications between clients and the load balancer.

- **Application-Aware Routing:** Offers the ability to create custom routing rules based on application data, improving the user experience and optimizing backend resource usage.

- **Access Control:** Provides the ability to block specific paths (e.g., /admin) to enhance security and prevent unauthorized access..

## Prerequisites
Before you begin, ensure you have the following tools installed on your machine:
- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Run The Project

- #### Clone the project

```bash
   git clone https://github.com/sakib3001/nginx-layer-7-load-balancer

```

- #### Go to the project directory

```bash
 cd nginx-layer-7-load-balancer
```

- #### Creating the containers

```bash
  docker compose up -d --build
```

## Custom Configuration `nginx.conf`

``` nginx.cnf
# nginx layer 7 proxy 
events { }

http {
    upstream home_page {
        server app1:5000;
        server app2:5000;
        server app3:5000;
        server app4:5000;
    }
    upstream lb-set-1 {
        server app1:5000;
        server app2:5000;
    }
    upstream lb-set-2 { 
        server app3:5000;
        server app4:5000;
    }

    server {
        listen 80;

        # Default request handler (for `/`)
        location / { 
            proxy_pass http://home_page;  # Requests to `/` will be load-balanced by `home_page`
        }

        # Handling `/frontend` requests
        location /frontend {
            proxy_pass http://lb-set-1;  # Requests to `/frontend` will be load-balanced by `lb-set-1`
        }

        # Handling `/backend` requests
        location /backend {
            proxy_pass http://lb-set-2;  # Requests to `/backend` will be load-balanced by `lb-set-2`
        }

        # Block access to `/admin`
        location /admin {
            return 403;  # Returns a 403 Forbidden status for `/admin` requests
        }
    }
}

```

## Observer Load Balancing on The Browser
 
#### Hit these Links and Refresh 
```bash
  1. http://localhost/
  2. http://localhost/admin
  3. http://localhost/frontend
  4. http://localhost/backend

```

## Destroy The Containers
 
#### Stop All the containers in the docker-compose.yml
```bash
  docker compose stop
```
#### To release all the resources 
```bash
  docker compose down
```

## My Blog
For your better understanding read my blog
- [Documentation](https://ikasakib.hashnode.dev/layer-7-load-balancing-using-nginx)
