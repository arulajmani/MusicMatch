# MusicMatch
MusicMatch is a Python script that allows you to manage your local music library. By simply providing the name (meaningful or otherwise) of the file you want to manage, MusicMatch provides a bunch of tools to organize and manage your file. This can be particularly helpful when names of the files aren't meaningful, as MusicMatch extracts and uses metadata to this effect.

MusicMatch also has extensive Spotify compatibility. It allows the user to export particular songs to their Spotify account, and add aditional songs based on recommendations. It accurately matches the provided music file to a song in the Spotify library, and prompts the user to add that to their songs. Recommendations are provided using the song id, and the user is given information about similar songs they might like. The user may decide to add all, none, or some of these suggestions. For this to work, the user must log in to their Spotify account ofcourse. All this functionality is achieved by using the Spotify API.

This project was a huge learning experience for me. While working on this project, I used the Mutagen library to extract song's metadata and gained experience working with Spotify's developer API. I had to intelligently parse JSON responses and gain familiarity with GET and PUT API calls. For the majority of the functionality provided, I also needed appropriate authorization tokens as well. All in all, it was a challenging but fun experience.
#Screenshots

