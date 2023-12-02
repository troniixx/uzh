# Directory where chapter files are located
#chapter_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Chapters"
chapter_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Chapters"
#chapter_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Chapters"

# Directory where you want to save the analysis results
#results_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Results"
results_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Results"
#results_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/Results"

# Create the results directory if it doesn't exist
mkdir -p "$results_dir"

for file in "$chapter_dir"/*; do
    echo "Analyzing $file..."

    # Extract filename without path for naming the results file
    filename=$(basename "$file")
    
    # Define the output file for the results
    output_file="$results_dir/${filename}_analysis.txt"

    # Grep for capitalized words (potential named entities)
    echo "Named Entities:" > "$output_file"
    grep -oE '\b[A-Z][a-z]+' "$file" | sort | uniq -c | sort -nr >> "$output_file"
    
    # Grep for basic sentiment words
    echo -e "\nSentiment Expressions:" >> "$output_file"
    grep -owiE 'happy|joy|sorrow|sad|love|hate|excited|angry|afraid|peaceful' "$file" | sort | uniq -c | sort -nr >> "$output_file"
done

echo "Analysis complete. Results saved in $results_dir"
