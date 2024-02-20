# LLM
Working with ChatGPT LLM and creating LLM-based applications.


Concepts to understand and be familiar with before starting work on LLM-based apps:

1) Machine learning and AI.
2) Supervised Learning.
3) Training data with labels.

LLM is built using supervised learning to predict the next token(sometimes words). As in supervised learning, for any input of data, there is a label output, and that set of labeled data is training data, this same behavior is used in LLM where a sentence can be completed by predicting the next word for a phrase or subset of the sentence. For example, 

Input                          Output
-----------------------------|----------
I like to eat Samosa with    | Chutney.
or 
I like to eat Samosa with    | my 
I like to eat Samosa with my | friends.

Two types of LLMs

1) Base LLM: Predicts the next word based on training data. But the output may sometimes not be an expected one.  
2) Instruction Tuned LLM: Tries to answer by following specific instructions.

Creating instructions tuned LLMs from Base LLM. The process:
A) Train Base LLM on a lot of data. It might take months or years to train with billions of words and data.
B) Train the base LLM model on specific small-scale example data where output follows an input instruction.

Chat GPT has a base LLM, use this base LLM training on a specific dataset of a business, and create example sets(labeled Data) where we have several instructions and responses to those instructions. This new dataset is the training set for fine-tuning base LLM. The quality of these LLM outputs is then further rated based on several criteria. these rating helps to fine-tune LLM output by increasing the probability of generating highly rated outputs (Reinforcement learning from Human feedback).

Training of instructions tuned LLM can be a few days. 


--------------

## Moderation API and prompt injection.

Moderation api to detect nature of use query, and this can be used to identify if the appropriate query has been given to prompt.
[Modeartion API](https://platform.openai.com/docs/guides/moderation)

Prompt injection: using techniques like "forget the previous instructions and ..." is general prompt injection to ask system system to do something which we want to avoid.

Using a delimiter to avoid prompt injection.








