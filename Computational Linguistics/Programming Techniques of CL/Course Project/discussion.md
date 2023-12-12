# Analysis process for the PCL1 Course Project:
## Automatic Plot Analysis

###### Group: Mert Erol, Andrea Scheck

## Part 0.
### A. Selected 3 books:
We picked the 3 most popular fiction books from Project Gutenberg: Alice in Wonderland, Dracula and Frankenstein

### B. Adapted the cleanup script:
* We added a function to the cleanup script that would remove the footer since our footer markers were not recognized by the ones in the end marker set. 
* We implemented the splitting function by creating a new text file and then writing every chapter which is not empty (and incrementing the chapter number in the file name).
* Mert created a very cool progress bar for the splitting process by using tqdm and the length of the chapter list
* We then worked on the main function, which requires the path to the original book file and the path to the output base directory.
The main function reads the original file, applies the strip_header function given by the tutors and the strip_footer function defined by us, saves the cleaned file and then applies the split_book_by_chapter function.

### C. Using grep:
* We created a python module which can search the entire cleaned text with the grep pattern: r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b' and count the number of matches
* We analyzed the found most common capitalized words and defined the most common names. Picking out the most common names was simple for Alice in Wonderland, but more difficult for Frankenstein and Dracula because several characters had first names, last names and titles. We decided to only use the one most common name per person.
* We then let added these specific names to the grep script alongside the sentiment words we had already defined:
        ```python
    names_pattern = r'\b(Alice|Queen|King|Gryphon|Hatter|Mock Turtle|Duchess|Dormouse|Mouse|Rabbit|Elizabeth|Clerval|Justine|Felix|Victor|Safie|Henry|William|Agatha|Kirwin|Van Helsing|Lucy|Jonathan Count|Arthur|Seward|Mina|Quincey|Renfield)\b'
    good_sentiment_pattern = r'\b(happy|joy|love|pleased|delighted|ecstatic|optimistic|satisfied|content|grateful|positive|successful|peaceful|enthusiastic|proud|thrilled|joyful|cheerful|amazing|fantastic|incredible|wonderful|exciting)\b'
    bad_sentiment_pattern = r'\b(sad|angry|frustrated|disappointed|depressed|unhappy|miserable|gloomy|hopeless|dismayed|discouraged|pessimistic|annoyed|upset|distressed|troubled|sorrowful|agitated|furious|resentful|displeased|fear|scared)\b'
    ```
* We made the script write the findings for all 3 categories per chapter into a txt-file

### D. Converting grep Results to JSON:
* We defined a function to convert the data to a json string. It takes a folder path as input, iterates over the files containing the names & sentiments and reads them.
*The function creates a dictionary for each category (name, good sentiments, bad sentiments)
* It then goes through every line and if it is not a specific string (title), it splits the line. If the resulting split is exactly 2 elements we know that it's the count of the word's occurence + the word itself. In this case, the content is added to the appropriate dictionary.
* We then defined the second function that takes the processed data and puts it into 3 different files in a defined file path. It names the files using the original file name as a basis.
* In the main function, we define the folders and call the 2 functions.