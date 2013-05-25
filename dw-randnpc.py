from random import choice, random, randint
import sys
import weightedlist

def statblock():
	if isMasked:
		print 'Race:   ' + race + ' (Masked)'
	else:
		print 'Race:   ' + race
	print 'Sex:    ' + gender.title()
	print 'Age:    ' + age.title()
	print 'Job:    ' + job.title()
	print 'Looks:  ' + appearance
	print 'Wants:  to ' + instinct
	print 'Using:  ' + knack
	return ''

def narrative():
	if gender == 'male':
		pronoun = 'he'
	else:
		pronoun = 'she'
	if isMasked:
		print "You see before you a %s Masked %s. %s is %s, with %s. %s is employed as a %s; %s wants to %s using %s." % (gender, race, pronoun.title(), age, appearance, pronoun.title(), job, pronoun, instinct, knack)
	else:
		print "You see before you a %s %s. %s is %s, with %s. %s is employed as a %s; %s wants to %s using %s." % (gender, race, pronoun.title(), age, appearance, pronoun.title(), job, pronoun, instinct, knack)
	return ''

def pickrace():
        raceList = [(20, 'Elvarin'),(15, 'Huma'),(10, 'Dwarro'),(10, 'Thanae'),(10, 'Surrel'),(10, 'Kyhrro'),(10, 'Talar'),(5, 'Zomai'),(1, 'Masked')]
        raceResult = weightedlist.pick(raceList)
        if raceResult == 'Masked':
                isMasked = 1
                raceResult = weightedlist.pick(raceList)
        else:
                isMasked = 0
        return(raceResult,isMasked)

def pickgender():
	return choice(['male', 'female'])

def pickage():
	return choice(['young','mature','an adult','an elder','aged','fresh-faced','nubile','seasoned','inexperienced','youthful','settled','sophisticated','graceful'])

def pickjob():
	jobList = ['anchorite monk','apothecary','apprentice seer','apprentice wizard','hedge wizard','bailiff','barber','boatman','bodyguard','bondsman','bounty hunter','burgher','cadet','camp follower','cartographer','cenobite monk','bone picker','charcoal burner','chimneysweep','coachman','dilettante','drover','embalmer','entertainer','envoy','ex-convict','exciseman','farmer','ferryman','fieldwarden','fisherman','frogwife','gambler','grave robber','grave warden','hunter','jailer','knight errant','lamplighter','man-at-arms','marine','mediator','mercenary','messenger','militiaman','miner','minstrel','mystic','noble','outlaw','outrider','packmaster','peasant','penitent','pilgrim','pit fighter','prelate','raconteur','ratcatcher','river warden','roadwarden','rogue','scribe','scout','seaman','seer','servant','skald','skirmisher','smuggler','sneak','soldier','squire','stevedore','student','thief','thrall','thug','toll keeper','tradesman','vagabond','valet','watchman','whaler','wise man','woodsman','missionary','fighter','bard','cleric','druid','paladin','ranger','wizard']
	return(choice(jobList))

def pickappearance(job):
	eyeList = ['knowing','fiery','joyous','kind','sharp','sad','wise','wild','haunting','hard','dead','eager','animal','shifty','haunted']
	hairList = ['fancy hair','wild hair','a stylish cap','a tonsure','strange hair','a bald pate','a furry hood','messy hair','braided hair','wild hair','shorn hair','a battered helm','a polished helmet','a drab-colored hood','cropped hair','styled hair','a shapeless hat']
	clothingList = ['finery','travelling clothes','poor clothes','flowing robes','habit','common garb','ceremonial garb','practical leathers','weathered hides','cape','camouflage','dark clothes','fancy clothing','common tunic','worn robes','stylish robes']
	bodyList = ['fit','well-fed','thin','knobby','flabby','built','lithe','ravaged','bulky','pudgy']
	return '%s eyes and %s, wearing %s on a %s frame' % (choice(eyeList), choice(hairList), choice(clothingList), choice(bodyList))
	
def pickinstinct():
	instinctList = ['avenge','spread the good word','reunite with a loved one','make money','make amends','explore a mysterious place','uncover a hidden truth','locate a lost thing','kill a hated foe','conquer a faraway land','cure an illness','craft a masterwork','survive just one more day','earn affection','prove a point','be smarter, faster, and stronger','heal an old wound','extinguish an evil forever','hide from a shameful fact','evangelize','spread suffering','prove worth','rise in rank','be praised','discover the truth','make good on a bet','get out of an obligation','convince someone to do their dirty work','steal something valuable','overcome a bad habit','commit an atrocity','earn renown','ccumulate power','save someone from a monstrosity','teach','settle down','get just one more haul','preserve the law','discover','devour','restore the family name','live a quiet life','help others','atone','prove their worth','gain honor','expand their land','gain a title','retreat from society','escape','party','return home','serve','reclaim what was taken','do what must be done','be a champion','avoid notice','help a family member','perfect a skill','travel','overcome a disadvantage','play the game','establish a dynasty','improve the realm','retire','recover a lost memory','battle','become a terror to criminals','raise dragons','live up to expectations','become someone else',"do what can't be done",'be remembered in song','be forgotten','find true love','lose their mind','indulge','make the best of it','find the one','destroy an artifact','show them all','bring about unending summer','fly','find the six-fingered man','wake the ancient sleepers','entertain','follow an order','die gloriously','be careful','show kindness','not screw it all up','uncover the past','go where no man has gone before','do good','become a beast','spill blood','live forever','hunt the most dangerous game','hate','run away']
	return(choice(instinctList))

def pickknack():
	knackList = ['criminal connections','muscle','skill with a specific weapon','hedge wizardry','comprehensive local knowledge','noble blood','a one-of-a-kind item','special destiny','unique perspective','hidden knowledge','magical awareness','abnormal parentage','political leverage','a tie to a monster','a secret','true love','an innocent heart','a plan for the perfect crime','a one-way ticket to paradise','a mysterious ore','money, money, money','divine blessing','immunity from the law','prophecy','secret martial arts techniques','a ring of power','a much-needed bag of potatoes','a heart','a fortified position','lawmaking','tongues','a discerning eye','endurance','a safe place','visions','a beautiful mind','a clear voice','stunning looks','a catchy tune','invention','baking','brewing','smelting','woodworking','writing','immunity to fire','cooking','storytelling','ratcatching','lying','utter unremarkableness','mind-bending sexiness','undefinable coolness','a way with knots','wheels of polished steel','a magic carpet','endless ideas','persistence','a stockpile of food','a hidden path','piety','resistance to disease','a library','a silver tongue','bloodlines','an innate spell','balance','souls','speed','a sense of right and wrong','certainty','an eye for detail','heroic self-sacrifice','sense of direction','a big idea','a hidden entrance to the city','the love of someone powerful','unquestioning loyalty','exotic fruit','poison','perfect memory','the language of birds','a key to an important door','metalworking','mysterious benefactors','steely nerves','bluffing','a trained wolf','a long-lost sibling, regained','an arrow with your name on it','a true name','luck','the attention of supernatural powers','kindness','strange tattoos','a majestic beard','a book in a strange language','power overwhelming','delusions of grandeur','the wind at his back and a spring in his step']
	return(choice(knackList))

if __name__ == '__main__': # this will only execute if this is the main script, so it can be called by other fnxns
#   get all of the variables together and stick them on the mannequin
#	name = pickname()
	isMasked = 0
	gender = pickgender()
	race, isMasked = pickrace()
	age = pickage()
	job = pickjob()
	appearance = pickappearance(job)
	instinct = pickinstinct()
	knack = pickknack()
	if len(sys.argv) >= 2: #this is how to get command line options
		if sys.argv[1] == '-statblock' or sys.argv[1] == '-sb' or sys.argv[1] == '-stat':
			print statblock()
		elif sys.argv[1] == '-story' or sys.argv[1] == '-narrative' or sys.argv[1] == '-n':
			print narrative()
	else:
		print statblock()
