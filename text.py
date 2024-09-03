import openai

# Replace with your actual API key
openai.api_key = 'API - KEY - UPDATE - HERE'

def complete_text(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use a supported model
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=50  # Adjust as needed
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    try:
        user_prompt = input("Enter a prompt: ")
        completion = complete_text(user_prompt)
        print("\nGenerated Text:")
        print(completion)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Keep the window open
    input("\nPress Enter to exit...")
