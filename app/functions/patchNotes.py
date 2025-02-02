import aiohttp
from app.functions.aliases import *
from app.functions.printFunctions import *

async def fetch(session, url):
	async with session.get(url) as response:
		return await response.text()

async def patchNotes(channel,text):
	if len(text)!=2:
		await channel.send('Use with [patchnotes/hero,X], where X is number of patches ago, or a search term.')
		return
	async with channel.typing():
		text=text[1]
		splitText=text.split(',')
		hero=aliases(splitText.pop(0)).replace('ú','u').lower().translate({ord(i):None for i in "' _-."}).replace('thebutcher','butcher')
		async with aiohttp.ClientSession() as session:
			page = await fetch(session, 'https://heroespatchnotes.com/hero/'+hero+'.html')
			patches=page.split('<h3>')
			if splitText:
				text=splitText.pop(0)
				if text.isdigit():
					if int(text)<len(patches):
						patch=patches[int(text)]
					else:
						await channel.send("The hero doesn't have "+text+' patches yet.')
						return
				else:
					for trialPatch in patches[1:]:
						if text.lower() in trialPatch.lower():
							patch=trialPatch
							break
					else:
						await channel.send('That has never been changed!')
						return
			else:
				patch=patches[1]

			remove=['<small class="hidden-xs">','  ','<li>','<p>','<em>','</li>','</p>','</em>','</ul>','<blockquote>','</blockquote>','<span class="text-warning">','amp;']
			for i in remove:
				patch=patch.replace(i,'')
			output='**'+patch.split('<')[0]+'**'	#Date and version
			patch='>'.join(patch.split('<h4')[1].split('>')[1:])
			#output+=patch.split('<')[0]+':'	#Type (bug fix, hero update)
			patch='>'.join(patch.split('>')[1:])
			patch=patch.split('</div>')[0]
			patch=patch.replace('\n',' ').replace('<strong>Developer Comment:</strong> ','\n***Developer Comment***: *').replace('<strong>','\n**').replace('</strong>',':** ').replace('<ul>',' ')
			patch=patch.replace('\n**Talents:**','').replace('\n**Abilities:**','').replace('**Stats:**','').replace(' Health Regen ',', Health Regen ')
			if '</span> <a class="label label-warning"' in patch:#Undocumented HTML
				patch=patch.split('</span> <a class="label label-warning"')
				patch='\n'.join([patch[0]]+[i.split('Undocumented <i class="fa fa-external-link"></i></a>    ')[1] for i in patch[1:]])
			output+=patch
			if 'Developer Comment' in output:
				output=output.strip()+'*'

			await printLarge(channel,output)

      