# MusicMatch
MusicMatch is a Python script that allows you to manage your local music library. By simply providing the name (meaningful or otherwise) of the file you want to manage, MusicMatch provides a bunch of tools to organize and manage your file. This can be particularly helpful when names of the files aren't meaningful, as MusicMatch extracts and uses metadata to this effect.

MusicMatch also has extensive Spotify compatibility. It allows the user to export particular songs to their Spotify account, and add aditional songs based on recommendations. It accurately matches the provided music file to a song in the Spotify library, and prompts the user to add that to their songs. Recommendations are provided using the song id, and the user is given information about similar songs they might like. The user may decide to add all, none, or some of these suggestions. For this to work, the user must log in to their Spotify account ofcourse. All this functionality is achieved by using the Spotify API.

This project was a huge learning experience for me. While working on this project, I used the Mutagen library to extract song's metadata and gained experience working with Spotify's developer API. I had to intelligently parse JSON responses and gain familiarity with GET and PUT API calls. For the majority of the functionality provided, I also needed appropriate authorization tokens as well. All in all, it was a challenging but fun experience.
#Screenshots
<img width="600" alt="metadata" src="https://cloud.githubusercontent.com/assets/6366031/15185781/7fe57e28-1768-11e6-8c84-67a89f8648d6.png" hspace = 200px vspace = 50px>
<img width="600" alt="invalid input" hspace = 200px vspace = 50px src="https://cloud.githubusercontent.com/assets/6366031/15185780/7fe473c0-1768-11e6-8479-c4b40a4b5f7a.png">
<img width="600" alt="finish" src="https://cloud.githubusercontent.com/assets/6366031/15185783/7fe88e10-1768-11e6-9a2b-f1e148ea56ef.png" hspace = 200px vspace = 50px>
<img width="600" alt="spotify start" hspace = 200px vspace = 50px src="https://cloud.githubusercontent.com/assets/6366031/15185784/7feacb08-1768-11e6-8514-889a9d159e9b.png">
<img width="600" alt="spotify result" hspace = 200px vspace = 50px src="https://cloud.githubusercontent.com/assets/6366031/15185782/7fe69466-1768-11e6-8fad-aaf868d59a28.png">

