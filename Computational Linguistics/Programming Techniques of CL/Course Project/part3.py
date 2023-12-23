import os
import json
import matplotlib.pyplot as plt
from sys import argv

def count_sentiments(file_path):
    """
    Count the positive and negative sentiments in a given file.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    positive_count = len(data.get('Positive Sentiments', []))
    negative_count = len(data.get('Negative Sentiments', []))
    return positive_count, negative_count

def plot_sentiments(positive_sentiments, negative_sentiments, output_folder_path, output_file_name):
    """
    Plot the positive and negative sentiment counts as a line graph.
    """
    chapters = range(1, len(positive_sentiments) + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(chapters, positive_sentiments, color='green', marker='o', linestyle='-', label='Positive Sentiments')
    plt.plot(chapters, negative_sentiments, color='red', marker='o', linestyle='-', label='Negative Sentiments')
    plt.xlabel('Chapter')
    plt.ylabel('Number of Sentiments')
    plt.title('Sentiments per Chapter')
    plt.xticks(chapters)
    plt.legend()
    plt.grid(True)

    # Save the plot in the specified output folder with the specified file name
    output_file_path = os.path.join(output_folder_path, output_file_name)
    plt.savefig(output_file_path)
    plt.close()  # Close the plot to free up memory

def main(input_folder_path, output_folder_path, output_file_name):
    """
    Main function to process each JSON file in the folder and plot aggregated sentiments.
    """
    positive_sentiment_counts = []
    negative_sentiment_counts = []

    # Iterate through each file in the folder
    for file_name in sorted(os.listdir(input_folder_path)):
        if file_name.endswith('.json'):
            file_path = os.path.join(input_folder_path, file_name)
            positive_count, negative_count = count_sentiments(file_path)
            positive_sentiment_counts.append(positive_count)
            negative_sentiment_counts.append(negative_count)

    plot_sentiments(positive_sentiment_counts, negative_sentiment_counts, output_folder_path, output_file_name)
    
if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage: python3 script_name.py <input_folder_path> <output_folder_path> <output_file_name>')
        exit(1)
    
    input_folder_path = argv[1]
    output_folder_path = argv[2]
    output_file_name = argv[3]
    main(input_folder_path, output_folder_path, output_file_name)
