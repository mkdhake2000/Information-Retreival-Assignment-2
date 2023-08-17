# %% [markdown]
# ### &emsp;GLOVE

# %%
#Import Numpy and Pandas package
import numpy as np
import pandas as pd

# %% [markdown]
# #### &emsp;&emsp; Reading Word Similarity Dataset and seperating word pairs to be compared into two lists

# %%
with open("Word-Similarity/hindi.txt",'rb') as flWS:
    txt2=flWS.read()
txt2=txt2.decode(errors='replace')
txt2Split=txt2.strip('\n').split('\n')
est=np.array([float(t.split(',')[2]) for t in txt2Split])
txt2Split2=[t.split(',')[1] for t in txt2Split]
txt2Split1=[t.split(',')[0] for t in txt2Split]

# %% [markdown]
# #### &emsp;&emsp; Reading GLOVE file for 50 dimension vectors for words

# %%
with open('hi/50/glove/hi-d50-glove.txt','rb') as fl:
    txt=fl.read()
txt=txt.decode(errors='replace')

# %%
#Splitting text into lines
wrdVec=txt.split('\n')

# %%
#Splitting lines into words and getting only hindi words
wrds=[t.split(" ")[0] for t in wrdVec]

# %%
#Creating Dictionary for hindi words and their index in files
wrdDict={v:i for i,v in enumerate(wrds)}

# %% [markdown]
# #### &emsp;&emsp; Getting word vectors for word pairs from word similarity dataset

# %%
lst1=[]
lst2=[]

for i in txt2Split1:
    lst1.append(np.array([float(s) for s in wrdVec[wrdDict[i]].split(" ")[1:]]))

for i in txt2Split2:
    lst2.append(np.array([float(s) for s in wrdVec[wrdDict[i]].split(" ")[1:]]))

# %%
#Getting Cosine Similarity for word pairs of word similarity dataset
cos50=np.array([(l1.dot(l2)/(np.linalg.norm(l1)*np.linalg.norm(l2)))*10 for l1,l2 in zip(lst1,lst2)])

# %%
#Deleting unrequired variables to free up memory
del txt
del txt2
del txt2Split
del wrdVec
del wrds

# %% [markdown]
# #### &emsp;&emsp; Reading GLOVE file for 100 dimension vectors for words

# %%
with open('hi/100/glove/hi-d100-glove.txt','rb') as fl:
    txt=fl.read()
txt=txt.decode(errors='replace')

# %%
#Splitting text into lines
wrdVec=txt.split('\n')

# %% [markdown]
# #### &emsp;&emsp; Getting word vectors for word pairs from word similarity dataset

# %%
lst1=[]
lst2=[]

for i in txt2Split1:
    lst1.append(np.array([float(s) for s in wrdVec[wrdDict[i]].split(" ")[1:]]))
    
for i in txt2Split2:
    lst2.append(np.array([float(s) for s in wrdVec[wrdDict[i]].split(" ")[1:]]))

# %%
#Getting Cosine Similarity for word pairs of word similarity dataset
cos100=np.array([(l1.dot(l2)/(np.linalg.norm(l1)*np.linalg.norm(l2)))*10 for l1,l2 in zip(lst1,lst2)])

# %%
#Thresholds*10 array given in question
threshs=[4.0,5.0,6.0,7.0,8.0]

# %%
#For Loop  to get the similarity of word pairs with word vectors of 50 dimensions and exporting output in respective files
for t in threshs:
    simSC=np.array([0 if s<t else 1 for s in cos50])
    estSC=np.array([0 if s<t else 1 for s in est])
    acc=(len([i[0] for i in zip(estSC,simSC) if i[0]==i[1]])/len(est))*100
    df={'Word1':txt2Split1, 'Word2':txt2Split2, 'Similarity Score( Similarity score from word2vec*10)':cos50, 'Ground Truth similarity score':est, 'Label(0 for dissimilar, 1 for similar)':simSC}
    df = pd.DataFrame(df)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']
    df.to_csv('Q1Output/Glove/Q1_Glove50_similarity_'+str(int(t))+'.csv',index=False)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']

#For Loop  to get the similarity of word pairs with word vectors of 100 dimensions and exporting output in respective files
for t in threshs:
    simSC=np.array([0 if s<t else 1 for s in cos100])
    estSC=np.array([0 if s<t else 1 for s in est])
    acc=(len([i[0] for i in zip(estSC,simSC) if i[0]==i[1]])/len(est))*100
    df={'Word1':txt2Split1, 'Word2':txt2Split2, 'Similarity Score( Similarity score from word2vec*10)':cos100, 'Ground Truth similarity score':est, 'Label(0 for dissimilar, 1 for similar)':simSC}
    df = pd.DataFrame(df)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']
    df.to_csv('Q1Output/Glove/Q1_Glove100_similarity_'+str(int(t))+'.csv',index=False)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']

# %%
del wrdDict

# %% [markdown]
# ### &emsp;CBOW

# %%
#Importing Word2Vec from gensim.models to read model files for CBOW
from gensim.models import Word2Vec as w2v

# %% [markdown]
# #### &emsp;&emsp; Loading CBOW model for 100 dimensions word vectors

# %%
cB100=w2v.load("hi/100/cbow/hi-d100-m2-cbow.model")

# %%
#Getting 100 dimension word vectors for word pairs from word similarity dataset
lst1=[cB100.wv[t] for t in txt2Split1]
lst2=[cB100.wv[t] for t in txt2Split2]

#Getting Cosine Similarity for the word pairs
cos100=np.array([(l1.dot(l2)/(np.linalg.norm(l1)*np.linalg.norm(l2)))*10 for l1,l2 in zip(lst1,lst2)])

# %%
#Deleting the 100 dimension model to free up space
del cB100

# %% [markdown]
# #### &emsp;&emsp; Loading CBOW model for 50 dimensions word vectors

# %%
cB50=w2v.load("hi/50/cbow/hi-d50-m2-cbow.model")

# %%
#Getting 50 dimension word vectors for word pairs from word similarity dataset
lst1=[cB50.wv[t] for t in txt2Split1]
lst2=[cB50.wv[t] for t in txt2Split2]

#Getting Cosine Similarity for the word pairs
cos50=np.array([(l1.dot(l2)/(np.linalg.norm(l1)*np.linalg.norm(l2)))*10 for l1,l2 in zip(lst1,lst2)])

# %%
#Deleting the 50 dimension model to free up space
del cB50

# %%
#Thresholds*10 array given in question
threshs=[4.0,5.0,6.0,7.0,8.0]

# %%
#For Loop  to get the similarity of word pairs with word vectors of 50 dimensions and exporting output in respective files
for t in threshs:
    simSC=np.array([0 if s<t else 1 for s in cos50])
    estSC=np.array([0 if s<t else 1 for s in est])
    acc=(len([i[0] for i in zip(estSC,simSC) if i[0]==i[1]])/len(est))*100
    df={'Word1':txt2Split1, 'Word2':txt2Split2, 'Similarity Score( Similarity score from word2vec*10)':cos50, 'Ground Truth similarity score':est, 'Label(0 for dissimilar, 1 for similar)':simSC}
    df = pd.DataFrame(df)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']
    df.to_csv('Q1Output/Cbow/Q1_Cbow50_similarity_'+str(int(t))+'.csv',index=False)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']

#For Loop  to get the similarity of word pairs with word vectors of 100 dimensions and exporting output in respective files
for t in threshs:
    simSC=np.array([0 if s<t else 1 for s in cos100])
    estSC=np.array([0 if s<t else 1 for s in est])
    acc=(len([i[0] for i in zip(estSC,simSC) if i[0]==i[1]])/len(est))*100
    df={'Word1':txt2Split1, 'Word2':txt2Split2, 'Similarity Score( Similarity score from word2vec*10)':cos100, 'Ground Truth similarity score':est, 'Label(0 for dissimilar, 1 for similar)':simSC}
    df = pd.DataFrame(df)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']
    df.to_csv('Q1Output/Cbow/Q1_Cbow100_similarity_'+str(int(t))+'.csv',index=False)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']

# %% [markdown]
# ### &emsp;SKIPGRAM

# %% [markdown]
# #### &emsp;&emsp; Loading SKIPGRAM model for 100 dimensions word vectors

# %%
sG100=w2v.load("hi/100/sg/hi-d100-m2-sg.model")

# %%
#Getting 100 dimension word vectors for word pairs from word similarity dataset
lst1=[sG100.wv[t] for t in txt2Split1]
lst2=[sG100.wv[t] for t in txt2Split2]

#Getting Cosine Similarity for the word pairs
cos100=np.array([(l1.dot(l2)/(np.linalg.norm(l1)*np.linalg.norm(l2)))*10 for l1,l2 in zip(lst1,lst2)])

# %%
#Deleting the 100 dimension model to free up space
del sG100

# %% [markdown]
# #### &emsp;&emsp; Loading SKIPGRAM model for 50 dimensions word vectors

# %%
sG50=w2v.load("hi/50/sg/hi-d50-m2-sg.model")

# %%
#Getting 50 dimension word vectors for word pairs from word similarity dataset
lst1=[sG50.wv[t] for t in txt2Split1]
lst2=[sG50.wv[t] for t in txt2Split2]

#Getting Cosine Similarity for the word pairs
cos50=np.array([(l1.dot(l2)/(np.linalg.norm(l1)*np.linalg.norm(l2)))*10 for l1,l2 in zip(lst1,lst2)])

# %%
#Deleting the 50 dimension model to free up space
del sG50

# %%
#Thresholds*10 array given in question
threshs=[4.0,5.0,6.0,7.0,8.0]

# %%
#For Loop  to get the similarity of word pairs with word vectors of 50 dimensions and exporting output in respective files
for t in threshs:
    simSC=np.array([0 if s<t else 1 for s in cos50])
    estSC=np.array([0 if s<t else 1 for s in est])
    acc=(len([i[0] for i in zip(estSC,simSC) if i[0]==i[1]])/len(est))*100
    df={'Word1':txt2Split1, 'Word2':txt2Split2, 'Similarity Score( Similarity score from word2vec*10)':cos50, 'Ground Truth similarity score':est, 'Label(0 for dissimilar, 1 for similar)':simSC}
    df = pd.DataFrame(df)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']
    df.to_csv('Q1Output/SkipGram/Q1_SkipGram50_similarity_'+str(int(t))+'.csv',index=False)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']

#For Loop  to get the similarity of word pairs with word vectors of 100 dimensions and exporting output in respective files
for t in threshs:
    simSC=np.array([0 if s<t else 1 for s in cos100])
    estSC=np.array([0 if s<t else 1 for s in est])
    acc=(len([i[0] for i in zip(estSC,simSC) if i[0]==i[1]])/len(est))*100
    df={'Word1':txt2Split1, 'Word2':txt2Split2, 'Similarity Score( Similarity score from word2vec*10)':cos100, 'Ground Truth similarity score':est, 'Label(0 for dissimilar, 1 for similar)':simSC}
    df = pd.DataFrame(df)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']
    df.to_csv('Q1Output/SkipGram/Q1_SkipGram100_similarity_'+str(int(t))+'.csv',index=False)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']

# %% [markdown]
# ### &emsp;FASTTEXT

# %%
#Importing FastText from gensim.models to read model files for FastText
from gensim.models import FastText as fT

# %% [markdown]
# #### &emsp;&emsp; Loading FASTTEXT model for 100 dimensions word vectors

# %%
fT100=fT.load("hi/100/fasttext/hi-d100-m2-fasttext.model")

# %%
#Getting 100 dimension word vectors for word pairs from word similarity dataset
lst1=[fT100.wv[t] for t in txt2Split1]
lst2=[fT100.wv[t] for t in txt2Split2]

#Getting Cosine Similarity for the word pairs
cos100=np.array([(l1.dot(l2)/(np.linalg.norm(l1)*np.linalg.norm(l2)))*10 for l1,l2 in zip(lst1,lst2)])

# %%
#Deleting the 100 dimension model to free up space
del fT100

# %% [markdown]
# #### &emsp;&emsp; Loading FASTTEXT model for 50 dimensions word vectors

# %%
fT50=fT.load("hi/50/fasttext/hi-d50-m2-fasttext.model")

# %%
#Getting 50 dimension word vectors for word pairs from word similarity dataset
lst1=[fT50.wv[t] for t in txt2Split1]
lst2=[fT50.wv[t] for t in txt2Split2]

#Getting Cosine Similarity for the word pairs
cos50=np.array([(l1.dot(l2)/(np.linalg.norm(l1)*np.linalg.norm(l2)))*10 for l1,l2 in zip(lst1,lst2)])

# %%
#Deleting the 50 dimension model to free up space
del fT50

# %%
#Thresholds*10 array given in question
threshs=[4.0,5.0,6.0,7.0,8.0]

# %%
#For Loop  to get the similarity of word pairs with word vectors of 50 dimensions and exporting output in respective files
for t in threshs:
    simSC=np.array([0 if s<t else 1 for s in cos50])
    estSC=np.array([0 if s<t else 1 for s in est])
    acc=(len([i[0] for i in zip(estSC,simSC) if i[0]==i[1]])/len(est))*100
    df={'Word1':txt2Split1, 'Word2':txt2Split2, 'Similarity Score( Similarity score from word2vec*10)':cos50, 'Ground Truth similarity score':est, 'Label(0 for dissimilar, 1 for similar)':simSC}
    df = pd.DataFrame(df)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']
    df.to_csv('Q1Output/FastText/Q1_FastText50_similarity_'+str(int(t))+'.csv',index=False)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']

#For Loop  to get the similarity of word pairs with word vectors of 100 dimensions and exporting output in respective files
for t in threshs:
    simSC=np.array([0 if s<t else 1 for s in cos100])
    estSC=np.array([0 if s<t else 1 for s in est])
    acc=(len([i[0] for i in zip(estSC,simSC) if i[0]==i[1]])/len(est))*100
    df={'Word1':txt2Split1, 'Word2':txt2Split2, 'Similarity Score( Similarity score from word2vec*10)':cos100, 'Ground Truth similarity score':est, 'Label(0 for dissimilar, 1 for similar)':simSC}
    df = pd.DataFrame(df)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']
    df.to_csv('Q1Output/FastText/Q1_FastText100_similarity_'+str(int(t))+'.csv',index=False)
    df.loc[len(df.index)] = ['Accuracy : ', acc, '','','']


