# from app.functions.aliases import *
# from app.functions.printFunctions import *
import json
import csv
import pandas as pd
import tabulate as tab

def get_current_season():
		csvPath = './app/data/seasons.csv'
		jsonPath = './app/data/seasons.json'
		jsonArray = []

		with open(csvPath, 'r', encoding='utf-8' ) as f:
			csvReader = csv.DictReader(f)
			for row in csvReader: 
				jsonArray.append(row)

		with open(jsonPath, "w", encoding='utf-8') as outfile:
			json.dump(jsonArray, outfile,  indent=4, sort_keys=True)
			outfile.close()
		
		df = pd.DataFrame(jsonArray)
		df = df.set_index(['StartDate'])
		df = df.sort_values(by=['StartDate'], ascending=False)
		df = df.iloc[:1,:]		
		url = df['Url'][0]
		df = df.drop(axis=1, columns=['Url'])		
		string = """
						```
{seasons}
						```
Url - {url}
						""".format(seasons=tab.tabulate(df, headers='keys', tablefmt='psql'), url=url)
		return(string)

def get_seasons():
		csvPath = './app/data/seasons.csv'
		jsonPath = './app/data/seasons.json'
		jsonArray = []

		with open(csvPath, 'r', encoding='utf-8' ) as f:
			csvReader = csv.DictReader(f)
			for row in csvReader: 
				jsonArray.append(row)

		with open(jsonPath, "w", encoding='utf-8') as outfile:
			json.dump(jsonArray, outfile,  indent=4, sort_keys=True)
			outfile.close()

		df = pd.DataFrame(jsonArray)
		df = df.set_index(['StartDate'])
		df = df.sort_values(by=['StartDate'], ascending=False)
		df = df.drop(axis=1, columns=['Url'])
		df = df.iloc[:5,:]
		print(tab.tabulate(df, headers='keys', tablefmt='psql'))
		string = """
						```
{seasons}
						```
						""".format(seasons=tab.tabulate(df, headers='keys', tablefmt='psql'))
		return(string)

def get_season(name):	
		jsonPath = './app/data/seasons.json'
		jsonArray = []

		with open(jsonPath, 'r', encoding='utf-8' ) as f:
			jsonArray = json.load(f)

		jsonArray = [h for h in jsonArray if h['Season'] == name]		

		df = pd.DataFrame(jsonArray)
		df = df.set_index(['StartDate'])
		df = df.sort_values(by=['StartDate'], ascending=False)
		df = df.iloc[:1,:]		
		url = df['Url'][0]
		df = df.drop(axis=1, columns=['Url'])		
		string = """
						```
{seasons}
						```
Url - {url}
						""".format(seasons=tab.tabulate(df, headers='keys', tablefmt='psql'), url=url)
		return(string)