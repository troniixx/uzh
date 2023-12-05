# Chapter Directory of each book
#chapter_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Chapters"
#chapter_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Chapters"
chapter_dir="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/Chapters"

# Results Directory of each book
#results_dir_ner="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Results/named"
#results_dir_sent="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Results/sentiment"

#results_dir_ner="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Results/named"
#results_dir_sent="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Results/sentiment"

results_dir_ner="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/Results/named"
results_dir_sent="/Users/merterol/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Frankenstein/Results/sentiment"

# Create the results directory if it doesn't exist
mkdir -p "$results_dir_ner"
mkdir -p "$results_dir_sent"

for file in "$chapter_dir"/*; do
    echo "NER for $file..."

    # Extract filename without path for naming the results file and remove .txt from the chapter file
    filename=$(basename "$file" .txt)
    
    # Define the output file for the results and add .txt back
    output_file="$results_dir_ner/${filename}_ner.txt"

    # Grep for capitalized words (potential named entities)
    echo "Named Entities:" > "$output_file"
    grep -oE '\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*(?:\s(City|Town|Village|Country|Province|State))?\b' "$file" | sort | uniq -c | sort -nr >> "$output_file"
    
    # Grep for basic sentiment words
done

for file in "$chapter_dir"/*; do

    # Extract filename without path for naming the results file and remove .txt from the chapter file
    filename=$(basename "$file" .txt)
    
    # Define the output file for the results and add .txt back
    output_file="$results_dir_sent/${filename}_sentiment.txt"

    echo "Sentiment Analysis for $file..."
# Grep for basic sentiment words
    echo -e "\nSentiment Expressions:" >> "$output_file"
    grep -owiE '\b(happy|joy|love|pleased|delighted|ecstatic|optimistic|satisfied|content|grateful|positive|successful|peaceful|enthusiastic|proud|thrilled|joyful|cheerful|amazing|fantastic|incredible|wonderful|exciting)\b' "$file" | sort | uniq -c | sort -nr >> "$output_file"
    grep -owiE '\b(sad|angry|frustrated|disappointed|depressed|unhappy|miserable|gloomy|hopeless|dismayed|discouraged|pessimistic|annoyed|upset|distressed|troubled|sorrowful|agitated|furious|resentful|displeased)\b' "$file" | sort | uniq -c | sort -nr >> "$output_file"
done

echo "Analysis complete. Results saved in ${results_dir_sent#*/Course Project/} and ${results_dir_ner#*/Course Project/}"

# ggrep didnt work for some reason so i just used grep -E
# -o: print only the match
# -w: match only whole words
# -i: ignore case
# -E: extended regex