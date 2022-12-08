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
### Use the weather assistant by running 2 different windows, 1 to run actions and 2 to interact the shell
```
python -m rasa run actions
python -m rasa shell
```

## Example questions to ask.
```
    - How is the weather in Helsinki?
    - What is the weather in London?
    - Tell me the weather in Singapore?
    - I want to know the weather in Agadir?
    - Weather in Budapest?
```