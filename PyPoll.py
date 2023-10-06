
print('welcome to the financial analysis')

import csv
import pandas as pd 

with open('./resources/election_data.csv') as csvfile:
    #TOTATL MONTHS

    csvreader = csv.reader(csvfile)
    csvreader = pd.DataFrame(csvreader)
    csvreader2 = csvreader[1:] #se usa para utilizar a partir de la segunda fila
    columnas = csvreader.loc[0]
    csvreader2.columns = columnas
    votos=csvreader2['Candidate'].count()
   #print('total votos:',votos)
    #frec=csvreader2
   
    frec=csvreader2.groupby('Candidate').size()
    frec=pd.DataFrame(frec)
    frec2=frec/votos*100
    winner=frec.max()
  



    print (frec2,'%')

    print('winner',winner)
    
    
    
    
    print(frec)


  

    #print(csvreader2)

