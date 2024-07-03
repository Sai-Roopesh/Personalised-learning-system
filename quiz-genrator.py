import vertexai
from vertexai.generative_models import GenerationConfig, GenerativeModel
import json
from dotenv import load_dotenv
from pdfminer.high_level import extract_text

load_dotenv()
# Set your Vertex AI project ID
project_id = "gemini-practice-sai"

# Initialize Vertex AI with your project ID and location
vertexai.init(project=project_id, location="us-central1")

# Load the response schema from JSON file
json_file = 'response-schema.json'


def pdf2text(filepath):
    return extract_text(filepath)


def load_json(file_path):
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    return json_data


response_schema = load_json(json_file)

# Function to prompt the generative model with a given prompt and schema


def prompt(model, prompt, response_schema):
    model_instance = GenerativeModel(model)

    response = model_instance.generate_content(
        prompt,
        generation_config=GenerationConfig(
            response_mime_type="application/json", response_schema=response_schema
        ),
    )

    return response


pdf_filepath = r"SE-M1.pdf"
text = pdf2text(pdf_filepath)
# Example prompt text (modify as needed)
prompt_text = f"Generate quiz questions for the given context: {text} with options and correct answers from the options generated."

# Example usage:
# Replace 'gemini-1.5-pro-001' with your actual model identifier
prompted_response = prompt(
    'gemini-1.5-pro-001', prompt_text, response_schema
)

# Print the generated response
print(prompted_response.text)
