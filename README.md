# URL Shortener


[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

The URL Shortener is a web application built with Django, Django Rest Framework, and Alpine.js. It allows users to shorten long URLs into shorter, more manageable links. The project also includes a click tracking feature, which records the total number of clicks made on each shortened link.

With this URL Shortener, you can easily share long URLs without having to remember or type them. Additionally, you can track how many times each shortened link has been accessed, providing valuable insights into link popularity and usage.

**Project URL:** [http://sh.jajobs.gq/](http://sh.jajobs.gq/)

## Features

- Shorten long URLs into concise, easy-to-share links.
- Track the total number of clicks made on each shortened link.

## Installation and Deployment

To deploy the URL Shortener using Docker and Docker Compose with MySQL, make sure you have Docker and Docker Compose installed on your system. Then follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/ricardowebleyjm/url_shortner.git
```
2. Change to the project directory:

```bash
cd url_shortner
```
3. Edit the .env.example file and configure the settings:
```bash
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=url_shortener_db
DB_USER=url_shortener_user
DB_PASSWORD=url_shortener_password
DB_HOST=db
DB_PORT=3306
```

4. Run the application using docker compose:

```bash
docker-compose up 

```

5. Test the application:
```bash
http://localhost:8000
```