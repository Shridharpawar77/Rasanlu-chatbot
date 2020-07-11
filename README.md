# Rasanlu-chatbot
# Rasa currently only supports Python version <= 3.6. If you have a higher version of Python, you can set up a new environment in conda using the following command
conda create -n rasa python=3.6

conda activate rasa

## installing Rasa and its dependencies
pip install -r requirements.txt

## install a spaCy English language model
python -m spacy download en

## Training the NLU classifier
python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models --fixed_model_name nlu --project current --verbose

## starting the chatbot
python chatbot.py
