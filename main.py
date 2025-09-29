import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys



def main():
    print("Hello from wagent!")
    user_prompt = sys.argv[1]
    if "--verbose" in sys.argv:
        verbose = True
    else:
        verbose = False

    # print(f"Input string: {input_string}")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages)
    print(response.text)
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
