## model training
# python -m rasa_nlu.train -c nlu_config.yml --data data/nlu_data.md -o models --fixed_model_name nlu --project current --verbose


def get_entity_and_values(output):
	entity=[]
	value=[]
	for i in range(len(output['entities'])):
		entity_1=output['entities'][i]['entity']
		print(entity_1)
		value_1 =output['entities'][i]['value']
		print(value_1)
		if entity_1=='sex':
			if value_1 == 'male':
				value_1= 'sex = ' + '"M"'
			elif value_1=='female':
				value_1='sex = ' + '"F"'
			else:
				value_1='sex = '+'"Unknown"'

		if entity_1=='age':
			ints=[int(s) for s in value_1.split() if s.isdigit()]
			if 'above' in value_1 or 'greater than' in value_1:
				value_1 = 'age >' + str(ints[0])
			elif 'bellow' in value_1 or 'less than' in value_1:
				value_1 ='age <' + str(ints[0])
			elif 'to' in value_1 and len(ints)==2:
				value_1 = 'age >='+str(min(ints)) + ' and ' + 'age <=' + str(max(ints)) 

		if entity_1=='health':
			if 'very good' in value_1:
				value_1='health =' +str(5)
			elif 'good' in value_1:
				value_1='health >=' +str(4)
			elif 'bad' in value_1:
				value_1='health <=' +str(2)
			elif 'normal' in value_1:
				value_1='health =' +str(3)
			else:
				value_1='health =' +str(1)

		if 'grade' in entity_1:
			ints=[int(s) for s in value_1.split() if s.isdigit()]
			if 'above' in value_1 or 'greater than' in value_1:
				value_1 = 'G1 >' + str(ints[0]) + ' and ' + 'G2 > '+ str(ints[0]) + ' and ' + 'G3 > ' + str(ints[0])  
			elif 'bellow' in value_1 or 'less than' in value_1:
				value_1 = 'G1 <' + str(ints[0]) + ' and ' + 'G2 < '+ str(ints[0]) + ' and ' + 'G3 < ' + str(ints[0])  
			elif 'to' in value_1 and len(ints)==2:
				value_1 = 'grades >='+str(min(ints)) + ' and ' + 'grades <=' + str(max(ints)) 

		entity.append(entity_1)
		value.append(value_1)
		print(entity,value)
	return entity, value







