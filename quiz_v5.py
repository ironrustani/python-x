def pyetje_me_alternativa(
        pyetja_nr1,
        alternativat_nr1,
        pergjigja_nr1,
        pyetja_nr2,
        alternativat_nr2,
        pergjigja_nr2,
        pyetja_nr3,
        alternativat_nr3,
        pergjigja_nr3,
        pyetja_nr4,
        alternativat_nr4,
        pergjigja_nr4,
        pyetja_nr5,
        alternativat_nr5,
        pergjigja_nr5,
        piket
        ):
    print(pyetja_nr1,'?')
    print(alternativat_nr1)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr1.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr1}\n')
        piket = piket
    print(pyetja_nr2,'?')
    print(alternativat_nr2)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr2.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr2}\n')
        piket = piket
    print(pyetja_nr3,'?')
    print(alternativat_nr3)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr3.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr3}\n') 
        piket = piket
    print(pyetja_nr4,'?')
    print(alternativat_nr4)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr4.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr4}\n')
        piket = piket
    print(pyetja_nr5,'?')
    print(alternativat_nr5)
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr5.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr5}')
        piket = piket
    print(f'Piket e juaja jane:  {piket}')

def pyetje_pergjigje(       
        pyetja_nr1,
        pergjigja_nr1,
        pyetja_nr2,
        pergjigja_nr2,
        pyetja_nr3,
        pergjigja_nr3,
        pyetja_nr4,
        pergjigja_nr4,
        pyetja_nr5,
        pergjigja_nr5,
        piket
        ):
    print(pyetja_nr1,'?')
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr1.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr1}\n')
        piket = piket
    print(pyetja_nr2,'?')
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr2.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr2}\n')
        piket = piket
    print(pyetja_nr3,'?')
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr3.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr3}\n') 
        piket = piket
    print(pyetja_nr4,'?')
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr4.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr4}\n')
        piket = piket
    print(pyetja_nr5,'?')
    pergjigja_e_userit = input('Shkruaj pergjigjen: ')
    if pergjigja_e_userit.lower() == pergjigja_nr5.lower():
        print('Pergjigje e Sakte\n')
        piket +=1
    else:
        print('Pergjigje e Gabuar')
        print(f'Pergjigja e sakte: {pergjigja_nr1}')
        piket = piket
    print(f'Piket e juaja jane:  {piket}')


def quiz():
    user_input = input('Ju lutemi shkruani kategorine: ') 
    match user_input.lower():
        case 'histori':
            pyetje_me_alternativa(
                'Sa kontinente ka toka',
                '6\n3\n9\n7',
                '7',
                'Cili eshte shteti me popullsine me te madhe',
                'Amerika\nKina\nRusia\nIndia',
                'Kina',
                'Cili eshte qyteti europian me popullsin me te madhe',
                'Stambolli\nParisi\nMilano\nAmsterdami',
                'Stambolli',
                'A eshte rusia ne veto',
                'Po\nJo',
                'Jo',
                'A ndodhet Shqiperia ne kontinetin e Amerikes se veriut',
                'Po\nJo',
                'Jo',
                0
                )
        case 'sport':
            pyetje_me_alternativa(
                'Sa champios league ka fituar Milan',
                '5\n4\n7\n11',
                '7',
                'Kush eshte klubi me i vjeter ne historine e futbollit',
                'Real Madrid\nBodo Glimt\nMilan\nShefilld',
                'Shefilld',
                'Cili shtet ka fituar me se shumti boterorin',
                'Brazili\nItali\nGjermani\nArgjentina',
                'Brazili',
                'Kush eshte klubi qe ka fituar me shume Champions League',
                'Milan\nReal Madrid\nBayern Munchen\nLuftetari Gjirokastres',
                'Real Madrid',
                'Kush ishte fituasi i Superliges Shqiptare sezoni 2021-2022',
                'Partizani\nTirana\nKukesi\nVllaznia',
                'Tirana',
                0
                )
        case 'gjeografi':
            pyetje_pergjigje(
                'Cili eshte kryeqyteti i turqise',
                'Ankara'
                'Cili eshte shteti qe ze siperfaqen me te madhe gjeometrike',
                'Rusia',
                'Ne cilin kontinet ndodhet Turqia',
                'Aziatik',
                'Cili eshte eshte oqeani me i madh ne bote',
                'Oqeani Paqesor',
                'Me sa shtete kofizohet Shqiperia',
                '4',
                0
                )
            
print('Ky eshte nje quiz i gjeneruar nga Python Suksese!')
quiz()

while True:
    user_input = input('\nDeshironi te vazhdoni?\nShtypni: Po per te vazhduar.\nShtypni: Jo per te dale.\n')
    if user_input.lower() == 'po':
        quiz()
    else:
        print('Suksese ne quzin e radhes.')
        break
