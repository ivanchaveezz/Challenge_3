
print('welcome to the financial analysis')

import csv
import pandas as pd 

with open('./resources/budget_data.csv') as csvfile:
    #TOTATL MONTHS

    csvreader = csv.reader(csvfile)
    csvreader = pd.DataFrame(csvreader)
    csvreader2 = csvreader[1:] #se usa para utilizar a partir de la segunda fila
    columnas = csvreader.loc[0]
    csvreader2.columns = columnas
    meses=csvreader2['Date'].count()
    
    #TOTAL PROFIT/LOSS
    suma =csvreader2['Profit/Losses'].sum()
    


    #AVERAGE CHANGE

  
  
    
    
    
    
    
    
    print('total profit/loss:',suma)
    print('Total months:', meses)

    
    



    





   
    



'''
    #print(csvreader) 
    #csvreader.count(0)

   # head = next(csvreader)

    for row in csvreader:
        (print(row))

'''
