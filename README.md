# cloudformation-random-string
Generate a random string to use in your CloudFormation templates: which could then be used for example for an RDS master password.

## Usage

1. Create a new Lambda function with the code in lambda_function.py. No special permissions are required so it can run with the basic execution role.
2. Run up the sample template. Pass in the ARN of the lambda function.
3. Check out the output of the stack.

## Parameters

* Length (required)

The length of string to generate.

* Punctuation (optional, defaults false)

Include the punctuation characters in the generated string

* RDSCompatible (optional, defaults false)

If using for an RDS master password, do not include the characters /,@," in the generated random string.
These aren't allowed to be used in an RDS master password.

* KeyId (optional)

If specified, encrypt the random generated string with the KMS key identified by the KeyId parameter
and return it in the 'EncryptedRandomString' attribute. Obviously means that the lambda function needs
permission to encrypt with this key.



