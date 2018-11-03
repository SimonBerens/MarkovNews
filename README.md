# MarkovNews

## What is this?
This website pulls article headings and summaries from a variety of sources, such as the New York Times, Wall Street Journal, and NPR News, and constructs sometimes reasonable and other times funny sounding article headings and summaries using markov chains.

## How does it get data?
Markov News scrapes the New York Times, Wall Street Journal, and NPR news for titles and summaries, using Beautiful Soup 4.

## What are markov chains?
Markov chains are giant matrices. In the case of text, they create a square* matrix of size however many unique words there are. Then, for each word in a row, they count how many times that word has followed the word of the row. To generate a chain, you randomly select a word based on how many times it has appeared after the current word you just generated. 

\* In reality, most of the values in the matrix would be 0 so you would optimize it by using a hash map of arrays or something similar, and add words in as you go along.