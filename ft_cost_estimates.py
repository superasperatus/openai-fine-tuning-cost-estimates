import json
import tiktoken  # Make sure that tiktoken is installed

def count_tokens_in_jsonl(jsonl_file_path, encoding_name='cl100k_base'):
    """
    This function counts the number of tokens for the serialized JSON object on each line of a JSONL file.

    Parameters:
    jsonl_file_path (str): Path to the JSONL file.
    encoding_name (str): The encoding to use for tokenization (default is 'cl100k_base').

    Returns:
    int: The total number of tokens across all JSON objects in the file.
    """
    total_token_count = 0
    encoding = tiktoken.get_encoding(encoding_name)

    with open(jsonl_file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):
            try:
                # Parse JSON to ensure it's valid
                json_object = json.loads(line)
                
                # Serialize JSON object back to string
                text_content = json.dumps(json_object, ensure_ascii=False)
                
                # Tokenize and count
                token_count = len(encoding.encode(text_content))
                total_token_count += token_count
                
                # Optional: Print the number of tokens in this line
                print(f"Line {line_number}: {token_count} tokens")

            except json.JSONDecodeError as e:
                print(f"Error parsing JSON on line {line_number}: {e}")

    return total_token_count

# Usage:
jsonl_file_path = 'jsonl-to-estimate.jsonl'  # Replace with your JSON Lines file path
total_tokens = count_tokens_in_jsonl(jsonl_file_path)
print(f"Total tokens across entire file: {total_tokens}")

cost_estimates = (total_tokens / 1000) * 0.0080 * 3 #calculating costs based on pricing https://openai.com/pricing; number 3 is number of epoch used for fine-tuning

print(f"Estimated costs for fine-tuning this jsonl is: $ {cost_estimates}")
