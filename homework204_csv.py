import csv

answers = {'hello':'Hello bro!','how are you?':'i am good', 'goodbye':'I will see you'}

with open('get_answer.csv', 'w', encoding='utf-8') as f:
    fields = ['ask', 'answer']
    writer = csv.DictWriter(f, fields, delimiter=',')
    writer.writeheader()
    #for user in answers:
    #    writer.writerow(user)
    for user in range(1):
    	writer.writerows('1','2') 