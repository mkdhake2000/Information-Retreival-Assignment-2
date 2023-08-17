# %%
file = open("NER_Datasets/hi_dev.conll", 'r', encoding='utf8')
lines = file.read()

# %%
lines=lines.split('#')
lines=lines[1:]

# %%
wrd=[]
label=[]
for i in range(len(lines)):
    line=lines[i].strip().split("\n")[1:]
    swrd=[]
    slabel=[]
    for j in range(len(line)):
        if line[j] == '(':
            continue
        swrd.append(line[j].split(" ")[0])
        slabel.append(line[j].split(" ")[-1])
    wrd.append(swrd)
    label.append(slabel)

lbl = [i for j in label for i in j]
uniqueLabels = list(set(lbl))

for i in range(len(wrd)):
    wrd[i] = ' '.join(wrd[i])
    label[i] = ' '.join(label[i])

# %%
import pandas as pd 

# %%
dfr = {'sentence':wrd,'label':label}
testDf = pd.DataFrame(dfr)
testDf.to_csv('NER-CSV/testData.csv',index=False)

# %%
file = open("NER_Datasets/hi_train.conll", 'r', encoding='utf8')
lines = file.read()

# %%
lines=lines.split('#')
lines=lines[1:]

# %%
wrd=[]
label=[]
for i in range(len(lines)):
    line=lines[i].strip().split("\n")[1:]
    swrd=[]
    slabel=[]
    for j in range(len(line)):
        if line[j] == '(':
            continue
        swrd.append(line[j].split(" ")[0])
        slabel.append(line[j].split(" ")[-1])
    wrd.append(swrd)
    label.append(slabel)
for i in range(len(wrd)):
    wrd[i] = ' '.join(wrd[i])
    label[i] = ' '.join(label[i])

# %%
dfr = {'sentence':wrd,'label':label}
trainDf = pd.DataFrame(dfr)
trainDf.to_csv('NER-CSV/trainData.csv',index=False)

# %%
labelIndex={v:i for i,v in enumerate(uniqueLabels)}
indexLabel={i:v for i,v in enumerate(uniqueLabels)}
