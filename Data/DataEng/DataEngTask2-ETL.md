# ETL

Now we want you to extract and transform data before loading it into a database.

## Extract

Read all the data from the **[Midsummer Nights Dream by William Shakespeare Download Here](data/a-midsummer-nights-dream.txt)**.

## Transform

The aim of this task is to extract every character and every word from the play.  Task 1 should help with the words, and you can use something similar for the characters.

All characters should be in lowercase, so that we can accurately compare each character and word.

### Optional extra 300+ level

Add the detail to identify the words and number of occurrences per Act.

## Load

You should have a Postgres or Mongo database that will allow you to store characters as a separate entity from words.

Your data should be stored as:

Character table/collection
* character
* number occurrences

Word table/collection
* Word
* number occurrences

### Optional 300+

Add the Acts to your database to store the words and characters count to the acts.