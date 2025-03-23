from langchain.chains import LLMChain
from langchain_community.chat_models import ChatSnowflakeCortex
# # from mistral import MistralSmall
# from langchain_openai import OpenAI
import openai 
import os 
# import getpass
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv() # Load environment variables

# Set OpenAI API key
# os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"
chat = ChatSnowflakeCortex()

# Initialize LangChain with OpenAI model
openai.api_key = api_key=os.environ.get("OPENAI_API_KEY")
# model = openai()
# Initialize LangChain with Mistral small model
# model = OpenAI()
# chat_model = ChatSnowflakeCortex(model=model)


chat_model = init_chat_model("gpt-4o-mini", model_provider="openai")
# langchain = LLMChain(model=model, chat_model=chat_model)
# model.invoke("Hello, how are you?")

# Define a function to perform semantic search
def semantic_search(query, data):
    # results = langchain.search(query, data)
    results = chat_model.invoke.search(query, data)
    return results

# # /Users/almazina/dev/db/snowflake/coplitbased/snowflake-genAI/langchain-snowflake/app.py
# import getpass
# import os

# if not os.environ.get("OPENAI_API_KEY"):
#   os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# from langchain.chat_models import init_chat_model

