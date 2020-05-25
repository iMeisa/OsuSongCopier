from shutil import copyfile
import os


def get_song_name(folder_name):
	try:
		start = folder_name.index(' ')
	except:
		start = 0
	song_name = ''
	for char_index in range(start + 1, len(folder_name)):
		song_name += folder_name[char_index]

	return song_name


login_name = os.getlogin()
osu_path = f'C:\\Users\\{login_name}\\AppData\\Local\\osu!\\Songs'
song_collection_path = f'C:\\Users\\{login_name}\\Desktop\\osu! Songs'
if not os.path.exists(song_collection_path):
	print('Making "osu! Songs" folder')
	os.makedirs(song_collection_path)

new_song_count = 0
song_total = 0
for folder in os.listdir(osu_path):
	for file in os.listdir(f'{osu_path}\\{folder}'):
		if file.endswith('.mp3'):
			song_title = get_song_name(folder)
			song_file = song_collection_path + f'\\{song_title}.mp3'
			if os.path.isfile(song_file):
				print(f'Already copied {song_title}')
				song_total += 1
			else:
				try:
					copyfile(os.path.join(f'{osu_path}\\{folder}', file), os.path.join(song_collection_path, song_file))
					new_song_count += 1
					song_total += 1
					print(f"Copied {song_title}")
				except:
					print(f"Couldn't copy {file} from {osu_path}\\{folder}\\{file}")

print(f'{song_total} songs in folder\nCopied {new_song_count} new songs')
os.system('pause')