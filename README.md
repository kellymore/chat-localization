# chat-localization

After configuring aws in your local machine, simply run the   chat.py   file to experience Amazon Translate's real-time translation

The access keys (AWS Access Key ID and AWS Secret Access Key) are not directly included in this particular code snippet. Instead, the code relies on the AWS SDK for Python (Boto3) to locate and use these credentials from the AWS credential provider chain.

The AWS credential provider chain typically looks for credentials in various sources, including environment variables, AWS configuration files, IAM roles if the code is running on an AWS resource, and other methods.

You can choose to add more target languages to the experience by adding the following [supported language codes](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html) and altering the input prompt:

```

# Prompt the user to choose a target language
target_language = input("Choose a target language (es for Spanish, pt for Portuguese): ").lower()
if target_language not in ["es", "pt"]:
    print("Invalid target language. Defaulting to Spanish.")
    target_language = "es"

```
