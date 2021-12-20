"""
the hard part is the dictionary with all the language details
maybe I dont have all the dict perfect, I take the words from diferents webpages
"""
from datetime import date

dict = { 
    'CA': {0: 'dilluns',1: 'dimarts', 2:'dimecres',3: 'dijous',4: 'divendres',5: 'dissabte',6: 'diumenge'},		
    'CZ': {0: 'pondělí',1: 'úterý', 2:'středa',3: 'čtvrtek',4: 'pátek',5: 'sobota',6: 'neděle'},								
    'DE': {0: 'montag',1: 'dienstag', 2:'mittwoch',3: 'donnerstag',4: 'freitag',5: 'samstag',6: 'sonntag'},		
    'DK': {0: 'mandag',1: 'tirsdag', 2:'onsdag',3: 'torsdag',4: 'fredag',5: 'lørdag',6: 'søndag'},								
    'EN': {0: 'monday',1: 'tuesday', 2:'wednesday',3: 'thursday',4: 'friday',5: 'saturday',6: 'sunday'},
    'ES': {0: 'lunes',1: 'martes', 2:'miércoles',3: 'jueves',4: 'viernes',5: 'sábado',6: 'domingo'},
    'FI': {0: 'maanantai',1: 'tiistai', 2:'keskiviikko',3: 'torstai',4: 'perjantai',5: 'lauantai',6: 'sunnuntai'},		
    'FR': {0: 'lundi',1: 'mardi', 2:'mercredi',3: 'jeudi',4: 'vendredi',5: 'samedi',6: 'dimanche'},		
    'IS': {0: 'mánudagur',1: 'þriðjudagur', 2:'miðvikudagur',3: 'fimmtudagur',4: 'föstudagur',5: 'laugardagur',6: 'sunnudagur'},		
    'GR': {0: 'δευτέρα',1: 'τρίτη', 2:'τετάρτη',3: 'πέμπτη',4: 'παρασκευή',5: 'σάββατο',6: 'κυριακή'},		
    'HU': {0: 'hétfő',1: 'kedd', 2:'szerda',3: 'csütörtök',4: 'péntek',5: 'szombat',6: 'vasárnap'},		
    'IT': {0: 'lunedì',1: 'martedì', 2:'mercoledì',3: 'giovedì',4: 'venerdì',5: 'sabato',6: 'domenica'},		
    'NL': {0: 'maandag',1: 'dinsdag', 2:'woensdag',3: 'donderdag',4: 'vrijdag',5: 'zaterdag',6: 'zondag'},		
    'VI': {0: 'thứ hai',1: 'thứ ba', 2:'thứ tư',3: 'thứ năm',4: 'thứ sáu',5: 'thứ bảy',6: 'chủ nhật'},		
    'PL': {0: 'poniedziałek',1: 'wtorek', 2:'środa',3: 'czwartek',4: 'piątek',5: 'sobota',6: 'niedziela'},		
    'RO': {0: 'luni',1: 'marţi', 2:'miercuri',3: 'joi',4: 'vineri',5: 'sâmbătă',6: 'duminică'},		
    'RU': {0: "понедельник",1: 'вторник', 2:'среда',3: 'четверг',4: 'пятница',5: 'суббота',6: "воскресенье"},		
    'SE': {0: 'måndag',1: 'tisdag', 2:'onsdag',3: 'torsdag',4: 'fredag',5: 'lördag',6: 'söndag'},		
    'SI': {0: 'ponedeljek',1: 'torek', 2:'sreda',3: 'četrtek',4: 'petek',5: 'sobota',6: 'nedelja'},		
    'SK': {0: 'pondelok',1: 'utorok', 2:'streda',3: 'štvrtok',4: 'piatok',5: 'sobota',6: "nedeľa"},		
}

def challenge6(input):
    f = open("submitOutput.txt", "w")
    cases = int(input.readline())
    i=1
    while i<=cases:
        line = input.readline().replace('\n','').split(':')
        fecha = line[0].split('-')
        if len(fecha[0])==2:
            aux = fecha[0]
            fecha[0]=fecha[2]
            fecha[2]=aux
        try:
            day_week=date(int(fecha[0]),int(fecha[1]),int(fecha[2])).weekday()
            try:
                print('Case #{}: {}'.format(i,dict[line[1]][day_week]))
                f.write('Case #{}: {}\n'.format(i,dict[line[1]][day_week]))
            except:
                print('Case #{}: {}'.format(i,'INVALID_LANGUAGE'))
                f.write('Case #{}: {}\n'.format(i,'INVALID_LANGUAGE'))
        except:
            print('Case #{}: {}'.format(i,'INVALID_DATE'))
            f.write('Case #{}: {}\n'.format(i,'INVALID_DATE'))
        i+=1
    f.close()

# input = open('miInput.txt', 'r')
# input = open('sampleInput.txt', 'r')
# input = open('testInput.txt', 'r')
input = open('submitInput.txt', 'r')
challenge6(input)
input.close()


