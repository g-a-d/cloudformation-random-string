# cloudformation-random-string
Generate a random string to use in your CloudFormation templates: which could then be used for example for an RDS master password.

## Usage

1. Create a new Lambda function with the code in lambda_function.py. No special permissions are required so it can run with the basic execution role.
2. Run up the sample template. Pass in the ARN of the lambda function.




