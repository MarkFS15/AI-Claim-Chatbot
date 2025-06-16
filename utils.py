from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.providers.google_gla import GoogleGLAProvider
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_model():
    model_name = os.getenv('MODEL_CHOICE')  # default fallback
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from the environment variables.")
    
    provider = GoogleGLAProvider(api_key=api_key)
    return GeminiModel(model_name, provider=provider)

# Create the agent globally
from pydantic_ai import Agent

# agent = Agent('google-gla:gemini-2.0-flash')

# # Run a test query when executing this file directly
# if __name__ == "__main__":
#     response = agent.run_sync("Explain quantum computing in simple terms.")
#     print(response.output)
