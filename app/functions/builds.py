from urllib.request import urlopen
from app.functions.printFunctions import getHeroes
from app.functions.aliases import aliases

build_base_path = r'./data/builds/'


async def trimForIcyVeinsAndPsionicStorm(hero):
	return hero.lower().replace('_','-').replace('.','').replace("'","").replace('ú','u').replace(' ','-')

async def guide(hero,channel):
	output=''
	with open(r'./builds/mindHawkBuilds.txt','r') as f:
		for i in f:
			if await trimForIcyVeinsAndPsionicStorm(hero) in i:
				output+='MindHawk: <'+i.replace('\n','')+'>\n'
	with open(r'./builds/otherBuilds.txt','r') as f:
		for i in f:
			if hero in i:
				authorAndLink=i.split('; ')[1]
				[author,link]=authorAndLink.split(': ')
				output+=author+': <'+link.replace('\n','')+'>\n'
	
	with open(r'./builds/icyVeinsHeroes.txt','r') as f:
		for i in f:
			if hero==aliases(i):
				await channel.send(output+'Icy Veins: <https://www.icy-veins.com/heroes/'+(await trimForIcyVeinsAndPsionicStorm(hero)).replace('kelthuzad','kel-thuzad')+'-build-guide>')#<> prevents thumbnails.
				return

	with open(r'./builds/elitesparkleBuilds.txt','r') as f:
		for i in f:
			if await trimForIcyVeinsAndPsionicStorm(hero) in i:
				await channel.send(output+'Elitesparkle: <'+i[:-1]+'>')#<> prevents thumbnails. [:-1] removes the \n at end of i
				return
		if output:
			await channel.send(output)
		else:
			await channel.send("That's not a hero!")

def updateBuilds():
	page=[i.strip().decode('utf-8') for i in urlopen('https://elitesparkle.wixsite.com/hots-builds') if "var warmupData = {" in i.strip().decode('utf-8')][0]
	with open(r'./builds/elitesparkleBuilds.txt','w+') as f:
		for hero in getHeroes():
			hero=aliases(hero).lower().replace('_','-').replace('.','').replace("'","")
			heropage=page[page.index('builds\/'+hero):]
			code=heropage[heropage.index('-'):heropage.index('\/"')]
			output='https://psionic-storm.com/en/builds/'+hero+code+'\n'
			print(output)
			f.write(output)

if __name__=='__main__':
	updateBuilds()
