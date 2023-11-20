# Microservices Architecture

This project consists of four microservices (A, B, C, D), with service A exposed externally. The services communicate internally, and they are orchestrated using Docker Compose.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Run Services](#run-services)
  - [Run Tests](#run-tests)
  - [Access Shell](#access-shell)

## Overview

The project is organized into four microservices:

- **Main Service**: (Exposed externally)
- **Sentiment Analysis**: (Internal)
- **Word Count**: (Internal)
- **Entity Recognition**: (Internal)

These services are orchestrated using Docker Compose.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- make
- git
- docker
- docker-compose
- poetry

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hardikaj96/microservice-system-design.git
    ```

2. Navigate to the project directory:

    ```bash
    cd microservice-system-design
    ```

3. Build the Docker images:

    ```bash
    make build
    ```

## Usage

### Run Services

To run the services:

```bash
make up

```
To stop the services:

```bash
make down
```

### Run Tests

To run external tests, use the following command: (This will be ran inside Poetry shell within tests directory)

```bash
make test
```
Alternate solution: if Poetry cannot be installed, one can just install the dependencies from the `tests/requirements.txt` file and just run the tests using `pytest` inside `tests` directory. 

To run each internal service tests within the Docker containers:

```bash
make test-services
```

### Access Shell

To access the shell of Main Service:

```bash
make shell
```