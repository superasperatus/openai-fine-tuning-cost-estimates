# Fine-tuning cost estimates

This script `token_counter.py` provides a utility to count the total number of tokens across all JSON objects in a JSON Lines file (JSONL). It uses the `tiktoken` library for tokenization, which you should ensure is installed before using the script.

## Installation

To run this script, you will need Python and the `tiktoken` package installed on your system. If you do not have `tiktoken` installed, you can install it using pip:

```bash
pip install tiktoken
```

## Usage
To use this script, simply call it with the path to your JSONL file as an argument:

```
python token_counter.py jsonl-to-estimate.jsonl
```

Replace jsonl-to-estimate.jsonl with the path to your own JSONL file.

## Script Function
The script defines a function `count_tokens_in_jsonl`, which processes a JSONL file and counts the number of tokens in each line. A summary of total tokens and estimated costs for fine-tuning is printed to the console.

## Function Parameters
`jsonl_file_path`: Path to the JSONL file.
`encoding_name`: The encoding to use for tokenization (default is 'cl100k_base').

### Returns
The function returns the total number of tokens across all JSON objects in the file.

## Example Cost Estimates Output
The script will produce output similar to the following:

```
Line 1: 123 tokens
Line 2: 456 tokens
...
Total tokens across entire file: 123456
Estimated costs for fine-tuning this jsonl is: $ X.XX
```

The estimated costs are calculated based on the OpenAI Pricing as follows: (total_tokens / 1000) * 0.0080 * number_of_epochs.

## Contributing
Feel free to fork this repository and submit pull requests to contribute to the script's development.

## Disclaimer
Please ensure that you comply with the tiktoken library's licensing and usage guidelines. The cost estimate is indicative and based on publicly available pricing at the time of writing; actual costs may vary.

## Contact
If you have any questions or feedback regarding this script, please open an issue in the GitHub repository.
