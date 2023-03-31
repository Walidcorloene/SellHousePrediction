<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>

<h1>
  hey there
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
</h1>


### 🧑‍💻: About Us :
- :telescope: We are Studying Data & AI and contributing for building a image analyzer of LinkedIn profile pictures.

- At the origin of the idea and our Business Coach : Jean-Charles TASSAN
- Our Technical Coach : Théo GIGANT


# SellHousePrediction



## Ressources

develop a model to predict sells houses of a specific house with a specific parameters

## Dependencies for the Scraper

* Anaconda or Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

## Setup

1. Create a new conda env named SellsPrediction (if you haven't already) for the project in the Conda application or in the terminal:
```
conda create --name SellsPrediction python=3.9.7 
```

2. Activate the conda env (you can check your availables env with: conda env list):
```
conda activate SellsPrediction
```

3. Install the project python dependencies :
```
pip install -r requirements.txt
```

5. Launch the API :

```
python app.py
```


<div align="center">
  <img src="https://lalalab.zendesk.com/hc/article_attachments/4411304152338/LoathsomeWaryDugong-max-1mb.gif" width="300"/>
</div>


## Project structure

    
-- template/form.html : the main page with the form
    
-- template/results : the results page after submiting

-- model.joblib : a trained model with XGBoost sur une df de 1500 rows
    
-- app.py : the API whom imported the model

-- requirement.txt : the library that you need to run this project
----- 




