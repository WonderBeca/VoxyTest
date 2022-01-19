# Word Counter

This is a simple web application that counts how many characters, words, sentences and paragraphs a sent text has.

## How to run

First you need to run:

`docker build -t word_counter:latest .`       

And then:

`docker run --rm -p 5000:5000 word_counter:latest`

Now everything is running and the application will be runing at : 

`http://localhost:5000/`

