
# Cloud API with AWS Lambda and DynamoDB

This project sets up a Lambda function that reads data from an AWS DynamoDB table and returns it as a JSON response via a Lambda function URL. The project is managed using Terraform and includes CI/CD pipelines configured with GitHub Actions to automate infrastructure deployment and testing.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
4. [Terraform Configuration](#terraform-configuration)
5. [Testing the Lambda Function](#testing-the-lambda-function)
6. [Usage](#usage)
7. [Project Structure](#project-structure)
8. [Improvements](#improvements)

## Project Overview

- **AWS Lambda**: A function that queries data from a DynamoDB table and returns it as a JSON response.
- **DynamoDB**: A table (`cloud-api-db`) storing the data that the Lambda function queries.
- **CI/CD**: Continuous Integration and Continuous Deployment pipelines configured with GitHub Actions to automate the deployment and testing of the Lambda function.

![alt text](image.png)

## Prerequisites
- **AWS Account** with programmatic access.
- **Terraform** (v1.0 or higher).
- **AWS CLI** configured with the necessary permissions.
- **Python 3.12** or compatible Python runtime.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/cloud-api
   cd cloud-api
   ```

2. **Configure AWS CLI**:
   Ensure your AWS CLI is configured to access your AWS account:
   ```bash
   aws configure
   ```

3. **Initialize Terraform**:
   ```bash
   terraform init
   ```

4. **Apply the Terraform Configuration**:
   This step will create the DynamoDB table, IAM roles, Lambda function, and Lambda Function URL.
   ```bash
   terraform apply
   ```
   Type `yes` when prompted to confirm.

5. **Upload Lambda Function Code**:
   Ensure your Lambda function code (`lambda_function.py`) is available in the project directory. Terraform will package it and deploy it to AWS.

## Terraform Configuration
The Terraform configuration does the following:

- Creates a **DynamoDB** table (`cloud-api-db`) to store JSON data.
- Sets up an **IAM Role** and **Policy** to grant Lambda access to DynamoDB.
- Deploys a **Lambda Function** (`cloudApiLambda`) that retrieves data from DynamoDB.
- Configures a **Lambda Function URL** to enable HTTP access to the function.

### Key Terraform Resources
- `aws_dynamodb_table`: Creates the DynamoDB table.
- `aws_iam_role` & `aws_iam_policy`: Define permissions for the Lambda function.
- `aws_lambda_function`: Deploys the Lambda function.
- `aws_lambda_function_url`: Exposes the Lambda function with a publicly accessible URL.

## Testing the Lambda Function
To test the Lambda function, use a `curl` command or a tool like Postman:

```bash
curl -X GET <your_lambda_function_url>
```

If everything is set up correctly, this should return the JSON data from your DynamoDB table.

## Usage
### Adding Data to DynamoDB
Manually add items to the DynamoDB table (`cloud-api-db`) via the AWS Console or CLI.

Example CLI command to add data:
```bash
aws dynamodb put-item     --table-name cloud-api-db     --item '{
        "id": {"S": "resume"},
        "basics": {"M": {
            "name": {"S": "Nishanth Prem"},
            "email": {"S": "nishanthprem8@gmail.com"},
            "phone": {"S": "(623) 632-8787"},
            "location": {"M": {
                "city": {"S": "Tempe"},
                "countryCode": {"S": "USA"},
                "region": {"S": "California"}
            }}
        }}
    }'
```

## Project Structure
- **`main.tf`**: Contains all Terraform resources to deploy the Lambda function, DynamoDB table, and IAM policies.
- **`variables.tf`**: Defines project-specific variables, including the DynamoDB table name and region.
- **`lambda_function.py`**: The Lambda function code for querying DynamoDB and returning the JSON response.
- **`outputs.tf`**: Outputs the Lambda Function URL after deployment.
- **`data`**: (Optional) Contains the data to be uploaded to DynamoDB in JSON format.

## Improvements

- Limit IAM permissions to specific resources.
- Enable CloudWatch logging for Lambda and DynamoDB.
