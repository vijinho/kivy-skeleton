# find file extension used in project
find . -type f | grep -v egg| grep -v 'skeleton/' | cut -d '.' -f 3 | sort |
uniq  | sort
