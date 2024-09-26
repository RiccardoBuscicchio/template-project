import yaml
import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram(data_file, model_file, output_file):
    # Load data from CSV
    data = pd.read_csv(data_file)
    
    # Assuming the data is in the first column
    values = data.iloc[:, 0]
    
    # Load model from YAML
    with open(model_file, 'r') as stream:
        model = yaml.safe_load(stream)
    
    # Get the number for the vertical line from the model (assuming the key is 'number')
    vertical_line_value = model['number']
    
    # Plot the histogram
    plt.figure(figsize=(8, 6))
    plt.hist(values, bins=30, alpha=0.7, label='Data')
    
    # Plot the vertical line
    plt.axvline(vertical_line_value, color='r', linestyle='--', label=f'Value: {vertical_line_value}')
    
    # Add labels and title
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram with Vertical Line')
    plt.legend()
    
    # Save the plot
    plt.savefig(output_file)
    plt.close()