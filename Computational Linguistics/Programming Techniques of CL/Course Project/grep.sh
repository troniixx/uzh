# Chapter Directory of each book
#chapter_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Chapters"
#chapter_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Chapters"
chapter_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Chapters"

# Results Directory of each book
#results_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Results"
#results_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Results"
results_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/Results"

# Create the results directory if it doesn't exist
mkdir -p "$results_dir"

for file in "$chapter_dir"/*; do
    echo "Analyzing $file..."

    # Extract filename without path for naming the results file and remove .txt from the chapter file
    filename=$(basename "$file" .txt)
    
    # Define the output file for the results and add .txt back
    output_file="$results_dir/${filename}_analysis.txt"

    # Grep for capitalized words (potential named entities)
    echo "Named Entities:" > "$output_file"
    grep -oE '\b[A-Z][a-z]+' "$file" | sort | uniq -c | sort -nr >> "$output_file"
    
    # Grep for basic sentiment words
    echo -e "\nSentiment Expressions:" >> "$output_file"
    grep -owiE 'happy|joy|sorrow|sad|love|hate|excited|angry|afraid|peaceful|regret|doubt|adore|depressed|' "$file" | sort | uniq -c | sort -nr >> "$output_file"
done

echo "Analysis complete. Results saved in $results_dir"
