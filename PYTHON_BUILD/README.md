# My Portfolio site

Built with Python & Flask
Delivered by Google App Engine

## Running

Setup runtime environment:

```shell
pipenv install --dev
```

Run the application with this:

```shell
pipenv run gunicorn -w 3 -b :5000 portfolio:app
```

Access the site at [http://localhost:5000](http://localhost:5000)
