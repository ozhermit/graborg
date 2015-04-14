# graborg
Used to grab and organise malware samples for tracking. Downloads files and appends details to csv file (Name, MD5, FileSize, Timestamp, Source) then rename the file to its md5 hash in the samples folder.

#Usage
./graborg.py -u URL

Eg. ./graborg.py -u http://www.ozhermit.com/wp-content/uploads/2014/11/kippo.jpg

#Output
Currently the output is to a .csv file.

user@host:/security/tools/graborg$ more graborg-log.csv

MD5,Filename,File Size,Time Acquired,Source

e07c771cbf9216d7dc93cff31c9d6d94,kippo.jpg,76192,14/04/2015 10:36:16,http://www.ozhermit.com/wp-content/uploads/2014/11/kippo.jpg

#Todo
Add TOR so files can be downloaded anonymously

Add support for other protocols to download files over

Add additional User-Agent options

#Contact
Any issues or feedback please feel free to contact me via <a href="https://twitter.com/ozhermit">Twitter</a>

