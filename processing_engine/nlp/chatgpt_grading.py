import openai
import json

openai.api_key = 'YOUR_OPENAI_API_KEY'

data = {
    "student_id": "123456",
    "subject": "Reading comprehension questions for the book titled 'Animal Farm'",
    "questions": "1. Who are the main characters in 'Animal Farm' and what are their roles?  2. What is the main theme of 'Animal Farm'? 3. How does George Orwell use animals to represent human characteristics in 'Animal Farm'? 4. What does the windmill symbolize in 'Animal Farm'? 5. How does 'Animal Farm' end and what does this signify?",
    "solutions": "1.  The main characters in 'Animal Farm' are Old Major, Napoleon, and Snowball. Old Major is a wise and respected pig who inspires the rebellion with his ideas of animal equality. Napoleon is another pig who becomes the leader of Animal Farm after the Rebellion. He gradually takes more power and becomes a dictator, mirroring the human farmer Mr. Jones. Snowball is a pig who is initially a leader of the rebellion and has many ideas for the farm's improvement. However, he is chased away by Napoleon and his guard dogs, allowing Napoleon to seize control of the farm. 2.  The main theme of 'Animal Farm' is that power can corrupt those who possess it. At the beginning of the story, the animals hope for a society where all animals are equal and no one has more power than anyone else. However, as the pigs take more control, they become more like the human farmers they overthrew, showing that power can lead to corruption and inequality. 3.  George Orwell uses animals to represent human characteristics and critique human behavior in 'Animal Farm'. Each animal represents a different type of human or idea. For example, the pigs represent those in power who abuse it, the horses represent the hardworking but naive lower classes, and the sheep represent the uninformed masses who can be easily swayed 4.  The windmill in 'Animal Farm' symbolizes the manipulation of the working class. Napoleon uses the windmill project to keep the other animals busy and to distract them from his increasing power and the decreasing living conditions. Even though the windmill is supposed to improve the farm, it brings more hardship to the animals, representing how those in power often exploit the working class. 5.  'Animal Farm' ends with the pigs becoming just like the humans they overthrew. They walk on two legs, wear clothes, and even drink alcohol. This signifies the failure of the rebellion and the complete corruption of the original ideals of Animal Farm. It shows that the pigs, who were once comrades to the other animals, have become indistinguishable from their former human oppressors, highlighting the theme of power's ability to corrupt.",
    "student_answers": "1. Main characters is Old Major, Napoleon, Snowball. Old Major is wise pig who start rebellion. Napoleon is leader pig who become tyrant. Snowball is pig who have good idea but Napoleon chase him away.  2. Main theme is power corrupt. Animal start good but leader become bad like human. 3.Orwell use animal for show human trait. Pig is smart and cunning, horse is strong and loyal, sheep is blind follower.4.Windmill is symbol of hard work and manipulation. Napoleon use windmill for control other animal. 5. Animal Farm end with pig become like human. This mean revolution fail and power corrupt.", 
    "rubric_filled": "Question,Incorrect Verb Tense,Incorrect Verb Form,Incorrect Article Usage,Incorrect Preposition Usage,Incorrect Subject-Verb Agreement,Incorrect Pronoun Usage,Incorrect Adjective/Adverb Usage,Incorrect Word Order,Incorrect Conjunction Usage,Incorrect Modal Verb Usage,Incorrect Spelling,Incorrect Capitalization,Incorrect Punctuation,Incorrect Sentence Structure,Incorrect Idiomatic Expression Usage,Incorrect Collocation,Incorrect Use of Passive Voice,Incorrect Use of Reported Speech,Incorrect Use of Conditional Sentences,Incorrect Use of Subjunctive Mood,Misc. Errors, Content Score\nQuestion 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
}

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": json.dumps(data)},
    ]
)

print(response)

'''


1.  I am sending a rubric.csv as a string, a text file with 5 reading comprehension questions for the book titled "Animal Farm", a text file with suggested solutions for the 5 questions and a text file with file_name that contains a student id number containing the student's submission for this assignment. These are nested in a string representation of a Python string.  Grade the student submission according to the rubric, fill in the rubric by counting the number of times the error for the column occurs in each of the student's answers to the questions on the rows of the rubric but for the content score column, give a score from 0 to 5, with 5 being the highest, for how accurately the student was able to answer the question. Then for each student you will do the following.

2.  Output markdown where the errors you detected while grading are superscripted with numbers.  

3.  Output markdown explanations for the superscripted errors.   

Here is an example of the json-like key value pairs I want returned for the above tasks:

{
    "student_id": "123456",
    "markdown_corrections": "1. Main characters $^{[1][2]}$ is $^{[2]}$ Old Major, Napoleon, Snowball. Old Major is a wise pig who start $^{[3]}$ rebellion. Napoleon is a leader pig who become $^{[3]}$ tyrant. Snowball is a pig who have $^{[2][3]}$ good idea but Napoleon chase $^{[3]}$ him away.  2. Main theme $^{[1]}$ is $^{[2]}$ power corrupt. Animal start $^{[3]}$ good but leader become $^{[3]}$ bad like human.  3. Orwell use $^{[3]}$ animal for $^{[4]}$ show human trait. Pig is smart and cunning, horse is strong and loyal, sheep is blind follower.  4. Windmill is symbol $^{[1]}$ of hard work and manipulation. Napoleon use $^{[3]}$ windmill for $^{[4]}$ control other animal. 5. Animal Farm end $^{[3]}$ with pig become $^{[3]}$ like human. This mean $^{[2]}$ revolution fail $^{[3]}$ and power corrupt.",
    "markdown_comments": "1. $^{[1]}$ Missing article before 'main characters', 'main theme', 'symbol'. 2. $^{[2]}$ Incorrect verb form; 'is', 'mean', and 'have' should be 'are'. 3. $^{[3]}$ Incorrect verb tense; 'start', 'become', 'use', 'end', 'fail' should be in the correct tense.4. $^{[4]}$ Incorrect preposition usage; 'for' should be 'to'.",
    "rubric_filled": "Question,Incorrect Verb Tense,Incorrect Verb Form,Incorrect Article Usage,Incorrect Preposition Usage,Incorrect Subject-Verb Agreement,Incorrect Pronoun Usage,Incorrect Adjective/Adverb Usage,Incorrect Word Order,Incorrect Conjunction Usage,Incorrect Modal Verb Usage,Incorrect Spelling,Incorrect Capitalization,Incorrect Punctuation,Incorrect Sentence Structure,Incorrect Idiomatic Expression Usage,Incorrect Collocation,Incorrect Use of Passive Voice,Incorrect Use of Reported Speech,Incorrect Use of Conditional Sentences,Incorrect Use of Subjunctive Mood,Misc. Errors, Content Score\nQuestion 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
}

The value for the "rubric_filled" field should be filled as per the instructions so they most likely will not be all 0's in your response.  

Here is a Python dictionary-like representation of what I will send as the body of my api request to ChatGPT.  

{
    "student_id": "123456",
    "subject": "Reading comprehension questions for the book titled 'Animal Farm'",
    "questions": "1. Who are the main characters in 'Animal Farm' and what are their roles?  2. What is the main theme of 'Animal Farm'? 3. How does George Orwell use animals to represent human characteristics in 'Animal Farm'? 4. What does the windmill symbolize in 'Animal Farm'? 5. How does 'Animal Farm' end and what does this signify?",
    "solutions": "1.  The main characters in 'Animal Farm' are Old Major, Napoleon, and Snowball. Old Major is a wise and respected pig who inspires the rebellion with his ideas of animal equality. Napoleon is another pig who becomes the leader of Animal Farm after the Rebellion. He gradually takes more power and becomes a dictator, mirroring the human farmer Mr. Jones. Snowball is a pig who is initially a leader of the rebellion and has many ideas for the farm's improvement. However, he is chased away by Napoleon and his guard dogs, allowing Napoleon to seize control of the farm. 2.  The main theme of 'Animal Farm' is that power can corrupt those who possess it. At the beginning of the story, the animals hope for a society where all animals are equal and no one has more power than anyone else. However, as the pigs take more control, they become more like the human farmers they overthrew, showing that power can lead to corruption and inequality. 3.  George Orwell uses animals to represent human characteristics and critique human behavior in 'Animal Farm'. Each animal represents a different type of human or idea. For example, the pigs represent those in power who abuse it, the horses represent the hardworking but naive lower classes, and the sheep represent the uninformed masses who can be easily swayed 4.  The windmill in 'Animal Farm' symbolizes the manipulation of the working class. Napoleon uses the windmill project to keep the other animals busy and to distract them from his increasing power and the decreasing living conditions. Even though the windmill is supposed to improve the farm, it brings more hardship to the animals, representing how those in power often exploit the working class. 5.  'Animal Farm' ends with the pigs becoming just like the humans they overthrew. They walk on two legs, wear clothes, and even drink alcohol. This signifies the failure of the rebellion and the complete corruption of the original ideals of Animal Farm. It shows that the pigs, who were once comrades to the other animals, have become indistinguishable from their former human oppressors, highlighting the theme of power's ability to corrupt.",
    "student_answers": "1. Main characters is Old Major, Napoleon, Snowball. Old Major is wise pig who start rebellion. Napoleon is leader pig who become tyrant. Snowball is pig who have good idea but Napoleon chase him away.  2. Main theme is power corrupt. Animal start good but leader become bad like human. 3.Orwell use animal for show human trait. Pig is smart and cunning, horse is strong and loyal, sheep is blind follower.4.Windmill is symbol of hard work and manipulation. Napoleon use windmill for control other animal. 5. Animal Farm end with pig become like human. This mean revolution fail and power corrupt.", 
    "rubric_filled": "Question,Incorrect Verb Tense,Incorrect Verb Form,Incorrect Article Usage,Incorrect Preposition Usage,Incorrect Subject-Verb Agreement,Incorrect Pronoun Usage,Incorrect Adjective/Adverb Usage,Incorrect Word Order,Incorrect Conjunction Usage,Incorrect Modal Verb Usage,Incorrect Spelling,Incorrect Capitalization,Incorrect Punctuation,Incorrect Sentence Structure,Incorrect Idiomatic Expression Usage,Incorrect Collocation,Incorrect Use of Passive Voice,Incorrect Use of Reported Speech,Incorrect Use of Conditional Sentences,Incorrect Use of Subjunctive Mood,Misc. Errors, Content Score\nQuestion 1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\nQuestion 5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
}

Query: """Write Python code to make this API request to OpenAI.  Use any model you want but I have been using GPT4."""  

'''