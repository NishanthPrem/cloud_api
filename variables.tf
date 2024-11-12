variable db_name {
  description = "Database Table name"
  type = string
  default = "cloud-api-db"
}

variable "lambda_function_name" {
  description = "Name of the lambda function"
  type = string
  default = "cloud-api-lambda"
}