#!/usr/bin/python3
  
import pandas as pd

# these following two lines are for writing to file
# use this when you are not rendering to a window
import matplotlib
matplotlib.use('Agg')

# create some graphs
import matplotlib.pyplot as plt

def main():
    # define the name of our xls file
    excel_file = 'movies.xls'

    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)

    movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)

    movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)

    movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

    movies.drop_duplicates(inplace=True)

    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    movies.to_excel('/home/student/static/myexcel.xls')

    print(sorted_by_gross.head(10))

    sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")
    plt.savefig("/home/student/static/stackedbar.png", bbox_inches='tight')

main()
