
# Grab CSVs

import requests




urls = [
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/1998.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/1999.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2000.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2001.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/20v02.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2003.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2004.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2005.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2006.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2007.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2008.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2009.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2010.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2011.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2012.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2013.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2014.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2015.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2016.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2017.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2018.csv",
    "https://raw.githubusercontent.com/AccessLibCon/conference-data/master/csv/2019.csv"
]

for u in urls:
    print(u[:-4])
    r = requests.get(u, allow_redirects=True)
    open(u, 'wb').write(r.content)
