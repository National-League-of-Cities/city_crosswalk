#!/usr/bin/env python
# coding: utf-8

import geopandas as gpd
from bs4 import BeautifulSoup
import pandas as pd
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import os
from tqdm import tqdm

#Function to pull shapefile data
#Returns list of zip files in main directory

def get_zip(url):
    front_page = requests.get(url,verify=False)
    soup = BeautifulSoup(front_page.content,'html.parser')
    zf = soup.find_all("a",href=re.compile(r"zip"))
    zl = [os.path.join(url,i['href']) for i in zf]
    return zl

#parse through list of zip files and append together (might take too much time)
def get_geo_table(geography, url):
    files = get_zip(url)
    pages = []
    for zfile in tqdm(files, desc=f"{geography}",total=len(files)):
        table = gpd.read_file(zfile).iloc[:,:-1]
        pages.append(table)
    fulltable = pd.concat(pages)
    fulltable.to_csv(f"{geography}.csv")


#Block shape files
#get_geo_table("block",r"https://www2.census.gov/geo/tiger/TIGER_RD18/LAYER/TABBLOCK20/")

#County Subdivision files
get_geo_table("countysub",r"https://www2.census.gov/geo/tiger/TIGER2020/COUSUB/")

#block group shape files
#get_geo_table("blockgroup",r"https://www2.census.gov/geo/tiger/TIGER_RD18/LAYER/BG/")
    
#tract Shape files
#get_geo_table("tract",r"https://www2.census.gov/geo/tiger/TIGER_RD18/LAYER/TRACT/")

#MetDiv shape files
#get_geo_table("metdiv",r"https://www2.census.gov/geo/tiger/TIGER2020/METDIV/")

#CBSA shape files
#get_geo_table("cbsa",r"https://www2.census.gov/geo/tiger/TIGER2020/CBSA/")
    
#CSA Shape files
#get_geo_table("csa",r"https://www2.census.gov/geo/tiger/TIGER2020/CSA/")

#CD shape files
#get_geo_table("CD",r"https://www2.census.gov/geo/tiger/TIGER2020/CD/CD118/")

#Place Shape Files
#get_geo_table("place",r"https://www2.census.gov/geo/tiger/TIGER2020/PLACE/")

