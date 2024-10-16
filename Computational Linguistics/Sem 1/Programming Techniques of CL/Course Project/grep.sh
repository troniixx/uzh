# Chapter Directory of each book
chapter_dir="/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Chapters"
#chapter_dir="/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Chapters"
#chapter_dir="/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Franky/Chapters"

# Results Directory of each book
results_dir_ner="/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Results/named"
results_dir_sent="/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Alice/Results/sentiment"

#results_dir_ner="/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Results/named"
#results_dir_sent="/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Dracula/Results/sentiment"

#results_dir_ner="/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Franky/Results/named"
#results_dir_sent="/Users/merterol/Desktop/VSCode/uzh/Computational Linguistics/Programming Techniques of CL/Course Project/Franky/Results/sentiment"

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
    grep -oE "\b(Alice|Queen|King|Gryphon|Hatter|Mock Turtle|Duchess|Dormouse|Mouse|Rabbit|Elizabeth|Clerval|Justine|Felix|Victor|Safie|Henry|William|Agatha|Kirwin|Van Helsing|Lucy|Jonathan|Count|Arthur|Seward|Mina|Quincey|Renfield)\b" "$file" | sort | uniq -c | sort -nr >> "$output_file"
    
    # Grep for basic sentiment words
done

for file in "$chapter_dir"/*; do

    # Extract filename without path for naming the results file and remove .txt from the chapter file
    filename=$(basename "$file" .txt)
    
    # Define the output file for the results and add .txt back
    output_file="$results_dir_sent/${filename}_sentiment.txt"

    echo "Sentiment Analysis for $file..."
# Grep for basic sentiment words
    echo -e "Sentiment Expressions:" >> "$output_file"
    echo -e "Positive Sentiments:\n" >> "$output_file"
    grep -owiE "\b(happy|joy|love|pleased|delighted|ecstatic|optimistic|satisfied|content|grateful|positive|successful|peaceful|enthusiastic|proud|thrilled|joyful|cheerful|amazing|fantastic|incredible|wonderful|exciting)\b" "$file" | sort | uniq -c | sort -nr >> "$output_file"
    echo -e "\nNegative Sentiments:\n" >> "$output_file"
    grep -owiE "\b(sad|angry|frustrated|disappointed|depressed|unhappy|miserable|gloomy|hopeless|dismayed|discouraged|pessimistic|annoyed|upset|distressed|troubled|sorrowful|agitated|furious|resentful|displeased|fear|scared)\b" "$file" | sort | uniq -c | sort -nr >> "$output_file"
done

echo "Analysis complete. Results saved in ${results_dir_sent#*/Course Project/} and ${results_dir_ner#*/Course Project/}"

# ggrep -P didnt work for some reason so i just used normal grep
# -o: print only the match
# -w: match only whole words
# -i: ignore case
# -E: extended regex