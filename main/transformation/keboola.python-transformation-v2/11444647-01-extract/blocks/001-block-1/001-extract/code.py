import pandas as pd

dataframe = pd.read_csv("https://nrpzs.uzis.cz/res/file/export/export-2022-02.csv", 
                        sep=';', 
                        encoding='latin-1')

dataframe.to_csv('/data/out/tables/seznam', index=False)
