# My Portfolio site

Built with Python & Flask. Delivered as a stateless container

## Running

Build the container with something like:

```
docker build -t localhost/portfolio:latest .
```

Run the resulting image like this:

```
docker run --rm -p 5000:5000 localhost/portfolio:latest
```

Access the site at [http://localhost:5000](http://localhost:5000)

