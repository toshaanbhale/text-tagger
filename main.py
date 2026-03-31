import argparse
from src.tagger import Tagger
from src.utils import read_file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to text file")
    args = parser.parse_args()

    text = read_file(args.file)

    tagger = Tagger()
    tag = tagger.predict(text)

    print("\n📄 File:", args.file)
    print("🏷️ Predicted Tag:", tag)

if __name__ == "__main__":
    main()
