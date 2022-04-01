from tokenize import String
import pandas as pd
import matplotlib.pyplot as mpl

game_sales = pd.read_csv("D:\Game_Sales Analys\sales.csv")
game_sales_clean = pd.DataFrame
game_sales_clean=game_sales.dropna(how='any')#Getting rid of Nan lines
game_sales_clean['Genre'].astype(str)

game_sales_year = pd.DataFrame
game_sales_year=game_sales_clean.groupby('Year').sum()#Getting yearly sales
del game_sales_year['Rank']

#In following Section of the code we are recieving sorted list of genrs. First 5 elements are top-5 genres, that will be analysed further
sales_temp=pd.DataFrame
sales_temp=game_sales_clean.groupby('Genre').sum()
sales_temp=sales_temp['Global_Sales'].sort_values(ascending=False)
Genres=list(sales_temp.index.values)

counter = 0
for Element in Genres:
    if counter<5:
        sales_temp=game_sales_clean[game_sales_clean['Genre']==Element]
        sales_temp=sales_temp.groupby('Year').sum()
        del sales_temp['Rank']
        sales_temp['Global_Sales_%']=sales_temp['Global_Sales']/game_sales_year['Global_Sales']*100        
        mpl.figure(Element)
        mpl.bar(sales_temp.index,sales_temp['Global_Sales'])
        mpl.title(Element)
        mpl.xlabel("Year")
        mpl.ylabel("Global sales, mil. copies")
        mpl.plot()
        mpl.figure(Element+" global")
        mpl.bar(sales_temp.index,sales_temp['Global_Sales_%'])
        mpl.title(Element)
        mpl.xlabel("Year")
        mpl.ylabel("Part of global sales, %")
        mpl.plot()
        sales_temp.to_csv("D:\Game_Sales Analys\Top_5.csv", sep='\t', mode='a', index=True, header=False)
        counter+=1


