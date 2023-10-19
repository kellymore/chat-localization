import boto3

# Initialize the Amazon Translate client
translate_client = boto3.client('translate', region_name='us-east-1')  # Change the region as needed

# List of user names
usernames = ["User1", "User2"]

# Prompt the user to choose a target language
target_language = input("Choose a target language (es for Spanish, pt for Portuguese): ").lower()
if target_language not in ["es", "pt"]:
    print("Invalid target language. Defaulting to Spanish.")
    target_language = "es"

while True:
    for user in usernames:
        message = input(f"{user}, enter a message (or type 'exit' to end): ")
        if message.lower() == "exit":
            exit(0)

        # Translate the user's input message
        translated_message = translate_client.translate_text(
            Text=message,
            SourceLanguageCode='en',  # Assuming the input language is English
            TargetLanguageCode=target_language
        )['TranslatedText']

        print(f"{user} ({target_language}): {translated_message}")

