

users:list=[
    {'username':'oliwia', 'location':'łódź','posts':1,'usermessage':['zyczenia1','kocham legie','sprzedam opla','kiwi']},
    {'username':'paweł', 'location':'ostróda','posts':2,'usermessage':['zyczenia2','kocham legie1','sprzedam opla1']},
    {'username':'eliza', 'location':'radom','posts':3,'usermessage':['zyczenia3','kocham legie2']},
    {'username':'filip', 'location':'dęblin','posts':4,'usermessage':['zyczenia4','kocham legie3','sprzedam opla3','kiwi3']},
]

for user in users[1:]:
    print(f'twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiadomość {user['usermessage'][-1]}')
    
#     twój znajomy filip z miejscowości dęblin opublikował 1 post o treści: zyczenia
