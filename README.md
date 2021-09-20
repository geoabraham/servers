# Servers Service

This repository contains a basic TDD example for building a
python service.

## Setup

For starting the developer environment:

    make init

Running unit tests:

    make unit-test

Running integration tests:

    make integration-test

## Server Model

```json
{
    "id": "uuid",
    "customer_id": "uuid",
    "hostname": "string",
    "os": "linux|windows",
    "ram": "int",
    "cpu": "intel|amd"
}
```
