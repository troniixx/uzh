# Analysis process for the PCL1 Course Project

## Automatic Plot Analysis

###### Group: Mert Erol, Andrea Scheck

## Part 0

### A. Selected 3 books

We picked the 3 most popular fiction books from Project Gutenberg: Alice in Wonderland, Dracula and Frankenstein

### B. Adapted the cleanup script

* We added a function to the cleanup script that would remove the footer since our footer markers were not recognized by the ones in the end marker set.
* We implemented the splitting function by creating a new text file and then writing every chapter which is not empty (and incrementing the chapter number in the file name).
* Mert created a very cool progress bar for the splitting process by using tqdm and the length of the chapter list
* We then worked on the main function, which requires the path to the original book file and the path to the output base directory.
The main function reads the original file, applies the strip_header function given by the tutors and the strip_footer function defined by us, saves the cleaned file and then applies the split_book_by_chapter function.

### C. Using grep

* We created a python module which can search the entire cleaned text with the grep pattern: r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b' and count the number of matches
* We analyzed the found most common capitalized words and defined the most common names. Picking out the most common names was simple for Alice in Wonderland, but more difficult for Frankenstein and Dracula because several characters had first names, last names and titles. We decided to only use the one most common name per person.
* We then let added these specific names to the grep script alongside the sentiment words we had already defined:

    names_pattern = r'\b(Alice|Queen|King|Gryphon|Hatter|Mock Turtle|Duchess|Dormouse|Mouse|Rabbit|Elizabeth|Clerval|Justine|Felix|Victor|Safie|Henry|William|Agatha|Kirwin|Van Helsing|Lucy|Jonathan Count|Arthur|Seward|Mina|Quincey|Renfield)\b'

    good_sentiment_pattern = r'\b(happy|joy|love|pleased|delighted|ecstatic|optimistic|satisfied|content|grateful|positive|successful|peaceful|enthusiastic|proud|thrilled|joyful|cheerful|amazing|fantastic|incredible|wonderful|exciting)\b'

    bad_sentiment_pattern = r'\b(sad|angry|frustrated|disappointed|depressed|unhappy|miserable|gloomy|hopeless|dismayed|discouraged|pessimistic|annoyed|upset|distressed|troubled|sorrowful|agitated|furious|resentful|displeased|fear|scared)\b'

* We made the script write the findings for all 3 categories per chapter into one singular txt-file

### D. Converting grep Results to JSON

* We defined a function to convert the data to a json string. It takes a folder path as input, iterates over the files containing the names & sentiments and reads them.
* The function creates a dictionary for each category (name, good sentiments, bad sentiments)
* It then goes through every line and if it is not a specific string (title), it splits the line. If the resulting split is exactly 2 elements we know that it's the count of the word's occurence + the word itself. In this case, the content is added to the appropriate dictionary.
* We then defined the second function that takes the processed data and puts it into 3 different files in a defined file path. It names the files using the original file name as a basis.
* In the main function, we define the folders and call the 2 functions.

Submitting

* gutenberg_cleanup_incl_footer.py: contains functions for stripping the header, the footer and splitting the cleaned text into chapters
* grep_for_specific_names.py: contains our full grep and the definition how files should be saved
* part0.py: contains the functions to convert .txt files to JSON and write the result.
* Folder containing subfolders for each book, with chapter files, grep results and JSON files for entities and sentiments per chapter.

## Part 1

### Approach

We first started by thinking how we can get our output json files as close to the demo one on the project pdf. After coding a very basic version of the output format (which in our case was just outputting a nested dictionairy on the terminal) we realized that we need to change our approach because punctuations and other random characters were reprensted inside the nested dictionaries.
This lead us to write some functions that help clean up the text by removing white spaces and various punctuations to make it cleaner.
All of this above was done by just using the paths of the books hardcoded. After realizing that our code works we started to make it more dynamic by adding command line arguments. This way we could just run the code by typing the following command in the terminal:

```bash
    python3 part1.py franky_cleaned.txt Chapters JSON_part1 Franky_json
```

The first argument is the path to the cleaned text file, the second argument is the path to the folder where the chapters are located, the third argument is the path to the folder where the json files will be saved and the last argument is the name of the json file.

Eventhough this worked, we still had to make small changes into the code to make sure the json files are displaying text correctly without using any escape characters or special escape codes to represent certain symbols. We did this by adding the following line of code:

```python
    json.dump(data, json_file, indent=4, ensure_ascii=False)
```

Finally after making sure that everything works as intended, we added a fancy progress bar again using tqdm :-) and also added some comments to make the code more readable. We then ran all the books through it and got all our json files.

### Challenges

* Sometimes we realized that we coded things that were already done by a different function.
* This lead us to refactor the code multiple times to make sure we are not doing redundant work and still keeping the code clean and readable.
* The json files outputted had some weird characters in them. It took a long time to figure out how to remove them.
* Finding aliases for characters was a pain. We tried to use a spacy model but then it also considered corefs inside the sentece as aliases which lead to "She" being an aliases for all female characters.

## Part 2

### Picking a tool

We analyzed a particularly negative text from Frankenstein with Textblob, VADER and Flair:

* Textblob: ['oppressed', 'various misfortunes', 'usual quantity', 'towards', "fiend 's grasp", 'cries rang', 'cloudy sky']
Sentiment(polarity=0.024999999999999994, subjectivity=0.42500000000000004)
* NRCLex: {'fear': 0.14705882352941177, 'anger': 0.11764705882352941, 'anticip': 0.0, 'trust': 0.11764705882352941, 'surprise': 0.0, 'positive': 0.17647058823529413, 'negative': 0.14705882352941177, 'sadness': 0.058823529411764705, 'disgust': 0.11764705882352941, 'joy': 0.058823529411764705, 'anticipation': 0.058823529411764705}
* VADER: {'neg': 0.189, 'neu': 0.779, 'pos': 0.032, 'compound': -0.9539}
* Flair: NEGATIVE (0.9979)
* SpaCy: Polarity: 0.024999999999999994, Subjectivity: 0.42500000000000004

We retested SpaCy with a very positive text from Alice in Wonderland to make sure the positive interpretation was not a fluke.
But even for the very positive text, it only gave a polarity of 0.21, so we decided VADER and Flair were good results.
VADER ran smoothest and the tutor said it was allowed, so we went with that.

### Grepping sentences with main characters in them

We created a grep function that would work for each of the books and roughly match sentences in which the 5 main characters per book were mentioned.
This was tricky because the books have a different writing style: Alice in Wonderland is written in the third person with lots of name references and direct speech, Dracula and Frankenstein contain a lot of retelling in the "I" form. Unfortunately, we only found out that we were allowed to pick just 1 book after we already made the grep, so we decided to stick with it.
Because the books contain formatting choices and unusual characters, we cleaned them up a little.
This script could be run over the entire book, but we decided to run it with the chapter files we created in part0. This way, we could use the file names (chapter_0, chapter_1 etc.) as information for later, when we want to aggregate values for entire chapters.

### Doing sentiment Analysis and saving everything

We made a Vader function to go over the grepped sentences and assign a sentiment value. All the info so far (sentences, value and chapter name) should then be written to a txt file. This way, we can easily perform a sanity check and just look at how the results change if we add more functions or play with the grep.

### Making JSON files

We wrote a function that would extract only the values for character name, sentiment value and chapter name from each sentence in the txt file. It saves those infos in a JSON file.
Another function then goes over this JSON file and averages the sentiment values per character and per chapter.
This might seem redundant, but again, creating 2 files allowed us to perform sanity checks and actually look if the averages were correct and no values were lost. For a more refined script, this middle step could be removed and only the final averaged JSON file created.

### Result

Running our module results in 3 files:

* txt file with grepped sentences, sentiment values and chapter names

* JSON file with only character name, sentiment value and chapter name from each sentence in the txt file

* JSON file with the average sentiment value for every chapter for each main character

This works for all 3 of our books and we decided to pick the one with the most interesting results for the further visualisation.

## Part 3: Visualization

For the results from Part 2, we did simple line plots to track the emotions of the main characters across the chapters.
We also overlapped the line plots and compared these results with the content of the book.
Additionally, we created box plots which allow us more insight into outliers and the distribution of data in detail.
For the results from Part 0, we tracked the occurences of positive and negative emotions across the entire book. In this part we had to
change the code a little bit to make it easier for us to plot the data. The change we made is that the code sorts the sentiments already into positive and negative sentiments.
This way we could just get the length of the list of positive and negative sentiments and plot them.

## Part 4: Reflection and Discussion

Our learning experience, project insights, and real-world applicability.

a. Learning and Challenges

* Comparing the results of grep and the more in-depth NLP analysis, what are the key insights?
The grep for part 0 probably was much better at capturing all occurences, as it was simpler. The more context we had to add (to capture entire sentences with the main character names, the

* You were asked to visualise both methods. How do they differ?

* Summarize key learnings, focusing on technical skills and literary insights.

* Briefly discuss major challenges and how you addressed them, particularly moving from basic grep searches to advanced NLP.

b. Analysis Insights and Real-World Applicability

* Describe significant insights from the book analysis and how advanced NLP tools enhanced your initial grep findings.

* Reflect on how these techniques and insights could apply in real-world contexts, like social media analysis or other literary works.

## --- Feedback

The project was very interesting overall. However the instructions were not given in a  clear way and this led to quite a lot of frustration. For example, in part 1 and 2, we tried to apply our code to all 3 books and only found out quite late that we could have picked just 1. Also, the comparison between the results of part 0 and part 2 in part 3 did not seem sensible because the instructions for creating the results for part 0 were too ambigious. Of course we came up with something to compare, but it really did not feel very worthwile. If we'd been instructed in part 0 to grep the names and sentiments together, we could have avoided this.
