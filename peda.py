#Python3

import csv
import math
import glob
import numpy as np


def getExeNames(titles):
    ti = []
    for title in titles[1:]:
        ti.append(title)
    return ti


def getRow(row):
    r = [row[0]]

    points = []
    for i,p in enumerate( row[1:] ):
        #Convert the numbers separated by space into a array of integers
        #Fetch the max value of and return those.
        #print( p )
        #print( [('A'+i+'B') for i in p.strip().replace(u'\xa0',u' ').split(' ')] )
        #print( [('A'+i.replace(u'\xa0', u' ')+'B') for i in p.strip().split(' ')] )
        #print( [int('0'+i) for i in p.strip().split(' ')] )
        values = [int('0'+i) for i in p.strip().replace(u'\xa0', u' ').split(' ')]
        #print( values );
        r.append( max( values ))

    return r

def removeFieldName(a, name):
    #https://stackoverflow.com/questions/15575878/how-do-you-remove-a-column-from-a-structured-numpy-array
    names = list(a.dtype.names)
    if name in names:
        names.remove(name)
    b = a[names]
    return b


def leaveFields(a, ns):
    names = list(a.dtype.names)

    #Find the corresponding names of fields that stay
    fields = []
    for n in ns:
        res = [i for i in names if n in i]
        fields.append( res[0] )

    #Find the difference and drop those---except the one named "Name"
    #https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-19.php
    diff1 = list( set(names) - set(fields) )
    diff2 = list( set(fields) - set(names) )
    diff = diff1 + diff2
    diff.remove("Name")
    for n in diff:
        a = removeFieldName(a, n)

    return a

#
#
#
#
#

fil = []
tul = []
kpl = []

if (0):

    kpl.append( '1: Elävä solu ' )
    fil.append( 'bg7_1.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S1', 'T1','YT1'] )

    kpl.append( '4: Levät ja planktoneläimet ovat vesien runsaimpia eliöitä' )
    fil.append( 'bg7_4.csv'  )
    tul.append( ['P1'] )

    kpl.append( '5: Kasvit' )
    fil.append( 'bg7_5.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P04', 'S1'] )

    kpl.append( '6: Selkärangattomia eläimiä' )
    fil.append( 'bg7_6.csv'  )
    tul.append( ['P1', 'P2', '03', 'P4', 'P5', 'S1','S2'] )

    kpl.append( '7: Kiehtovat kalamme' )
    fil.append( 'bg7_7.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S2'] )

    kpl.append( '8: Sammakkolammella' )
    fil.append( 'bg7_8.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'YT1'] )

    kpl.append( '9: Matelijat menestyvät kuivalla maalla' )
    fil.append( 'bg7_9.csv'  )
    tul.append( ['P1', 'S1'] )

    kpl.append( '10: Linnut ovat sopeutuneet lentämään' )
    fil.append( 'bg7_10.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'S1'] )

    #kpl.append( '11: Nisäkkäät imettävät poikasiaan' )
    #fil.append( 'bg7_11.csv'  )
    #tul.append( ['P1', 'P2', 'S1'] )
    name = "Nanda"
    name = "Aada"
    name = "Jussi"
    name = "Lauri"
    name = "Emil"
    name = "Eemeli"
    name = "mimosa"
    name = "Tuomas"
    name = "Aleksandra"



if (0):

    kpl.append( '2: Karttatietoutta' )
    fil.append( 'ge7lk_2.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'S6'] )

    kpl.append( '3: Tähtitieteen perusteita' )
    fil.append( 'ge7lk_3.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'S5', 'S7', 'S8'] )

    kpl.append( '4: Vuorokausi, vuodenajat ja vuosi' )
    fil.append( 'ge7lk_4.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'S5', 'S6'] )

    kpl.append( '5: Valtameret erottavat manteireita ja maanosia' )
    fil.append( 'ge7lk_5.csv'  )
    tul.append( ['P1', 'P2', 'S3', 'S4', 'S5'] )

    kpl.append( '6: Levoton maankuori' )
    fil.append( 'ge7lk_6.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'S5', 'S6', 'S7', 'S8', 'S9'])

    kpl.append( '7: Vuoristot ovat syntyneet miljoonia vuosia sitten' )
    fil.append( 'ge7lk_7.csv'  )
    tul.append( ['P1', 'P2', 'S3'] )

    kpl.append( '8: Miten vesi, jää ja tuuli kuluttavat kalliota' )
    fil.append( 'ge7lk_8.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4'] )

    kpl.append( '9: Miksi kallio hajoaa ja maa vyöryy' )
    fil.append( 'ge7lk_9.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4'] )

    kpl.append( '10: Maapallon ilmastot' )
    fil.append( 'ge7lk_10.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'S5'] )

    kpl.append( '11: Kasvillisuusalueet' )
    fil.append( 'ge7lk_11.csv'  )
    tul.append( ['P1', 'P2', 'P3'] )

    kpl.append( '12: Sää' )
    fil.append( 'ge7lk_12.csv'  )
    tul.append( ['P1', 'P2', 'P3'] )

    kpl.append( '13: Ilmasto muuttuu' )
    fil.append( 'ge7lk_13.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'S5', 'S6'] )

    kpl.append( '14: Luontoa pitää suojella' )
    fil.append( 'ge7lk_14.csv'  )
    tul.append( ['P1', 'P2', 'S3', 'S4'] )


    name = "carmen"
    #name = "saimi"
    #name = "joel"
    #name = "leino"
    #name = "lily"
    #name = "max"
    #name = "mette"
    #name = "oda"
    #name = "eelis"

if (1):

    kpl.append( '3: Metsätyypit ja puulajit' )
    fil.append( 'bg8_3.csv'  )
    tul.append( ['P1', 'P2'] )

    kpl.append( '4: Sienet luovat metsän perustan' )
    fil.append( 'bg8_4.csv'  )
    tul.append( ['P1', 'S10', 'S1', 'S3', 'S4', 'S5'] )

    kpl.append( '5: Kasvien rakenne ja merkitys' )
    fil.append( 'bg8_5.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S1', 'T2'] )

    kpl.append( '6: Metsien kasveja' )
    fil.append( 'bg8_6.csv'  )
    tul.append( ['P1', 'P2'] )

    kpl.append( '7: Metsän selkärangattomia eläimiä' )
    fil.append( 'bg8_7.csv'  )
    tul.append( ['P1', 'P2'] )

    #kpl.append( '9: Metsän vuodenajat' )
    #fil.append( 'bg8_9.csv'  )
    #tul.append( ['P1', 'P2', 'P3', 'S1'] )


    name = "Carmen"
    name = "Saimi"
    name = "Joel"
    name = "Leino"
    name = "lily"
    name = "max"
    name = "lotta"
    #name = "jonatan"






if (0):

    kpl.append( '3: Maapallon on asutettu epätasaisesti ' )
    fil.append( 'ge8lk_3.csv'  )
    tul.append( ['P1', 'P2', 'S3', 'S4'] )

    kpl.append( '4: Väestönkasvu' )
    fil.append( 'ge8lk_4.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'S5'] )

    kpl.append( '5: Ihmiset muuttavat' )
    fil.append( 'ge8lk_5.csv'  )
    tul.append( ['P1', 'P2', 'S3', 'S4', 'S5'] )

    kpl.append( '6: Kaupungistuminen' )
    fil.append( 'ge8lk_6.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'YT5'] )

    kpl.append( '7: Ravinnontuotanto' )
    fil.append( 'ge8lk_7.csv'  )
    tul.append( ['P1', 'P2', 'S3', 'S4', 'YT4'] )

    kpl.append( '8: Luonnonvarat ovat talouden perusta' )
    fil.append( 'ge8lk_8.csv'  )
    tul.append( ['P2', 'S4', 'S5'] )

    kpl.append( '9: Maailma tarvitsee energiaa' )
    fil.append( 'ge8lk_9.csv'  )
    tul.append( ['P1', 'S2'] )

    kpl.append( '10: Teollisuusalueet' )
    fil.append( 'ge8lk_10.csv'  )
    tul.append( ['P1', 'S2', 'S3'] )

    kpl.append( '11: EU' )
    fil.append( 'ge8lk_11.csv'  )
    tul.append( ['P1', 'P2', 'P3'] )

    kpl.append( '12: Liikenne' )
    fil.append( 'ge8lk_12.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'S5', 'S6'] )

    kpl.append( '13: Matkailu' )
    fil.append( 'ge8lk_13.csv'  )
    tul.append( ['P1', 'P2', 'S3', 'S4', 'S5'] )

    kpl.append( '14: Reilumpaan maailmaan' )
    fil.append( 'ge8lk_14.csv'  )
    tul.append( ['P1', 'S2', 'S3', 'S4', 'S5'] )

    kpl.append( '29: Afrikan karttatietoutta' )
    fil.append( 'ge8lk_29.csv'  )
    tul.append( ['P1', 'S3'] )

    kpl.append( '30: Afrikan valtioita' )
    fil.append( 'ge8lk_30.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'P6'] )

    kpl.append( '31: Aasia on suuri maanosa' )
    fil.append( 'ge8lk_31.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'P5'] )

    kpl.append( '32: Aasian erilaiset valtiot' )
    fil.append( 'ge8lk_32.csv'  )
    tul.append( ['P1', 'P2'] )

    kpl.append( '33: Intia' )
    fil.append( 'ge8lk_33.csv'  )
    tul.append( ['P1', 'S2', 'S3', 'S4', 'S5'] )

    kpl.append( '34: Kiina' )
    fil.append( 'ge8lk_34.csv'  )
    tul.append( ['P1', 'P2', 'S3', 'S4'] )

    kpl.append( '35: Japani' )
    fil.append( 'ge8lk_35.csv'  )
    tul.append( ['P1', 'S2'] )



    kpl.append( '36: Kanada' )
    fil.append( 'ge8lk_36.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'S10', 'S7', 'S8', 'S9'] )

    kpl.append( '38: Meksiko' )
    fil.append( 'ge8lk_38.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'P5', 'P6'] )


    name = "elin"
    name = "wiliam"
    name = "gin"
    name = "nestori"
    name = "lotta"
    name = "hilla"
    #name = "milla"
    name = "jonatan"



if (0):
    #9. luokka
    kpl.append( '2: Solut -- elämän legopalikat' )
    fil.append( 'bg9_2.csv'  )
    tul.append( ['P1', 'P2', 'S3'] )

    kpl.append( '3: Kudokset' )
    fil.append( 'bg9_3.csv'  )
    tul.append( ['P1'] )

    kpl.append( '4: Luusto' )
    fil.append( 'bg9_4.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'P5', 'S7'] )

    kpl.append( '5: Lihakset' )
    fil.append( 'bg9_5.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'S5', 'Essee'] )

    kpl.append( '6: Ruuansulatus' )
    fil.append( 'bg9_6.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'Essee', 'S6', 'T1'] )

    kpl.append( '7: Hengitys' )
    fil.append( 'bg9_7.csv'  )
    tul.append( ['P1', 'S2', 'S4', 'T5'] )

    kpl.append( '8: Veri' )
    fil.append( 'bg9_8.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'P5', 'S6', 'S7', 'S9'] )

    kpl.append( '9: Sydän ja verenkierto' )
    fil.append( 'bg9_9.csv'  )
    tul.append( ['P1', 'P2', 'S4', 'S5'] )

    kpl.append( '10: Maksa ja munuaiset' )
    fil.append( 'bg9_10.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4'] )

    #kpl.append( '11: Umpirauhaset' )
    #fil.append( 'bg9_11.csv'  )
    #tul.append( ['P1', 'P2'] )

    kpl.append( '12: Hermosolu' )
    fil.append( 'bg9_12.csv'  )
    tul.append( ['P1', 'P2', 'S4', 'S5', 'S7'] )

    kpl.append( '13: Aivot ja hermosto' )
    fil.append( 'bg9_13.csv'  )
    tul.append( ['P1', 'P2', 'S3', 'S4', 'S5'] )

    kpl.append( '14: Näkökyky' )
    fil.append( 'bg9_14.csv'  )
    tul.append( ['P1', 'P2', 'S3', 'S4', 'S5', 'T7', 'T8'] )

    kpl.append( '15: Kuulo' )
    fil.append( 'bg9_15.csv'  )
    tul.append( ['P1', 'S2', 'S3', 'S7'] )

    kpl.append( '17: Kuulo' )
    fil.append( 'bg9_17.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'P4', 'S5', 'S6', 'S7'] )
    name = "ss"
    name = "sophie"
    name = "mell"
    name = "katariina"
    name = "andreas"
    #name = "anton"

if (0):
    #9. luokka
    kpl.append( '2: Kivilajit kalliossa' )
    fil.append( 'ge9_2.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S5'] )

    kpl.append( '3: Jääkausi' )
    fil.append( 'ge9_3.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4', 'S5'] )

    kpl.append( '4: Maaperä ja maankohoaminen' )
    fil.append( 'ge9_4.csv'  )
    tul.append( ['P1', 'P2', 'S3'] )

    kpl.append( '5: Muuttuva luonto')
    fil.append( 'ge9_5.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'YT5'] )

    kpl.append( '6: Metsät')
    fil.append( 'ge9_6.csv'  )
    tul.append( ['P1', 'P2', 'P3', 'S4'] )

    kpl.append( '7: Suot')
    fil.append( 'ge9_7.csv'  )
    tul.append( ['P1', 'P2', 'S3'] )

    #kpl.append( '8: Ilmasto')
    #fil.append( 'ge9_8.csv'  )
    #tul.append( ['P1', 'P2', 'P3', 'S4', 'S5'] )

    #kpl.append( '9: Sää')
    #fil.append( 'ge9lk_9.csv'  )
    #tul.append( ['P1', 'S2', 'S3', 'S4'] )

    #kpl.append( '10: Kartat')
    ##fil.append( 'ge9lk_10.csv'  )
    #tul.append( ['P1', 'S2', 'S3'] )

    #kpl.append( '11: Suomen maisema-alueet')
    #fil.append( 'ge9lk_11.csv'  )
    #tul.append( ['P1', 'S2'] )

    #kpl.append( '12: Itämeri')
    #fil.append( 'ge9lk_12.csv'  )
    #tul.append( ['P1', 'P2', 'P3', 'P4', 'S5'] )

    #kpl.append( '13: Suomen järvet ja joet')
    #fil.append( 'ge9lk_13.csv'  )
    #tul.append( ['P1', 'P2', 'S3', 'S4'] )

    #kpl.append( '14: Väestö' )
    #fil.append( 'ge9lk_14.csv'  )
    #tul.append( ['P1', 'P2', 'P3', 'S4', 'YT5'] )

    #kpl.append( '15: Kaavoitus' )
    #fil.append( 'ge9lk_15.csv'  )
    #tul.append( ['P1', 'S2', 'S5'] )




    name = "Trei"
    name = "Wiliam"
    name = "Gin"
    name = "Marken"
    name = "Nestori"
    name = "Hilla"
    name = "Jonatan"

#
#
#
ka = 0
lkm = 0 
print("\n\n")
print('Hei')
print('Biologian tehtäväsi tähän mennessä. Lopussa arvosana seisoo, mutta huomaa että voi huonontuakin tästä, jos luokkasi on tehnyt laiskasti tehtäviä.')
print('Tarkista ainakin, että olet teet ne tehtävät mitkä olen merkinnyt arvosanalla neljä (4). Jos olet tehnyt, mutta arvosanasi on 4, kerro minulle. ')
print('Saat parannella ja lisäillä tehtäviä, jos haluat paremman numeron. Aikaa on pari viikkoa.')
print('- - - - - - - - - - - - - - - - - - - - -')
ave = 0 
for i, tcsv in enumerate( fil ):
    lkm = lkm + 1
    names = []
    with open( tcsv ) as csvfile:
        print( kpl[i] )
        print( "-"*len( kpl[i] ) )
        readCSV = csv.reader(csvfile, delimiter=',')
        #Read the column names
        eNames = getExeNames(next(readCSV)) 
        eNames.insert(0,'Name')
        formats = ['u4']*( len( eNames ) - 1)
        formats.insert(0, 'U30')
        #print( eNames )

        # Create the array
        rr = [];
        for row in readCSV:
            r = getRow( row )
            rr.append( tuple(r) )
        points = np.array( (rr),  dtype={'names': eNames, 'formats':formats})
        #print( points )

        #Create the grading table.
        formatsGrade = ['f4']*( len( eNames ) - 1)
        formatsGrade.insert(0, 'U30')
        grades = np.array( (rr),  dtype={'names': eNames, 'formats':formatsGrade})
        #print( grades ) 
        #print( eNames )
        #print( len( eNames ) )
        for n in eNames[1:]:
            #print( grades[n] )
            grades[n] = grades[n]/ max( max( grades[n] ), 1 )
            grades[n] = np.maximum( np.round( ( 4*( 6/(1-0.1)*(grades[n]-1)+10 ))/4, 2), 4)
        #print( grades )
        

        #Get the needed columns (exercises) only
        grades = leaveFields(grades, tul[i])
        #print( grades.dtype.names[1:] ) 
        #print( grades ) 


        if 1:
            names = grades['Name'] 
            nameInd = [j for j,i in enumerate(names) if name.lower() in i.lower()]
            average = 4
            if nameInd:
                nameInd = nameInd[0]
                pp = list( grades[nameInd] )
                print( pp[0] )
                for ni, n in enumerate( grades.dtype.names[1:] ):
                    print( "Arvosana: " + str(pp[ni+1]) , end="\t" )
                    print(n)
                average = np.round( np.average( pp[1:] ), 1) 
            else:
                print("Et ole tehnyt yhtään tehtävää tästä luvusta! Tee vielä:")
                for ni, n in enumerate( grades.dtype.names[1:] ):
                    print(n)

            print( "-> Keskiarvo: " + str( average ) )
            ave = ave + average

        print("\n")
print('---------------')
print( 'Kaikkien tehtävien keskiarvo: ', np.round( ave/lkm, 1) )
print("\n\n")
