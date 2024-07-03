import json
import streamlit as st

# Load the simplified contents from JSON file
simplified_contents_file = 'simplified_contents.json'


def load_json(file_path):
    with open(file_path, 'r') as f:
        json_data = json.load(f)
    return json_data


simplified_contents = load_json(simplified_contents_file)

st.title("Simplified Content Viewer")


def parse_simplified_content(content):
    try:
        parsed_content = json.loads(content)
        # Flatten the parsed content for display
        if isinstance(parsed_content, dict):
            return ' '.join(str(value) for value in parsed_content.values())
        elif isinstance(parsed_content, list):
            return ' '.join(str(item) for item in parsed_content)
        else:
            return str(parsed_content)
    except json.JSONDecodeError:
        return content  # Return the original content if it can't be parsed


if st.button('Fetch Simplified Content'):
    st.write("Simplified Content for Incorrect Answers:")
    for sc in simplified_contents:
        st.subheader(f"Question {sc['question-number']}")
        st.write(f"{sc['question']}")
        simplified_content_parsed = parse_simplified_content(
            sc['simplified_content'])
        st.write(f"Simplified Content: {simplified_content_parsed}")
