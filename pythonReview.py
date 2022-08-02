def create_youtube_video(title, description, word1, word2, word3, word4, word5):
	youtubedict = { "title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}, "hashtag": [word1, word2, word3, word4, word5]}
	return youtubedict

def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video

def dislikes(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] += 1
	return youtube_video

def add_comment(youtube_video, username, comment_text):
	youtube_video["comments"][username] = comment_text

def similarity_to_video(dictionary1, dictionary2):
		

dictionary = create_youtube_video("hello", "this video is about hello")
like(dictionary)
dislikes(dictionary)
add_comment(dictionary, "rephael", "nice video")
print(dictionary)