import re,os
openProfile=open('suven/linkedin_comments.txt','r')
fileRead=openProfile.read()
print(fileRead)
matchFoundEmail=[]
matchFoundNumber=[]
matchFoundMobile=[]
phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{4}|\(\d{10}\))? # first 3 digits
 (\s|-|\.) # separator
 (\d{10}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)
# TODO: Create email regex.
#emailAddressRegex=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
##for finds in phoneRegex.findall(fileRead):
## if finds in ('-',finds[1],finds[3],finds[5],finds[8]):
##     matchFound.append(finds)
##     print(matchFound)
#for emailFinds in emailAddressRegex.findall(openProfile.read()):
#	 matchFound.append(emailFinds[0])
#     print(matchFound)
emailAddressRegex=re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
mobileNumberRegex=re.compile(r'''(
 (\+)? # area code
 (\d{2})?
 (\s|-|\.)? # separator
 (\d{5}) # first 3 digits
 (\s|-|\.)? # separator
 (\d{5}) # last 4 digits
 )''', re.VERBOSE)
with open("suven/linkedin_comments.txt") as f:
    for line in f:
      result = emailAddressRegex.findall(line)

      if  len(result) != 0:
        matchFoundEmail.append(result)
with open("suven/linkedin_comments.txt") as f:
    for line in f:
      result = mobileNumberRegex.findall(line)

      result=[tuple(j for j in i if j)[0] for i in result]
      if  len(result) != 0:
        matchFoundMobile.append(result)
with open("suven/linkedin_comments.txt") as f:
    for line in f:
      result = phoneRegex.findall(line)
      result=[tuple(j for j in i if j)[0] for i in result]
      if  len(result) != 0:
        matchFoundNumber.append(result)
print(matchFoundEmail)
print(matchFoundNumber)
print(matchFoundMobile)

#with open('suven/linkedin_comments_Extracted.txt', 'a') as out_file:
#     out_file.writelines(result)
#
#
#
#
#
#     #for i in result:
#     #  list1=i.split()
#     #    if len(list1)>0:
#     #  	   matchFound.append(list1)

#import re,os,pyperclip
#openProfile=open('suven/linkedin_comments.txt','r')
#readContent=openProfile.read()
#phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))? # area code
# (\s|-|\.)? # separator
# (\d{3}) # first 3 digits
# (\s|-|\.) # separator
# (\d{4}) # last 4 digits
# (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
# )''', re.VERBOSE)
#
#
## TODO: Create email regex.
#emailRegex = re.compile(r'''(
#    [a-zA-Z0-9._%+-]+      # username
#    @                      #  symbol
#    [a-zA-Z0-9.-]+         # domain name
#    (\.[a-zA-Z]{2,4})      # dot-something
#    )''', re.VERBOSE)
#
#
#
## TODO: Find matches in text file.
#text = str(readContent)
#matches = []
#for groups in phoneRegex.findall(text):
#       phoneNum = '-'.join([groups[1], groups[3], groups[5],groups[8]])
#       if groups[8] != '':
#           phoneNum += ' x' + groups[14]
#       matches.append(phoneNum)
#for groups in emailRegex.findall(text):
#       matches.append(groups[0])
#
#
## TODO: Copy results to another text file.
#if len(matches) > 0:
#    pyperclip.copy('\n'.join(matches))
#    print('Copied to clipboard:')
#    print('\n'.join(matches))
#else:
#    print('No phone numbers or email addresses found.')
#
#