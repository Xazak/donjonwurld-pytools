from random import choice, random, randint

#starting from the overall mannequin, as it were; invoking this should spit out a generated NPC
def mannequin():
#   do the usual clearing out
	is_masked = 0

#   get all of the variables together and stick them on the mannequin
#	name = pickname()
	gender = pickgender()
	race = pickrace()
	age = pickage(race)
#	appearance = pickappearance(gender,race,job)
	instinct = pickinstinct()
	knack = pickknack()

#   report all of the mannequin's features
	if is_masked:
		print 'Race: ' + race + ' (Masked)'
	else:
		print 'Race: ' + race
	print 'Gender: ' + gender
	print 'Age:  ' + age
	print 'Wants To: ' + instinct
	print 'Using: ' + knack
	return '...' #provides space between, else prints out 'None'

def pickrace():
	n = randint(1, 100)
	if n >= 50:
		is_masked = 1
		n = randint(1, 99)
	if n >= 1 and n <= 25:
		return 'Elvarin'
	elif n >= 26 and n <= 40:
		return 'Huma'
	elif n >= 41 and n <= 55:
		return 'Dwarro'
	elif n >= 56 and n <= 65:
		return 'Thanae'
	elif n >= 66 and n <= 75:
		return 'Surrel'
	elif n >= 76 and n <= 85:
		return 'Kyhrro'
	elif n >= 86 and n <= 95:
		return 'Talar'
	elif n >= 96 and n <= 99:
		return 'Zomai'

def pickgender():
	return choice(['Male', 'Female'])

def pickage(race):
	if race == 'Dwarro':
		ageresult = randint(30, 200)
	elif race == 'Elvarin':
		ageresult = randint(10, 50)
	elif race == 'Huma':
		ageresult = randint(16, 80)
	elif race == 'Kyhrro':
		ageresult = randint(2, 5)
	elif race == 'Surrel':
		ageresult = randint(1, 4)
	elif race == 'Talar':
		ageresult = randint(15, 150)
	elif race == 'Thanae':
		ageresult = randint(16, 60)
	elif race == 'Zomai':
		ageresult = randint(3, 6)
	return(str(ageresult))

def pickinstinct():
	instinctList = ['avenge','spread the good word','reunite with a loved one','make money','make amends','explore a mysterious place','uncover a hidden truth','locate a lost thing','kill a hated foe','conquer a faraway land','cure an illness','craft a masterwork','survive just one more day','earn affection','prove a point','be smarter, faster, and stronger','heal an old wound','extinguish an evil forever','hide from a shameful fact','evangelize','spread suffering','prove worth','rise in rank','be praised','discover the truth','make good on a bet','get out of an obligation','convince someone to do their dirty work','steal something valuable','overcome a bad habit','commit an atrocity','earn renown','ccumulate power','save someone from a monstrosity','teach','settle down','get just one more haul','preserve the law','discover','devour','restore the family name','live a quiet life','help others','atone','prove their worth','gain honor','expand their land','gain a title','retreat from society','escape','party','return home','serve','reclaim what was taken','do what must be done','be a champion','avoid notice','help a family member','perfect a skill','travel','overcome a disadvantage','play the game','establish a dynasty','improve the realm','retire','recover a lost memory','battle','become a terror to criminals','raise dragons','live up to expectations','become someone else',"do what can't be done",'be remembered in song','be forgotten','find true love','lose their mind','indulge','make the best of it','find the one','destroy an artifact','show them all','bring about unending summer','fly','find the six-fingered man','wake the ancient sleepers','entertain','follow an order','die gloriously','be careful','show kindness','not screw it all up','uncover the past','go where no man has gone before','do good','become a beast','spill blood','live forever','hunt the most dangerous game','hate','run away']
	return(choice(instinctList))

def pickknack():
	knackList = ['criminal connections','muscle','skill with a specific weapon','hedge wizardry','comprehensive local knowledge','noble blood','a one-of-a-kind item','special destiny','unique perspective','hidden knowledge','magical awareness','abnormal parentage','political leverage','a tie to a monster','a secret','true love','an innocent heart','a plan for the perfect crime','a one-way ticket to paradise','a mysterious ore','money, money, money','divine blessing','immunity from the law','prophecy','secret martial arts techniques','a ring of power','a much-needed bag of potatoes','a heart','a fortified position','lawmaking','tongues','a discerning eye','endurance','a safe place','visions','a beautiful mind','a clear voice','stunning looks','a catchy tune','invention','baking','brewing','smelting','woodworking','writing','immunity to fire','cooking','storytelling','ratcatching','lying','utter unremarkableness','mind-bending sexiness','undefinable coolness','a way with knots','wheels of polished steel','a magic carpet','endless ideas','persistence','a stockpile of food','a hidden path','piety','resistance to disease','a library','a silver tongue','bloodlines','an innate spell','balance','souls','speed','a sense of right and wrong','certainty','an eye for detail','heroic self-sacrifice','sense of direction','a big idea','a hidden entrance to the city','the love of someone powerful','unquestioning loyalty','exotic fruit','poison','perfect memory','the language of birds','a key to an important door','metalworking','mysterious benefactors','steely nerves','bluffing','a trained wofl','a long-lost sibling, regained','an arrow with your name on it','a true name','luck','the attention of supernatural powers','kindness','strange tattoos','a majestic beard','a book in a strange language','power overwhelming','delusions of grandeur','the wind at his back and a spring in his step']
	return(choice(knackList))

#this will only execute if this is the main script, so it can be called by other fnxns
if __name__ == '__main__':
	print mannequin()
