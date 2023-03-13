#Regex eshte nje sekuence me karaktere e cila formon nje model kerkimi

#Metodat e regex 
"""
findall	Krijon nje liste me te gjithe gjetjet
search  Krijon nje objekt i cili eshte i njejte me stringun qe kerkojme
split	Krijon nje liste, nga ku cdo element perbehet nga prerja e cdo elemnti qe eshte gjetur: 
  "Sot eshte nje dite shume e bukur" nese vendosim te ndajme ne elment ne cdo hapsire boshe ather do kemi
  [Sot,eshte,nje,dite,shume,e,bukur]

sub	zevendeson nje string me nje tjeter nese perputhet me modelin

Karakteret

[]	Nje set me karaktere	"[a-m]"	
\	Sinjalizon nje sekuence speciale "\d"	
.	Cdo karakter pervec \n 	"he..o"	  
^	Fillon me..."^hello"	
$	Mbaron me with	"planet$"	
*	0 ose disa raste	"he.*o"	
+	1 ose me shume raste	"he.+o"	
?	0-1 raste	"he.?o"	
{}	Raste ekzakte	"he.{2}o" 	
|	Ose 	"falls|stays"	
()	Perzgjidh dhe grupo

\A	Kthen elementin e gjetur nese ai ndodhet ne fillim te string 	"\AThe"	
\b	Kthen elementin e gjetur nese ai ndodhet ne fillimin e fjalise ose ne fundin e saj.(r siguron qe eshte raw string) r"\bain"
r"ain\b"	
\B	Kthen elementet qe perputhen pavarsisht vendodhjes ne fillim apo ne fund r"\Bain" r"ain\B"	
\d	Sjell te gjith rastet nese ka numra  (numrat nga 0-9)	"\d"	
\D	Sjell te gjithe rastet kur NUK KA NUMRA	"\D"	
\s	Sjell te gjithe rastet kur ka hapsira boshe	"\s"	
\S	Sjell te gjithe rastet kur NUK KA HAPSIRA BOSHE	"\S"	
\w	Sjell te gjithe	rastet kur ka shkronja, numra ose simbole te tipit _"\w"	
\W	Sjell te gjithe rastet kur nuk ka asnje shkronj karakter"\W"	
\Z	Sjell te gjithe rastet kur karaktert e kerkuar ndodhen ne fund te string
I am in Spain 	"Spain\Z" == [Spain] pasi Spain ndodhet ne fund te string



Setet
[arn]	Sjell mnje liste ku njera nga karakteret eshte perputhur	
[a-n]	Sjell rasastet kur kushti eshte perputhur, shkronjat e vogla nga a ne n	
[^arn]	Sjell te gjitha rastet kur a,r dhe n nuk jane perdorur	
[0123]	Sjell te gjitha rastet kur 0,1,2,3 eshte perdorur
[0-9]	Sjell te gjitha rastet kur jane perdorur numra nga 0-9	
[0-5][0-9]	Pret te gjithe numra 2shifror nga 00 ne 59	
[0-9][0-9][0-9]
[a-zA-Z]	Pret te gjithe shkronjat te vogla ose te medha nga a ne z	
[A-Z]
[+]	Ne sete, +, *, ., |, (), $,{} nuk kan ndonje kuptim special, [+] Pret qe te perdoret simboli i +
"""


import re # ose gjate regex, eshte libraria per regular expression
hand = open('./file/text.txt')
for line in hand:
    line = line.rstrip()
    # if re.search('[A-Za-z]', line):
    #     print(line)
    if re.findall('[^lorem]', line):
         print(line)
    #if re.search('[0-9]',line):
    #   print(line)
hand.close()

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#valido nje email
def check(email):
    if(re.fullmatch(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")

 

email = "adii2@gmail.com"
check(email)

email = "visi9_+@G02-.doc"
check(email)

email = "my.ownsite@our-earth.org"
check(email)

email = "adii326.com"
check(email)


# Kontrollo ZIP code
words_pattern = "^[0-9]{5}(?:-[0-9]{4})?$"
print(re.match(words_pattern, '80001')) # Printon Match object
print(re.match(words_pattern, '80001-2222')) # Printon Match object
print(re.match(words_pattern, '800010')) # Printon None

"""
# The regular expression below cheks that a password:

# Minimumi 8 karaktere {8,}
# Te pakten nje shkronje te madhe.(?=.*?[A-Z])
# Te pakten nje shkronje te vogel (?=.*?[a-z])
# Te pakten nje numer (?=.*?[0-9])
# Te pakten nje simbol(?=.*?[#?!@$%^&*-])
# "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
"""

password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
x= re.match(password_pattern, 'secret') # Printon None
print(x)
y= re.match(password_pattern, '-Secr3t.') # Printon Match object
print(y)


