from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt',quiet=True)

article=Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()
corpus=article.text

print(corpus)

text=corpus
sentence_list=nltk.sent_tokenize(text)
print(sentence_list)

def greeting_response(text):
  text.lower()

  bot_greetings=['hi','hello','hey','halo']
  user_greetings=['hi','hello','greetings','whatsapp']
  for word in text.split():
    if word in user_greetings:
      return random.choice(bot_greetings)
    
def index_sort(list_var):
  lenght=len(list_var)
  list_index=list(range(0,lenght))

  x=list_var
  for i in range(lenght):
    for j in range(lenght):
      if x[list_index[i]]>x[list_index[j]]:
        temp=list_index[i]
        list_index[i]=list_index[j]
        list_index[j]=temp
  return list_index


def bot_response(user_input):
  user_input=user_input.lower()
  sentence_list.append(user_input)
  bot_response=''
  cm=CountVectorizer().fit_transform(sentence_list)
  similarity_scores=cosine_similarity(cm[-1],cm)
  similarity_scores_list=similarity_scores.flatten()
  index=index_sort(similarity_scores_list)
  index=index[1:]
  response_flag=0

  j=0
  for i in range(len(index)):
    if similarity_scores_list[index[i]]>0.0:
      bot_response=bot_response+' '+sentence_list[index[i]]
      response_flag=1
      j=j+1
    if j>2:
      break
  if response_flag==0:
    bot_response=bot_response+' '+"I apologise,I don't understand."
  sentence_list.remove(user_input)

  return bot_response


 print("visab bot:this a assistance to gid you")

exit_list=['exit','bye','quit','break']
while(True):
  user_input=input()
  if user_input.lower() in exit_list:
    print('visab bot:chat with you later,bye!')
    break
  else:
    if greeting_response(user_input)!=None:
      print('visab bot:'+greeting_response(user_input))
    else:
      print('visab bot:'+bot_response(user_input))
      
