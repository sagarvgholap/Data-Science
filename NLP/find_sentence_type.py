import spacy
from spacy.matcher import PhraseMatcher

# Load the small English model
nlp = spacy.load("en_core_web_sm")


# Define a function to identify the sentence type
def identify_sentence_type(sentence):
    matcher = PhraseMatcher(nlp.vocab)
    
    sentence_type = "Simple sentence"
    doc = nlp(sentence)

    # Check if the sentence contains multiple clauses
    if len(list(doc.sents)) > 1:
        sentence_type = "Complex sentence"
        # return sentence_type


    # Check if there is a subordinating conjunction or adverb indicating a complex sentence
    for token in doc:
        if token.dep_ in ["mark", "advcl"]:
            sentence_type = "Complex sentence"
            # return sentence_type

    # Check if there is a relative pronoun or adverb indicating a complex sentence
    for token in doc:
        if token.dep_ in ["relcl", "advcl"]:
            sentence_type = "Complex sentence"
            # return sentence_type

    # Check if there is a coordinating conjunction indicating a compound sentence
    for token in doc:
        if sentence_type != "Complex sentence" and token.dep_ == "cc" and token.head.dep_ != "mark":
            sentence_type = "Compound sentence"
            # return sentence_type

    print(sentence_type)

    return sentence_type




# # # Simple Sentences:
# identify_sentence_type("I like to read books.")
# identify_sentence_type("The sun shines brightly.")
# identify_sentence_type("She sings beautifully.")
# identify_sentence_type("They went to the park.")

# # # Complex Sentences:
# identify_sentence_type("Although it was cold outside, they decided to go for a swim.")
# identify_sentence_type("After I finish my work, I will go for a run.")
# identify_sentence_type("Because she studied hard, she passed the exam.")
# identify_sentence_type("Since it was raining, they stayed indoors.")
# identify_sentence_type("Although it was raining, she went for a walk.")
# identify_sentence_type("Although she was tired, she went for a walk.")
# identify_sentence_type("I like to eat the candy before I watch a movie.")
# identify_sentence_type("Because he was late again, he would be docked a day’s pay.")
# identify_sentence_type("While I am a passionate basketball fan, I prefer football.")
# identify_sentence_type("Although she was considered smart, she failed all her exams.")
# identify_sentence_type("Whenever it rains, I like to wear my blue coat.") # Simple sentence
# identify_sentence_type("Having a party is a bad idea because the neighbors will complain.")
# identify_sentence_type("I am extremely happy since I retired.")
# identify_sentence_type("The dog jumped on his lap while he was eating.")
# identify_sentence_type("Annie was still crying, although she had been happy about the news.")
# identify_sentence_type("Because she was scoring many baskets, Elesa was considered the best player on the team.")
# identify_sentence_type("Elesa was considered the best player on the team because she was scoring many baskets.")
# identify_sentence_type("Since Hannah got here, she’s been nothing but trouble.")
# identify_sentence_type("Hannah has been nothing but trouble since she got here.")
# identify_sentence_type("Because I was often late, and since I was always forgetting things, I was regarded as a scatterbrain by my friends.") # Compound sentence
# identify_sentence_type("Although the war ended, and as people tend to have short memories, the city’s people were still divided over its impact.") # Compound sentence
# identify_sentence_type("Because he was so small, Stuart was often hard to find around the hou")
# identify_sentence_type("I’ve never any pity for conceited people, because I think they carry their comfort about with them.")
# identify_sentence_type("And now that you don’t have to be perfect, you can be good.") # Compound sentence
# identify_sentence_type("Whenever he was lonely, Lance called his mother.") # Simple sentence
# identify_sentence_type("Don’t leave the restaurant until the dishes here are washed.")
# identify_sentence_type("While playing football, the ball thrown by my friend hit the boy crossing the street.")
# identify_sentence_type("Elissa was very sick today and we will take her to the hospital now, before she gets worse.") # Compound sentence
# identify_sentence_type("Even after all these years, when I saw her, I was as excited as the first day.") # Simple sentence
# identify_sentence_type("The game we went to at the mall today was so much fun no matter how long it lasted.")
# identify_sentence_type("Although he wanted to study abroad, he could not go because his father did not want him to go.")
# identify_sentence_type("I saw him going to work in the morning when I was going to school.") # Simple sentence
# identify_sentence_type("While I was cooking he was still playing games on the computer.")
# identify_sentence_type("Although I miss him so much, I cannot go to him because I do not have money.")
# identify_sentence_type("Although I worked hard, I got a very low grade from the exam and stayed in the classroom.") # Compound sentence

# # Compound Sentences:
# identify_sentence_type("I bought a new laptop, and my brother bought a new smartphone.")
# identify_sentence_type("She loves to dance, but he prefers to paint.")
# identify_sentence_type("I wanted to go to the party, yet I had too much work to do.")
# identify_sentence_type("He played football, and she played basketball.")
# identify_sentence_type("She ate breakfast, and then she went for a walk.")

