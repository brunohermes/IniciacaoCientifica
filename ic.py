"""
Created on Sat Jul 29 20:57:34 2023

@author: Bruno
"""
import pandas as pd
#import numpy as np

source = pd.read_excel("dados.xlsx")

source = source.drop(columns=['nome_4md','regiao', 'atbt', 'qtde_u_csrecebem_os_creditos', 'n_sistemas']) [source["uf"].str.contains("PR")]
