# Weather Assistant

## Information
Weather Assistant chatbot using Rasa Open Source and Weather API by OpenWeather data. 

Chatbot is lightly trained to understand weather related questions via custom actions and default question provided by Rasa. 

Question format for inquiring the weather can be found on ```data/nlu.yml```

## Using the bot

### Install required pip packages
```
pip install -r requirements.txt
```
### Train the model
```
python -m rasa train
```
### Use the weather assistant
```
python -m rasa run actions
python -m rasa shell
```