from rasa_nlu.model import Interpreter
from rasa_trial import get_entity_and_values
import pandas as pd
import pandasql

## load the nlu model
nlu_model = Interpreter.load('./models/current/nlu')

## load the data
data = pd.read_csv('./data/student-mat.csv')

def generate_query(entity,values):
	if not entity:
		text ='select * from data'
	else:
		text = 'select * from data where ' 
	for i in range(len(entity)):
	    if i==0:
	        text = text+values[i]
	    else:
	        text = text + ' and ' + values[i]
	return text

# output = nlu_model.parse('Who are the students from with grades above 7?')
# output = nlu_model.parse('How many female students from age 17 to 19?')
# output = nlu_model.parse('What % of students with health status good')

def get_response(user_question):
	output = nlu_model.parse(user_question)
	entity,values = get_entity_and_values(output)
	text = generate_query(entity,values)
	bot_ans = 'hi'

	if output['intent']['name'] == 'percentage':
		number = pandasql.sqldf(text).shape[0]
		percentage = (number/data.shape[0])*100
		bot_ans = '% of students = '+ str(percentage)
	elif output['intent']['name'] == 'number':
		number = pandasql.sqldf(text).shape[0]
		bot_ans = 'number is  = ' + str(number)
	elif output['intent']['name'] == 'all_info':
		bot_ans = pandasql.sqldf(text)

	return bot_ans


