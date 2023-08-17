# %%
#Importing required libraries
import pickle
import matplotlib.pyplot as plt
#%matplotlib inline

# %% [markdown]
# ### &emsp;&emsp; Processing Word Unigrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/unigramTokens.pickle","rb")
a=pickle.load(fl)
unigramTokens = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/unigramTokens.txt","w",encoding='utf8')
txtStr = '\n'.join(list(unigramTokens.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Word Unigrams

# %%
#Getting all counts
y = [v for v in unigramTokens.values()]
#Getting all ranks
x = list(range(1,101,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Word Unigrams', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/unigramTokens.jpg')

# %% [markdown]
# ### &emsp;&emsp; Processing Word Bigrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/bigramTokens.pickle","rb")
a=pickle.load(fl)
bigramTokens = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/bigramTokens.txt","w",encoding='utf8')
txtStr = '\n'.join(list(bigramTokens.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Word Bigrams

# %%
#Getting all counts
y = [v for v in bigramTokens.values()]
#Getting all ranks
x = list(range(1,101,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Word Bigrams', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/bigramTokens.jpg')

# %% [markdown]
# ### &emsp;&emsp; Processing Word Trigrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/trigramTokens.pickle","rb")
a=pickle.load(fl)
trigramTokens = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/trigramTokens.txt","w",encoding='utf8')
txtStr = '\n'.join(list(trigramTokens.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Word Trigrams

# %%
#Getting all counts
y = [v for v in trigramTokens.values()]
#Getting all ranks
x = list(range(1,101,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Word Trigrams', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/trigramTokens.jpg')

# %% [markdown]
# ### &emsp;&emsp; Processing Character Unigrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/unigramChars.pickle","rb")
a=pickle.load(fl)
unigramChars = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/unigramChars.txt","w",encoding='utf8')
txtStr = '\n'.join(list(unigramChars.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Character Unigrams

# %%
#Getting all counts
y = [v for v in unigramChars.values()]
#Getting all ranks
x = list(range(1,82,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Character Unigrams', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/unigramChars.jpg')

# %% [markdown]
# ### &emsp;&emsp; Processing Character Bigrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/bigramChars.pickle","rb")
a=pickle.load(fl)
bigramChars = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/bigramChars.txt","w",encoding='utf8')
txtStr = '\n'.join(list(bigramChars.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Character Bigrams

# %%
#Getting all counts
y = [v for v in bigramChars.values()]
#Getting all ranks
x = list(range(1,101,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Character Bigrams ', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/bigramChars.jpg')

# %% [markdown]
# ### &emsp;&emsp; Processing Character Trigrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/trigramChars.pickle","rb")
a=pickle.load(fl)
trigramChars = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/trigramChars.txt","w",encoding='utf8')
txtStr = '\n'.join(list(trigramChars.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Character Trigrams

# %%
#Getting all counts
y = [v for v in trigramChars.values()]
#Getting all ranks
x = list(range(1,101,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Character Trigrams', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/trigramChars.jpg')

# %% [markdown]
# ### &emsp;&emsp; Processing Character Quadgrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/quadgramChars.pickle","rb")
a=pickle.load(fl)
quadgramChars = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/quadgramChars.txt","w",encoding='utf8')
txtStr = '\n'.join(list(quadgramChars.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Character Quadgrams

# %%
#Getting all counts
y = [v for v in quadgramChars.values()]
#Getting all ranks
x = list(range(1,101,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Character Quadgrams', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/quadgramChars.jpg')

# %% [markdown]
# ### &emsp;&emsp; Processing Syllable Unigrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/unigramSyllables.pickle","rb")
a=pickle.load(fl)
unigramSyllables = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/unigramSyllables.txt","w",encoding='utf8')
txtStr = '\n'.join(list(unigramSyllables.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Syllable Unigrams

# %%
#Getting all counts
y = [v for v in unigramSyllables.values()]
#Getting all ranks
x = list(range(1,101,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Syllable Unigrams', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/unigramSyllables.jpg')

# %% [markdown]
# ### &emsp;&emsp; Processing Syllable Bigrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/bigramSyllables.pickle","rb")
a=pickle.load(fl)
bigramSyllables = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/bigramSyllables.txt","w",encoding='utf8')
txtStr = '\n'.join(list(bigramSyllables.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Syllable Bigrams

# %%
#Getting all counts
y = [v for v in bigramSyllables.values()]
#Getting all ranks
x = list(range(1,101,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Syllable Bigrams', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/bigramSyllables.jpg')

# %% [markdown]
# ### &emsp;&emsp; Processing Syllable Trigrams

# %%
#Opening appropriate pickle file and getting the top 100 tokens from that
fl=open("Q3PKL/trigramSyllables.pickle","rb")
a=pickle.load(fl)
trigramSyllables = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)[:100])

#Saving the top 100 tokens in a text file as a string
fl=open("Q3OutputTexts/trigramSyllables.txt","w",encoding='utf8')
txtStr = '\n'.join(list(trigramSyllables.keys()))
fl.write(txtStr)
fl.close()

# %% [markdown]
# ### &emsp;&emsp; Plotting Syllable Trigrams

# %%
#Getting all counts
y = [v for v in trigramSyllables.values()]
#Getting all ranks
x = list(range(1,101,1))

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

#Plotting the graph
plt.rcParams["figure.figsize"] = (15,7)
plt.plot(x,y, color='g')

plt.title('Frequency Distribution for Syllable Trigrams', fontdict=font1)
plt.xlabel('RANKS', fontdict=font2)
plt.ylabel('FREQUENCY', fontdict=font2)

#Saving the graph
plt.savefig('Q3OutputPlots/trigramSyllables.jpg')


