import argparse
from lib import plotlib  
# Import the function from the code/lib folder

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plot histogram and vertical line.')
    parser.add_argument('--data', type=str, help='Path to the input data file (CSV)')
    parser.add_argument('--model', type=str, help='Path to the model file (YAML)')
    parser.add_argument('--output', type=str, help='Path to the output plot file')

    args = parser.parse_args()
    
    # Call the imported function
    plot_histogram(args.data, args.model, args.output)