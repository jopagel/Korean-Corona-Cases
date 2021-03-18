# Korean-Corona-Cases

## Files 

- [requirements.txt](https://github.com/jopagel/Korean-Corona-Cases/blob/main/requirements.txt): defines the requirements of the project
- [PatientInfo.csv](https://github.com/jopagel/Korean-Corona-Cases/blob/main/PatientInfo.csv): dataset used for the analysis.
- [Data_Analysis.ipynb](https://github.com/jopagel/Korean-Corona-Cases/blob/main/Data_Analysis.ipynb): main Jupyter Notebook with the Python Code and Interpretation




## Introduction

The preceding analysis deals with a structured dataset of Corona patients in Korea. It is provided by the KCDC (Korea Centers for Disease Control & Prevention) and consists of 14 features discribing 5,165 patients infected with the Corona Virus in 2020. It can be downloaded on [Kaggle](https://www.kaggle.com/kimjihoo/coronavirusdataset).

## Questions of interest

The analysis includes different data preparation steps that transform the initial dataset into a suitable selection of features to answer the following questions:

- Which province had the most Corona cases?
- Is there any difference in duration of illness for male vs female citizen?
- Which features have the biggest influence on the duration of the infection?

These answers to these questions can be found in the [Notebook](https://github.com/jopagel/Korean-Corona-Cases/blob/main/Data_Analysis.ipynb).

## Central results 

The main findings of the preceding analysis are:
- The province with the most Corona Cases in the dataset is Seoul, followed by Gyeongsangbuk-do and Gyeonggi-do.
- There is no significant difference in duration of the Corona infection for men vs women
- The categoric feature age_100s and the province Daegu show the highest influence on the duration auf the infection


More detailed answers to these questions can be found in the [Notebook](https://github.com/jopagel/Korean-Corona-Cases/blob/main/Data_Analysis.ipynb).


## Acknowledgements 

- [[NeurIPS 2020] Data Science for COVID-19 (DS4C) | Kaggle](https://www.kaggle.com/kimjihoo/coronavirusdataset)
- [Korea (Rep.): Städte — Einwohnerzahlen, Karten, Grafiken, Wetter und Web-Informationen (citypopulation.de)](https://www.citypopulation.de/de/southkorea/cities/)
- [South Korea struggling to control resurgence of coronavirus | Asia| An in-depth look at news from across the continent | DW | 28.08.2020](https://www.dw.com/en/south-korea-struggles-with-coronavirus/a-54727852)
