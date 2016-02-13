import re   #import the re module having all the regex functions
msg='i =soh fn gm n122222272.12.134.544kjhjk'

regex_obj= re.compile(r'\d\d\d.\d\d.\d\d\d.\d\d\d')
match_obj= regex_obj.search(msg);
print(match_obj.group())
