[![AWS Lambda Package, Deploy and Test](https://github.com/pawanJ09/expense-category-fetcher/actions/workflows/aws-lambda-package.yml/badge.svg)](https://github.com/pawanJ09/expense-category-fetcher/actions/workflows/aws-lambda-package.yml)

# Expense Category Fetcher

This app will fetch all the expense categories from DynamoDB.

## Requirements

For building and running the application you need:

- [Python3](https://www.python.org/downloads/)

```shell
pip3 install -r requirements.txt
```
OR
```shell
pip install -r requirements.txt
```

## Running the application locally

You can run the main.py program to get started. This file has the __main__ method.

```shell
python3 ./src/main.py
```
OR
```shell
python ./src/main.py
```

## Trigger AWS Lambda with Test event from cli

```shell
aws lambda invoke --function-name expense-category-fetcher --invocation-type RequestResponse \
--payload file://events/test-sqs-event.json cli-binary-format raw-in-base64-out /dev/stdout
```

