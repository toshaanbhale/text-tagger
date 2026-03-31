# Text Tagger (CLI Tool)

A simple command-line tool that reads a text file and assigns it a category.

## Features

- Reads plain text files
- Classifies content into predefined categories
- Fast and lightweight
- Easy to extend

## Categories

- AI
- Programming
- Finance
- Health

## Setup

Install dependencies:

pip install -r requirements.txt

## Train the Model

python models/train.py

## Usage

python main.py sample.txt

## Example Output

File: sample.txt  
Predicted Tag: AI

## Notes

- The model is trained on a small dataset for demonstration purposes
- You can expand the dataset in `data/dataset.csv` to improve results

## Project Structure

- data/ → training data
- models/ → trained model files
- src/ → core logic
- main.py → CLI entry point

## Future Improvements

- Support multiple tags
- Improve dataset quality
- Add batch processing
