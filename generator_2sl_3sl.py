#!/usr/bin/env python
# -*- coding: utf-8 -*-

##zamjenjuje naglašene samoglasnike (i slogotvorno 'r') iz oblika preuzetih iz baze s nenaglašenim samoglasnicima
## ngos=nenaglašena glagolska osnova
def nenag_sam(gos):
    ngos=''
    for bs in gos:
        if bs in u'àȁáâāèȅéêēìȉíîīòȍóôōùȕúûūŗȑŕȓř':
            if bs in u'àȁáâā':
                ngos+='a'
            elif bs in u'èȅéêē':
                ngos+='e'
            elif bs in u'ìȉíîī':
                ngos+='i'
            elif bs in u'òȍóôō':
                ngos+='o'
            elif bs in u'ùȕúûū':
                ngos+='u'
            elif bs in u'ŗȑŕȓř':
                ngos+='r'
        else:
            ngos+=bs
    return ngos

##funkcija za brojanje slogova (uključuje i slogotvorno 'r')
def slog(infs):
    si=0
    infs=nenag_sam(infs)
    sams='aeiou'
    rs='r'
    for ai in range(len(infs)):
        if infs[ai] in sams:
            si+=1
        if infs[ai] in rs and infs[ai-1] not in sams and infs[ai+1] not in sams:
            si+=1
        elif infs[ai] in 'r' and ai==0 and infs[ai+1] not in sams:
            si+=1
    if infs.find('ije') != -1:
       si-=1
    return si

#pronalazi redni broj sloga na kojem se nalazi naglasak u 1.l.jd. prezenta
def slog_prez(pres):
    ai=1
    bi=0
    sam=u'aeiouāēīōūȁȅȉȍȕâêîôûàèìòùáéíóú'
    if pres.find(u'à') != -1:
        bi=string.find(pres,u'à')
    elif pres.find(u'è') != -1:
        bi=string.find(pres,u'è')
    elif pres.find(u'ì') != -1:
        bi=string.find(pres,u'ì')
    elif pres.find(u'ò') != -1:
        bi=string.find(pres,u'ò')
    elif pres.find(u'ù') != -1:
        bi=string.find(pres,u'ù')
    elif pres.find(u'ř') != -1:
        bi=string.find(pres,u'ř')
    elif pres.find(u'á') != -1:
        bi=string.find(pres,u'á')
    elif pres.find(u'é') != -1:
        bi=string.find(pres,u'é')
    elif pres.find(u'í') != -1:
        bi=string.find(pres,u'í')
    elif pres.find(u'ó') != -1:
        bi=string.find(pres,u'ó')
    elif pres.find(u'ú') != -1:
        bi=string.find(pres,u'ú')
    elif pres.find(u'ŕ') != -1:
        bi=string.find(pres,u'ŕ')
    elif pres.find(u'ȁ') != -1:
        bi=string.find(pres,u'ȁ')
    elif pres.find(u'ȅ') != -1:
        bi=string.find(pres,u'ȅ')
    elif pres.find(u'ȉ') != -1:
        bi=string.find(pres,u'ȉ')
    elif pres.find(u'ȍ') != -1:
        bi=string.find(pres,u'ȍ')
    elif pres.find(u'ȕ') != -1:
        bi=string.find(pres,u'ȕ')
    elif pres.find(u'ȑ') != -1:
        bi=string.find(pres,u'ȑ')
    elif pres.find(u'â') != -1:
        bi=string.find(pres,u'â')
    elif pres.find(u'ê') != -1:
        bi=string.find(pres,u'ê')
    elif pres.find(u'î') != -1:
        bi=string.find(pres,u'î')
    elif pres.find(u'ô') != -1:
        bi=string.find(pres,u'ô')
    elif pres.find(u'û') != -1:
        bi=string.find(pres,u'û')
    elif pres.find(u'ȓ') != -1:
        bi=string.find(pres,u'ȓ')
    for ci in range(len(pres[:bi])):
        if pres[ci] in u'aieouāēīōū':
            ai+=1
        if pres[ci] in 'r' and pres[ci-1] not in sam and pres[ci+1] not in sam:
            ai+=1
        if pres.find('ije') != -1:
             ai-=1
    return ai

## mijenja iz bilo kojeg naglaska u dugosilazni
def dugosilazni(cs,gos2):
    if cs in u'àáȁ':
        gos3=gos2.replace(cs,u'â')
    elif cs in u'èéȅ':
        gos3=gos2.replace(cs,u'ê')
    elif cs in u'ìíȉ':
        gos3=gos2.replace(cs,u'î')
    elif cs in u'òóȍ':
        gos3=gos2.replace(cs,u'ô')
    elif cs in u'ùúȕ':
        gos3=gos2.replace(cs,u'û')
    elif cs in u'ŗŕȑ':
        gos3=gos2.replace(cs,u'ȓ')
    return gos3

## mijenja iz bilo kojeg naglaska u dugouzlazni
def dugouzlazni(cs,gos2):
    if cs in u'ȁàâ':
        gos3=gos2.replace(cs,u'á')
    elif cs in u'ȅèê':
        gos3=gos2.replace(cs,u'é')
    elif cs in u'ȉìî':
        gos3=gos2.replace(cs,u'í')
    elif cs in u'ȍòô':
        gos3=gos2.replace(cs,u'ó')
    elif cs in u'ȕùû':
        gos3=gos2.replace(cs,u'ú')
    elif cs in u'ȑŗȓ':
        gos3=gos2.replace(cs,u'ŕ')
    return gos3

## mijenja iz bilo kojeg naglaska u kratkosilazni 
def kratkosilazni(cs,gos2):
    if cs in u'àáâ':
        gos3=gos2.replace(cs,u'ȁ')
    elif cs in u'èéê':
        gos3=gos2.replace(cs,u'ȅ')
    elif cs in u'ìíî':
        gos3=gos2.replace(cs,u'ȉ')
    elif cs in u'òóô':
        gos3=gos2.replace(cs,u'ȍ')
    elif cs in u'ùúû':
        gos3=gos2.replace(cs,u'ȕ')
    elif cs in u'ŗŕȓ':
        gos3=gos2.replace(cs,u'ȑ')
    return gos3

## mijenja iz bilo kojeg naglaska u kratkouzlazni 
def kratkouzlazni(cs,gos2):
    if cs in u'ȁáâ':
        gos3=gos2.replace(cs,u'à')
    elif cs in u'ȅéê':
        gos3=gos2.replace(cs,u'è')
    elif cs in u'ȉíî':
        gos3=gos2.replace(cs,u'ì')
    elif cs in u'ȍóô':
        gos3=gos2.replace(cs,u'ò')
    elif cs in u'ȕúû':
        gos3=gos2.replace(cs,u'ù')
    elif cs in u'ȑŕȓ':
        gos3=gos2.replace(cs,u'ŗ')
    return gos3

## stavlja dugouzlazni naglasak
def dugouzlazni1(bs):
    if bs in 'a':
        bs=u'á'
    elif bs in 'e':
        bs=u'é'
    elif bs in 'i':
        bs=u'í'
    elif bs in 'o':
        bs=u'ó'
    elif bs in 'u':
        bs=u'ú'
    elif bs in 'r':
        bs=u'ŕ'
    return bs

## stavlja kratkouzlazni naglasak
def kratkouzlazni1(bs):
    if bs in 'a':
        bs=u'à'
    elif bs in 'e':
        bs=u'è'
    elif bs in 'i':
        bs=u'ì'
    elif bs in 'o':
        bs=u'ò'
    elif bs in 'u':
        bs=u'ù'
    elif bs in 'r':
        bs=u'ŗ'
    return bs

## stavlja dugosilazni naglasak
def dugosilazni1(bs):
    if bs in 'a':
        bs=u'â'
    elif bs in 'e':
        bs=u'ê'
    elif bs in 'i':
        bs=u'î'
    elif bs in 'o':
        bs=u'ô'
    elif bs in 'u':
        bs=u'û'
    elif bs in 'r':
        bs=u'ȓ'
    return bs

## stavlja kratkosilazni naglasak
def kratkosilazni1(bs):
    if bs in 'a':
        bs=u'ȁ'
    elif bs in 'e':
        bs=u'ȅ'
    elif bs in 'i':
        bs=u'ȉ'
    elif bs in 'o':
        bs=u'ȍ'
    elif bs in 'u':
        bs=u'ȕ'
    elif bs in 'r':
        bs=u'ȑ'
    return bs

def slog1(gos,naglasak):
    ai=0
    for i in range(len(gos)-1):
        if gos[i] in u'aieouāēīōū':
            ai+=1
        if gos[i] in 'r' and gos[i-1] not in u'aieouāēīōū' and gos[i+1] not in u'aieouāēīōū':
            ai+=1       
        if ai==1:
            gos2=gos[:i]+naglasak(gos[i])+gos[i+1:]  
            return gos2

def slog2(gos,naglasak):
    ai=0
    for i in range(len(gos)-1):
        if gos[i] in u'aieouāēīōū':
            ai+=1
        if gos[i] in 'r' and gos[i-1] not in u'aieouāēīōū' and gos[i+1] not in u'aieouāēīōū':
            ai+=1
        if ai==2:
            gos2=gos[:i]+naglasak(gos[i])+gos[i+1:]  
            return gos2

def slog3(gos,naglasak):
    ai=0
    for i in range(len(gos)-1):
        if gos[i] in u'aieouāēīōū':
            ai+=1
        if gos[i] in 'r' and gos[i-1] not in u'aieouāēīōū' and gos[i+1] not in u'aieouāēīōū':
            ai+=1       
        if ai==3:
            gos2=gos[:i]+naglasak(gos[i])+gos[i+1:]  
            return gos2

def slog2unazad(gos,naglasak):
    ai=0
    if gos.find('ije') != -1:
        ai-=1
    for i in range(len(gos)-1,-1,-1):
        if gos[i] in u'aieouāēīōū':
            ai+=1
        elif gos[i] in 'r' and gos[i-1] not in u'aieouāēīōū' and gos[i+1] not in u'aieouāēīōū':
            ai+=1
        elif gos[i] in 'r' and i==0 and gos[i+1] not in u'aieou':
            ai+=1
        if ai==2 and i!=0 and gos[i] in 'raeiou' and gos[i+1] not in u'aieou':
            gos2=gos[:i]+naglasak(gos[i])+gos[i+1:]
        elif ai==2 and i==0 and gos[i] in u'raieou' and gos[i+1] not in u'aieou':
            gos2=naglasak(gos[i])+gos[i+1:]
        elif ai==2 and i==0:
            gos2=gos
    return gos2    

def slog3unazad(gos,naglasak):
    ai=0
    if gos.find('ije') != -1:
        ai-=1
    for i in range(len(gos)-1,-1,-1):
        if gos[i] in u'aieouāēīōū':
            ai+=1
        elif gos[i] in 'r' and gos[i-1] not in u'aieouāēīōū' and gos[i+1] not in u'aieouāēīōū':
            ai+=1
        elif gos[i] in 'r' and i==0 and gos[i+1] not in u'aieou':
            ai+=1
        if ai==3 and i!=0 and gos[i] in 'raeiou' and gos[i+1] not in u'aieou':
            gos2=gos[:i]+naglasak(gos[i])+gos[i+1:]
        elif ai==3 and i==0 and gos[i] in u'raieou' and gos[i+1] not in u'aieou':
            gos2=naglasak(gos[i])+gos[i+1:]
        elif ai==3 and i==0:
            gos2=gos
    return gos2

def slog4unazad(gos,naglasak):
    ai=0
    if gos.find('ije') != -1:
        ai-=1
    for i in range(len(gos)-1,-1,-1):
        if gos[i] in u'aieouāēīōū':
            ai+=1
        elif gos[i] in 'r' and gos[i-1] not in u'aieouāēīōū' and gos[i+1] not in u'aieouāēīōū':
            ai+=1
        elif gos[i] in 'r' and i==0 and gos[i+1] not in u'aieou':
            ai+=1
        if ai==4 and i!=0 and gos[i] in 'raeiou' and gos[i+1] not in u'aieou':
            gos2=gos[:i]+naglasak(gos[i])+gos[i+1:]
        elif ai==4 and i==0 and gos[i] in u'raieou' and gos[i+1] not in u'aieou':
            gos2=naglasak(gos[i])+gos[i+1:]
        elif ai==4 and i==0:
            gos2=gos
    return gos2
            
def jotacija(gos):
    if gos[-1] in 's':
        gos3=gos[:-1]+u'š'
    elif gos[-1] in 'b':
        gos3=gos[:-1]+'blj'
    elif gos[-1] in 'l':
        gos3=gos[:-1]+'lj'
    elif gos[-1] in 'd':
        gos3=gos[:-1]+u'đ'
    elif gos[-1] in 't':
        gos3=gos[:-1]+u'ć'
    elif gos[-1] in 'g':
        gos3=gos[:-1]+u'ž'
    elif gos[-1] in 'k':
        gos3=gos[:-1]+u'č'
    elif gos[-1] in 'c':
        gos3=gos[:-1]+u'č'
    elif gos[-1] in 'h':
        gos3=gos[:-1]+u'š'
    elif gos[-1] in 'z':
        gos3=gos[:-1]+u'ž'
    elif gos[-1] in 'p':
        gos3=gos[:-1]+'plj'
    elif gos[-1] in 'm':
        gos3=gos[:-1]+'mlj'
    elif gos[-1] in 'v':
        gos3=gos[:-1]+'vlj'
    elif gos[-2:] in 'sk':
        gos3=gos[:-1]+u'št'
    else:
        gos3=gos
    return gos3

def krati(gos2):
    gos3=''
    for ai in range(len(gos2)):
        if gos2[ai] in 'i' and gos2[ai+1] in 'j' and gos2[ai+2] in u'eēȅèéê':
            gos3+=''
        else:
            gos3+=gos2[ai]
    return gos3

def palatalizacija(gos2):
    cs=gos2[-1]
    if cs in u'č':
        gos3=gos2[:-1]+'k'
    elif cs in u'ž':
        gos3=gos2[:-1]+'g'
    elif cs in u'š':
        gos3=gos2[:-1]+'h'
    return gos3

def palatalizacija2(gos2):
    cs=gos2[-1]
    if cs in 'k':
        gos3=gos2[:-1]+u'č'
    elif cs in 'g':
        gos3=gos2[:-1]+u'ž'
    elif cs in 'h':
        gos3=gos2[:-1]+u'š'
    else:
        gos3=gos2
    return gos3

def sibilarizacija(gos2):
    cs=gos2[-1]
    if cs in u'č':
        gos3=gos2[:-1]+'c'
    elif cs in u'ž':
        gos3=gos2[:-1]+'z'
    elif cs in u'š':
        gos3=gos2[:-1]+'s'
    return gos3

def sibilarizacija2(gos2):
    cs=gos2[-1]
    if cs in 'k':
        gos3=gos2[:-1]+'c'
    elif cs in 'g':
        gos3=gos2[:-1]+'z'
    elif cs in 'h':
        gos3=gos2[:-1]+'s'
    else:
        gos3=gos2
    return gos3

def d_pretvorba(gos2):
    cs=gos2[-1]
    if cs in 'd':
        gos3=gos2[:-1]+u'đ'
    else:
        gos3=gos2
    return gos3

def naglasak_r(gos2):
    for bs in gos2:
        if bs in 'r':
            gos3=gos2.replace(bs,u'ȓ')
    return gos3

def prezent1(gos2):
    pre1ljd=gos2+u'ēm'
    pre2ljd=gos2+u'ēš'
    pre3ljd=gos2+u'ē'
    pre1lmn=gos2+u'ēmo'
    pre2lmn=gos2+u'ēte'
    pre3lmn=gos2+u'ū'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+u'\t')
    af.write(pre2ljd+u'\t')
    af.write(pre3ljd+u'\t')
    af.write(pre1lmn+u'\t')
    af.write(pre2lmn+u'\t')
    af.write(pre3lmn+u'\t')

def prezent2(gos2,gos3):
    pre1ljd=gos2+u'ēm'
    pre2ljd=gos2+u'ēš'
    pre3ljd=gos2+u'ē'
    pre1lmn=gos2+u'ēmo'
    pre2lmn=gos2+u'ēte'
    pre3lmn=gos3+u'ū'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+'\t')
    af.write(pre2ljd+'\t')
    af.write(pre3ljd+'\t')
    af.write(pre1lmn+'\t')
    af.write(pre2lmn+'\t')
    af.write(pre3lmn+'\t')

def prezent3(gos2,gos3):
    pre1ljd=gos2+u'ēm'
    pre2ljd=gos2+u'ēš'
    pre3ljd=gos2+u'ē'
    pre1lmn=gos3+u'ēmo'
    pre2lmn=gos3+u'ēte'
    pre3lmn=gos2+u'ū'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+'\t')
    af.write(pre2ljd+'\t')
    af.write(pre3ljd+'\t')
    af.write(pre1lmn+'\t')
    af.write(pre2lmn+'\t')
    af.write(pre3lmn+'\t')

def prezent4(gos2):
    pre1ljd=gos2+u'êm'
    pre2ljd=gos2+u'êš'
    pre3ljd=gos2+u'ê'
    pre1lmn=gos2+u'êmo'
    pre2lmn=gos2+u'éte'
    pre3lmn=gos2+u'ú'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+'\t')
    af.write(pre2ljd+'\t')
    af.write(pre3ljd+'\t')
    af.write(pre1lmn+'\t')
    af.write(pre2lmn+'\t')
    af.write(pre3lmn+'\t')

def prezent5(gos2):
    pre1ljd=gos2+u'îm'
    pre2ljd=gos2+u'îš'
    pre3ljd=gos2+u'î'
    pre1lmn=gos2+u'îmo'
    pre2lmn=gos2+u'íte'
    pre3lmn=gos2+u'é'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+'\t')
    af.write(pre2ljd+'\t')
    af.write(pre3ljd+'\t')
    af.write(pre1lmn+'\t')
    af.write(pre2lmn+'\t')
    af.write(pre3lmn+'\t')

def prezent6(gos2):
    pre1ljd=gos2+u'êm'
    pre2ljd=gos2+u'êš'
    pre3ljd=gos2+u'ê'
    pre1lmn=gos2+u'émo'
    pre2lmn=gos2+u'éte'
    pre3lmn=gos2+u'û'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+'\t')
    af.write(pre2ljd+'\t')
    af.write(pre3ljd+'\t')
    af.write(pre1lmn+'\t')
    af.write(pre2lmn+'\t')
    af.write(pre3lmn+'\t')

def prezent7(gos2):
    pre1ljd=gos2+u'ēm'
    pre2ljd=gos2+u'ēš'
    pre3ljd=gos2+u'ē'
    pre1lmn=gos2+u'ēmo'
    pre2lmn=gos2+u'ēte'
    pre3lmn=gos2+u'ū'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+u'\t')
    af.write(pre2ljd+u'\t')
    af.write(pre3ljd+u'\t')
    af.write(pre1lmn+u'\t')
    af.write(pre2lmn+u'\t')
    af.write(pre3lmn+u'\t')

def prezent8(gos2):
    pre1ljd=gos2+u'īm'
    pre2ljd=gos2+u'īš'
    pre3ljd=gos2+u'ī'
    pre1lmn=gos2+u'īmo'
    pre2lmn=gos2+u'īte'
    pre3lmn=gos2+u'ū'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+'\t')
    af.write(pre2ljd+'\t')
    af.write(pre3ljd+'\t')
    af.write(pre1lmn+'\t')
    af.write(pre2lmn+'\t')
    af.write(pre3lmn+'\t')

def prezent9(gos2):
    pre1ljd=gos2+u'īm'
    pre2ljd=gos2+u'īš'
    pre3ljd=gos2+u'ī'
    pre1lmn=gos2+u'īmo'
    pre2lmn=gos2+u'īte'
    pre3lmn=gos2+u'ē'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+'\t')
    af.write(pre2ljd+'\t')
    af.write(pre3ljd+'\t')
    af.write(pre1lmn+'\t')
    af.write(pre2lmn+'\t')
    af.write(pre3lmn+'\t')

def prezent10(gos2):
    pre1ljd=gos2+u'ām'
    pre2ljd=gos2+u'āš'
    pre3ljd=gos2+u'ā'
    pre1lmn=gos2+u'āmo'
    pre2lmn=gos2+u'āte'
    pre3lmn=gos2+u'āju'
##    print 'Prezent: '
##    print pre1ljd+'\t'+pre1lmn
##    print pre2ljd+'\t'+pre2lmn
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+'\t')
    af.write(pre2ljd+'\t')
    af.write(pre3ljd+'\t')
    af.write(pre1lmn+'\t')
    af.write(pre2lmn+'\t')
    af.write(pre3lmn+'\t')

def prezent11(gos2,ngos2,gos3,naglasak,slog):
    pre1ljd=gos2+u'ēm'
    pre2ljd=gos2+u'ēš'
    pre3ljd=gos2+u'ē'
    pre1lmn=ngos2+u'ēmo'
    pre2lmn=ngos2+u'ēte'
    pre3lmn=gos3+u'ū'
##    print 'Prezent: '
##    print pre1ljd+'\t'+slog(pre1lmn,naglasak)
##    print pre2ljd+'\t'+slog(pre2lmn,naglasak)
##    print pre3ljd+'\t'+pre3lmn
    af.write(pre1ljd+u'\t')
    af.write(pre2ljd+u'\t')
    af.write(pre3ljd+u'\t')
    af.write(slog(pre1lmn,naglasak)+u'\t')
    af.write(slog(pre2lmn,naglasak)+u'\t')
    af.write(pre3lmn+u'\t')

def aorist1(gos2,gos3,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=gos2+'oh'
        ao2ljd=gos3+'e'
        ao3ljd=gos3+'e'
        ao1lmn=gos2+'osmo'
        ao2lmn=gos2+'oste'
        ao3lmn=gos2+u'ošē'
##        print 'Aorist: '
##        print ao1ljd+'\t'+ao1lmn
##        print ao2ljd+'\t'+ao2lmn
##        print ao3ljd+'\t'+ao3lmn
        af.write(ao1ljd+'\t')
        af.write(ao2ljd+'\t')
        af.write(ao3ljd+'\t')
        af.write(ao1lmn+'\t')
        af.write(ao2lmn+'\t')
        af.write(ao3lmn+'\t')

def aorist2(gos1,gos2,gos3,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=gos1+'h'
        ao2ljd=gos2
        ao3ljd=gos2
        ao1lmn=gos3+'smo'
        ao2lmn=gos3+'ste'
        ao3lmn=gos3+u'šē'
##        print 'Aorist: '
##        print ao1ljd+'\t'+ao1lmn
##        print ao2ljd+'\t'+ao2lmn
##        print ao3ljd+'\t'+ao3lmn
        af.write(ao1ljd+'\t')
        af.write(ao2ljd+'\t')
        af.write(ao3ljd+'\t')
        af.write(ao1lmn+'\t')
        af.write(ao2lmn+'\t')
        af.write(ao3lmn+'\t')

def aorist3(gos2,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=gos2+'eh'
        ao2ljd=gos2+'e'
        ao3ljd=gos2+'e'
        ao1lmn=gos2+'esmo'
        ao2lmn=gos2+'este'
        ao3lmn=gos2+u'ešē'
##        print 'Aorist: '
##        print ao1ljd+'\t'+ao1lmn
##        print ao2ljd+'\t'+ao2lmn
##        print ao3ljd+'\t'+ao3lmn
        af.write(ao1ljd+'\t')
        af.write(ao2ljd+'\t')
        af.write(ao3ljd+'\t')
        af.write(ao1lmn+'\t')
        af.write(ao2lmn+'\t')
        af.write(ao3lmn+'\t')

def aorist4(gos2,gos3,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=gos2+'oh'
        ao2ljd=gos3+'e'
        ao3ljd=gos3+'e'
        ao1lmn=gos2+'osmo'
        ao2lmn=gos2+'oste'
        ao3lmn=gos2+u'ošē'
##        print 'Aorist: '
##        print ao1ljd+'\t'+ao1lmn
##        print ao2ljd+'\t'+ao2lmn
##        print ao3ljd+'\t'+ao3lmn
        af.write(ao1ljd+'\t')
        af.write(ao2ljd+'\t')
        af.write(ao3ljd+'\t')
        af.write(ao1lmn+'\t')
        af.write(ao2lmn+'\t')
        af.write(ao3lmn+'\t')

def aorist5(gos2,gos3,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=gos2+'ih'
        ao2ljd=gos3+'i'
        ao3ljd=gos3+'i'
        ao1lmn=gos2+'ismo'
        ao2lmn=gos2+'iste'
        ao3lmn=gos2+u'išē'
##        print 'Aorist: '
##        print ao1ljd+'\t'+ao1lmn
##        print ao2ljd+'\t'+ao2lmn
##        print ao3ljd+'\t'+ao3lmn
        af.write(ao1ljd+'\t')
        af.write(ao2ljd+'\t')
        af.write(ao3ljd+'\t')
        af.write(ao1lmn+'\t')
        af.write(ao2lmn+'\t')
        af.write(ao3lmn+'\t')

def aorist6(gos1,gos2,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=gos1+'h'
        ao2ljd=gos2
        ao3ljd=gos2
        ao1lmn=gos1+'smo'
        ao2lmn=gos1+'ste'
        ao3lmn=gos1+u'šē'
##        print 'Aorist: '
##        print ao1ljd+'\t'+ao1lmn
##        print ao2ljd+'\t'+ao2lmn
##        print ao3ljd+'\t'+ao3lmn
        af.write(ao1ljd+'\t')
        af.write(ao2ljd+'\t')
        af.write(ao3ljd+'\t')
        af.write(ao1lmn+'\t')
        af.write(ao2lmn+'\t')
        af.write(ao3lmn+'\t')

def aorist7(ngos,slog,naglasak,naglasak1,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=ngos+'oh'
        ao2ljd=ngos+'e'
        ao3ljd=ngos+'e'
        ao1lmn=ngos+'osmo'
        ao2lmn=ngos+'oste'
        ao3lmn=ngos+u'ošē'
##        print 'Aorist: '
##        print slog(ao1ljd,naglasak)+'\t'+slog(ao1lmn,naglasak)
##        print slog(ao2ljd,naglasak1)+'\t'+slog(ao2lmn,naglasak)
##        print slog(ao3ljd,naglasak1)+'\t'+slog(ao3lmn,naglasak)
        af.write(slog(ao1ljd,naglasak)+'\t')
        af.write(slog(ao2ljd,naglasak1)+'\t')
        af.write(slog(ao3ljd,naglasak1)+'\t')
        af.write(slog(ao1lmn,naglasak)+'\t')
        af.write(slog(ao2lmn,naglasak)+'\t')
        af.write(slog(ao3lmn,naglasak)+'\t')

def aorist8(ngos,ngos2,slog,naglasak,naglasak1,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=ngos+'oh'
        ao2ljd=ngos2+'e'
        ao3ljd=ngos2+'e'
        ao1lmn=ngos+'osmo'
        ao2lmn=ngos+'oste'
        ao3lmn=ngos+u'ošē'
##        print 'Aorist: '
##        print slog(ao1ljd,naglasak)+'\t'+slog(ao1lmn,naglasak)
##        print slog(ao2ljd,naglasak1)+'\t'+slog(ao2lmn,naglasak)
##        print slog(ao3ljd,naglasak1)+'\t'+slog(ao3lmn,naglasak)
        af.write(slog(ao1ljd,naglasak)+'\t')
        af.write(slog(ao2ljd,naglasak1)+'\t')
        af.write(slog(ao3ljd,naglasak1)+'\t')
        af.write(slog(ao1lmn,naglasak)+'\t')
        af.write(slog(ao2lmn,naglasak)+'\t')
        af.write(slog(ao3lmn,naglasak)+'\t')

def aorist9(ngos,ngos2,slog,naglasak,naglasak1,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=ngos+'h'
        ao2ljd=ngos2
        ao3ljd=ngos2
        ao1lmn=ngos+'smo'
        ao2lmn=ngos+'ste'
        ao3lmn=ngos+u'šē'
##        print 'Aorist: '
##        print slog(ao1ljd,naglasak)+'\t'+slog(ao1lmn,naglasak)
##        print slog(ao2ljd,naglasak1)+'\t'+slog(ao2lmn,naglasak)
##        print slog(ao3ljd,naglasak1)+'\t'+slog(ao3lmn,naglasak)
        af.write(slog(ao1ljd,naglasak)+'\t')
        af.write(slog(ao2ljd,naglasak1)+'\t')
        af.write(slog(ao3ljd,naglasak1)+'\t')
        af.write(slog(ao1lmn,naglasak)+'\t')
        af.write(slog(ao2lmn,naglasak)+'\t')
        af.write(slog(ao3lmn,naglasak)+'\t')

def aorist10(gos2,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=gos2+'ijeh'
        ao2ljd=gos2+'ije'
        ao3ljd=gos2+'ije'
        ao1lmn=gos2+'ijesmo'
        ao2lmn=gos2+'ijeste'
        ao3lmn=gos2+u'iješē'
##        print 'Aorist: '
##        print ao1ljd+'\t'+ao1lmn
##        print ao2ljd+'\t'+ao2lmn
##        print ao3ljd+'\t'+ao3lmn
        af.write(ao1ljd+'\t')
        af.write(ao2ljd+'\t')
        af.write(ao3ljd+'\t')
        af.write(ao1lmn+'\t')
        af.write(ao2lmn+'\t')
        af.write(ao3lmn+'\t')

def aorist11(gos2,svr):
    if svr==1:
        af.write('\t\t\t\t\t\t')
    else:
        ao1ljd=gos2+'h'
        ao2ljd=gos2+'e'
        ao3ljd=gos2+'e'
        ao1lmn=gos2+'smo'
        ao2lmn=gos2+'ste'
        ao3lmn=gos2+u'šē'
##        print 'Aorist: '
##        print ao1ljd+'\t'+ao1lmn
##        print ao2ljd+'\t'+ao2lmn
##        print ao3ljd+'\t'+ao3lmn
        af.write(ao1ljd+'\t')
        af.write(ao2ljd+'\t')
        af.write(ao3ljd+'\t')
        af.write(ao1lmn+'\t')
        af.write(ao2lmn+'\t')
        af.write(ao3lmn+'\t')

def imperfekt1(gos2,nesvr):
    if nesvr==2:
        af.write('\t\t\t\t\t\t')
    else:
        ipf1ljd=gos2+u'ijāh'
        ipf2ljd=gos2+u'ijāše'
        ipf3ljd=gos2+u'ijāše'
        ipf1lmn=gos2+u'ijāsmo'
        ipf2lmn=gos2+u'ijāste'
        ipf3lmn=gos2+u'ijāhu'
##        print 'Imperfekt: '
##        print ipf1ljd+'\t'+ipf1lmn
##        print ipf2ljd+'\t'+ipf2lmn
##        print ipf3ljd+'\t'+ipf3lmn
        af.write(ipf1ljd+'\t')
        af.write(ipf2ljd+'\t')
        af.write(ipf3ljd+'\t')
        af.write(ipf1lmn+'\t')
        af.write(ipf2lmn+'\t')
        af.write(ipf3lmn+'\t')

def imperfekt2(gos2,nesvr):
    if nesvr==2:
        af.write('\t\t\t\t\t\t')
    else:
        ipf1ljd=gos2+u'āh'
        ipf2ljd=gos2+u'āše'
        ipf3ljd=gos2+u'āše'
        ipf1lmn=gos2+u'āsmo'
        ipf2lmn=gos2+u'āste'
        ipf3lmn=gos2+u'āhu'
##        print 'Imperfekt: '
##        print ipf1ljd+'\t'+ipf1lmn
##        print ipf2ljd+'\t'+ipf2lmn
##        print ipf3ljd+'\t'+ipf3lmn
        af.write(ipf1ljd+'\t')
        af.write(ipf2ljd+'\t')
        af.write(ipf3ljd+'\t')
        af.write(ipf1lmn+'\t')
        af.write(ipf2lmn+'\t')
        af.write(ipf3lmn+'\t')

def imperfekt3(gos1,nesvr):
    if nesvr==2:
        af.write('\t\t\t\t\t\t')
    else:
        ipf1ljd=gos1+'h'
        ipf2ljd=gos1+u'še'
        ipf3ljd=gos1+u'še'
        ipf1lmn=gos1+'smo'
        ipf2lmn=gos1+'ste'
        ipf3lmn=gos1+'hu'
##        print 'Imperfekt: '
##        print ipf1ljd+'\t'+ipf1lmn
##        print ipf2ljd+'\t'+ipf2lmn
##        print ipf3ljd+'\t'+ipf3lmn
        af.write(ipf1ljd+'\t')
        af.write(ipf2ljd+'\t')
        af.write(ipf3ljd+'\t')
        af.write(ipf1lmn+'\t')
        af.write(ipf2lmn+'\t')
        af.write(ipf3lmn+'\t')

def imperfekt4(gos2,nesvr):
    if nesvr==2:
        af.write('\t\t\t\t\t\t')
    else:
        ipf1ljd=gos2+u'âh'
        ipf2ljd=gos2+u'âše'
        ipf3ljd=gos2+u'âše'
        ipf1lmn=gos2+u'âsmo'
        ipf2lmn=gos2+u'âste'
        ipf3lmn=gos2+u'âhu'
##        print 'Imperfekt: '
##        print ipf1ljd+'\t'+ipf1lmn
##        print ipf2ljd+'\t'+ipf2lmn
##        print ipf3ljd+'\t'+ipf3lmn
        af.write(ipf1ljd+'\t')
        af.write(ipf2ljd+'\t')
        af.write(ipf3ljd+'\t')
        af.write(ipf1lmn+'\t')
        af.write(ipf2lmn+'\t')
        af.write(ipf3lmn+'\t')

def imperfekt5(gos2,nesvr):
    if nesvr==2:
        af.write('\t\t\t\t\t\t')
    else:
        ipf1ljd=gos2+u'āh'
        ipf2ljd=gos2+u'āše'
        ipf3ljd=gos2+u'āše'
        ipf1lmn=gos2+u'āsmo'
        ipf2lmn=gos2+u'āste'
        ipf3lmn=gos2+u'āhu'
##        print 'Imperfekt: '
##        print ipf1ljd+'\t'+ipf1lmn
##        print ipf2ljd+'\t'+ipf2lmn
##        print ipf3ljd+'\t'+ipf3lmn
        af.write(ipf1ljd+'\t')
        af.write(ipf2ljd+'\t')
        af.write(ipf3ljd+'\t')
        af.write(ipf1lmn+'\t')
        af.write(ipf2lmn+'\t')
        af.write(ipf3lmn+'\t')

def imperfekt6(gos2,ngos2,naglasak,slog,slog2,nesvr):
    if nesvr==2:
        af.write('\t\t\t\t\t\t')
    else:
        ipf1ljd=ngos2+u'ijāh'
        ipf2ljd=gos2+u'ijāše'
        ipf3ljd=gos2+u'ijāše'
        ipf1lmn=gos2+u'ijāsmo'
        ipf2lmn=ngos2+u'ijāste'
        ipf3lmn=ngos2+u'ijāhu'
##        print 'Imperfekt: '
##        print slog(ipf1ljd,naglasak)+'\t'+ipf1lmn
##        print ipf2ljd+'\t'+slog2(ipf2lmn,naglasak)
##        print ipf3ljd+'\t'+slog2(ipf3lmn,naglasak)
        af.write(slog(ipf1ljd,naglasak)+'\t')
        af.write(ipf2ljd+'\t')
        af.write(ipf3ljd+'\t')
        af.write(ipf1lmn+'\t')
        af.write(slog2(ipf2lmn,naglasak)+'\t')
        af.write(slog2(ipf3lmn,naglasak)+'\t')

def imperfekt7(ngos2,naglasak,slog,slog2,nesvr):
    if nesvr==2:
        af.write('\t\t\t\t\t\t')
    else:
        ipf1ljd=ngos2+u'āh'
        ipf2ljd=ngos2+u'āše'
        ipf3ljd=ngos2+u'āše'
        ipf1lmn=ngos2+u'āsmo'
        ipf2lmn=ngos2+u'āste'
        ipf3lmn=ngos2+u'āhu'
##        print 'Imperfekt: '
##        print slog(ipf1ljd,naglasak)+'\t'+slog2(ipf1lmn,naglasak)
##        print slog2(ipf2ljd,naglasak)+'\t'+slog2(ipf2lmn,naglasak)
##        print slog2(ipf3ljd,naglasak)+'\t'+slog2(ipf3lmn,naglasak)
        af.write(slog(ipf1ljd,naglasak)+'\t')
        af.write(slog2(ipf2ljd,naglasak)+'\t')
        af.write(slog2(ipf3ljd,naglasak)+'\t')
        af.write(slog2(ipf1lmn,naglasak)+'\t')
        af.write(slog2(ipf2lmn,naglasak)+'\t')
        af.write(slog2(ipf3lmn,naglasak)+'\t')

def imperfekt8(gos2,nesvr):
    if nesvr==2:
        af.write('\t\t\t\t\t\t')
    else:
        ipf1ljd=gos2+u'ijāh'
        ipf2ljd=gos2+u'ijāše'
        ipf3ljd=gos2+u'ijāše'
        ipf1lmn=gos2+u'ijāsmo'
        ipf2lmn=gos2+u'ijāste'
        ipf3lmn=gos2+u'ijāhu'
##        print 'Imperfekt: '
##        print ipf1ljd+'\t'+ipf1lmn
##        print ipf2ljd+'\t'+ipf2lmn
##        print ipf3ljd+'\t'+ipf3lmn
        af.write(ipf1ljd+'\t')
        af.write(ipf2ljd+'\t')
        af.write(ipf3ljd+'\t')
        af.write(ipf1lmn+'\t')
        af.write(ipf2lmn+'\t')
        af.write(ipf3lmn+'\t')

def imperfekt9(gos2,nesvr):
    if nesvr==2:
        af.write('\t\t\t\t\t\t')
    else:
        ipf1ljd=gos2+'h'
        ipf2ljd=gos2+u'še'
        ipf3ljd=gos2+u'še'
        ipf1lmn=gos2+'smo'
        ipf2lmn=gos2+'ste'
        ipf3lmn=gos2+'hu'
##        print 'Imperfekt: '
##        print ipf1ljd+'\t'+ipf1lmn
##        print ipf2ljd+'\t'+ipf2lmn
##        print ipf3ljd+'\t'+ipf3lmn
        af.write(ipf1ljd+'\t')
        af.write(ipf2ljd+'\t')
        af.write(ipf3ljd+'\t')
        af.write(ipf1lmn+'\t')
        af.write(ipf2lmn+'\t')
        af.write(ipf3lmn+'\t')

def imperativ1(gos2):
    imp2ljd=gos2+'i'
    imp1lmn=gos2+'imo'
    imp2lmn=gos2+'ite'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def imperativ2(gos2):
    imp2ljd=gos2
    imp1lmn=gos2+'mo'
    imp2lmn=gos2+'te'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def imperativ3(gos2):
    imp2ljd=gos2+'ij'
    imp1lmn=gos2+'ijmo'
    imp2lmn=gos2+'ijte'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def imperativ4(gos2):
    imp2ljd=gos2+u'ȉ'
    imp1lmn=gos2+u'ȉmo'
    imp2lmn=gos2+u'ȉte'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def imperativ5(gos2):
    imp2ljd=gos2+u'ȉj'
    imp1lmn=gos2+u'ȉjmo'
    imp2lmn=gos2+u'ȉjte'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def imperativ6(gos2):
    imp2ljd=gos2+u'ì'
    imp1lmn=gos2+u'ìmo'
    imp2lmn=gos2+u'ìte'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def imperativ7(ngos,naglasak,naglasak1,slog,slog2):
    imp2ljd=ngos+'i'
    imp1lmn=ngos+'imo'
    imp2lmn=ngos+'ite'
##    print 'Imperativ: '
##    print '-'+'\t'+slog2(imp1lmn,naglasak1)
##    print slog(imp2ljd,naglasak)+'\t'+slog2(imp2lmn,naglasak1)
##    print '-'+'\t'+'-'
    af.write(slog(imp2ljd,naglasak)+'\t')
    af.write(slog2(imp1lmn,naglasak)+'\t')
    af.write(slog2(imp2lmn,naglasak)+'\t')

def imperativ8(gos2):
    imp2ljd=gos2+'i'
    imp1lmn=gos2+'imo'
    imp2lmn=gos2+'ite'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def imperativ9(gos2):
    imp2ljd=gos2+'aj'
    imp1lmn=gos2+'ajmo'
    imp2lmn=gos2+'ajte'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def imperativ10(gos2):
    imp2ljd=gos2+'ij'
    imp1lmn=gos2+'ijmo'
    imp2lmn=gos2+'ijte'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def imperativ11(gos2):
    imp2ljd=gos2
    imp1lmn=gos2+'mo'
    imp2lmn=gos2+'te'
##    print 'Imperativ: '
##    print '-'+'\t'+imp1lmn
##    print imp2ljd+'\t'+imp2lmn
##    print '-'+'\t'+'-'
    af.write(imp2ljd+'\t')
    af.write(imp1lmn+'\t')
    af.write(imp2lmn+'\t')

def prad1(gos1,gos2):
    pradmrjd=gos2+'o'
    pradzrjd=gos1+'la'
    pradsrjd=gos1+'lo'
    pradmrmn=gos1+'li'
    pradzrmn=gos1+'le'
    pradsrmn=gos1+'la'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad2(gos2):
    pradmrjd=gos2+'ao'
    pradzrjd=gos2+'la'
    pradsrjd=gos2+'lo'
    pradmrmn=gos2+'li'
    pradzrmn=gos2+'le'
    pradsrmn=gos2+'la'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad3(gos2,gos1):
    pradmrjd=gos2+'ao'
    pradzrjd=gos2+'la'
    pradsrjd=gos2+'lo'
    pradmrmn=gos1+'li'
    pradzrmn=gos1+'le'
    pradsrmn=gos1+'la'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad4(gos2):
    pradmrjd=gos2+'eo'
    pradzrjd=gos2+'ela'
    pradsrjd=gos2+'elo'
    pradmrmn=gos2+'eli'
    pradzrmn=gos2+'ele'
    pradsrmn=gos2+'ela'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad5(gos1,gos2):
    pradmrjd=gos2+u'ô'
    pradzrjd=gos1+'la'
    pradsrjd=gos1+'lo'
    pradmrmn=gos1+'li'
    pradzrmn=gos1+'le'
    pradsrmn=gos1+'la'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad6(gos1,gos2):
    pradmrjd=gos2+u'îo'
    pradzrjd=gos1+'la'
    pradsrjd=gos1+'lo'
    pradmrmn=gos1+'li'
    pradzrmn=gos1+'le'
    pradsrmn=gos1+'la'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad7(gos2):
    pradmrjd=gos2+u'ȅo'
    pradzrjd=gos2+u'ȅla'
    pradsrjd=gos2+u'ȅlo'
    pradmrmn=gos2+u'ȅli'
    pradzrmn=gos2+u'ȅle'
    pradsrmn=gos2+u'ȅla'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad8(gos2):
    pradmrjd=gos2+'ao'
    pradzrjd=gos2+'la'
    pradsrjd=gos2+'lo'
    pradmrmn=gos2+'li'
    pradzrmn=gos2+'le'
    pradsrmn=gos2+'la'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad9(gos2):
    pradmrjd=gos2+'o'
    pradzrjd=gos2+'la'
    pradsrjd=gos2+'lo'
    pradmrmn=gos2+'li'
    pradzrmn=gos2+'le'
    pradsrmn=gos2+'la'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad10(gos1,gos2):
    pradmrjd=gos1+'io'
    pradzrjd=gos2+'la'
    pradsrjd=gos2+'lo'
    pradmrmn=gos2+'li'
    pradzrmn=gos2+'le'
    pradsrmn=gos2+'la'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad11(gos2):
    pradmrjd=gos2+'ao'
    pradzrjd=gos2+'ala'
    pradsrjd=gos2+'alo'
    pradmrmn=gos2+'ali'
    pradzrmn=gos2+'ale'
    pradsrmn=gos2+'ala'
##    print 'Pridjev radni: '
##    print pradmrjd+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(pradmrjd+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad12(ngos2,gos1,naglasak,slog):
    pradmrjd=ngos2+'ao'
    pradzrjd=gos1+'la'
    pradsrjd=gos1+'lo'
    pradmrmn=gos1+'li'
    pradzrmn=gos1+'le'
    pradsrmn=gos1+'la'
##    print 'Pridjev radni: '
##    print slog(pradmrjd,naglasak)+'\t'+pradmrmn
##    print pradzrjd+'\t'+pradzrmn
##    print pradsrjd+'\t'+pradsrmn
    af.write(slog(pradmrjd,naglasak)+'\t')
    af.write(pradzrjd+'\t')
    af.write(pradsrjd+'\t')
    af.write(pradmrmn+'\t')
    af.write(pradzrmn+'\t')
    af.write(pradsrmn+'\t')

def prad13(ngos2,naglasak,slog):
    pradmrjd=ngos2+'ao'
    pradzrjd=ngos2+'la'
    pradsrjd=ngos2+'lo'
    pradmrmn=ngos2+'li'
    pradzrmn=ngos2+'le'
    pradsrmn=ngos2+'la'
##    print 'Pridjev radni: '
##    print slog(pradmrjd,naglasak)+'\t'+slog(pradmrmn,naglasak)
##    print slog(pradzrjd,naglasak)+'\t'+slog(pradzrmn,naglasak)
##    print slog(pradsrjd,naglasak)+'\t'+slog(pradsrmn,naglasak)
    af.write(slog(pradmrjd,naglasak)+'\t')
    af.write(slog(pradzrjd,naglasak)+'\t')
    af.write(slog(pradsrjd,naglasak)+'\t')
    af.write(slog(pradmrmn,naglasak)+'\t')
    af.write(slog(pradzrmn,naglasak)+'\t')
    af.write(slog(pradsrmn,naglasak)+'\t')

def ptrpni(gos2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos2+'en'
        ptrzrjd=gos2+'ena'
        ptrsrjd=gos2+'eno'
        ptrmrmn=gos2+'eni'
        ptrzrmn=gos2+'ene'
        ptrsrmn=gos2+'ena'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni2(gos1,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos1+'n'
        ptrzrjd=gos1+'na'
        ptrsrjd=gos1+'no'
        ptrmrmn=gos1+'ni'
        ptrzrmn=gos1+'ne'
        ptrsrmn=gos1+'na'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni3(gos1,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos1+'ven'
        ptrzrjd=gos1+'vena'
        ptrsrjd=gos1+'veno'
        ptrmrmn=gos1+'veni'
        ptrzrmn=gos1+'vene'
        ptrsrmn=gos1+'vena'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')
    
def ptrpni4(gos1,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos1+'jen'
        ptrzrjd=gos1+'jena'
        ptrsrjd=gos1+'jeno'
        ptrmrmn=gos1+'jeni'
        ptrzrmn=gos1+'jene'
        ptrsrmn=gos1+'jena'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni5(gos1,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos1+'t'
        ptrzrjd=gos1+'ta'
        ptrsrjd=gos1+'to'
        ptrmrmn=gos1+'ti'
        ptrzrmn=gos1+'te'
        ptrsrmn=gos1+'ta'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni6(gos2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos2+'even'
        ptrzrjd=gos2+'evena'
        ptrsrjd=gos2+'eveno'
        ptrmrmn=gos2+'eveni'
        ptrzrmn=gos2+'evene'
        ptrsrmn=gos2+'evena'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni7(gos2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos2+'ut'
        ptrzrjd=gos2+'uta'
        ptrsrjd=gos2+'uto'
        ptrmrmn=gos2+'uti'
        ptrzrmn=gos2+'ute'
        ptrsrmn=gos2+'uta'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni8(gos2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos2+u'êven'
        ptrzrjd=gos2+u'êvena'
        ptrsrjd=gos2+u'êveno'
        ptrmrmn=gos2+u'êveni'
        ptrzrmn=gos2+u'êvene'
        ptrsrmn=gos2+u'êvena'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni9(gos2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos2+'en'
        ptrzrjd=gos2+'ena'
        ptrsrjd=gos2+'eno'
        ptrmrmn=gos2+'eni'
        ptrzrmn=gos2+'ene'
        ptrsrmn=gos2+'ena'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni10(gos2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos2+'ut'
        ptrzrjd=gos2+'uta'
        ptrsrjd=gos2+'uto'
        ptrmrmn=gos2+'uti'
        ptrzrmn=gos2+'ute'
        ptrsrmn=gos2+'uta'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni11(gos2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos2+'n'
        ptrzrjd=gos2+'na'
        ptrsrjd=gos2+'no'
        ptrmrmn=gos2+'ni'
        ptrzrmn=gos2+'ne'
        ptrsrmn=gos2+'na'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni12(ngos,naglasak,slog,slog2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=ngos+'en'
        ptrzrjd=ngos+'ena'
        ptrsrjd=ngos+'eno'
        ptrmrmn=ngos+'eni'
        ptrzrmn=ngos+'ene'
        ptrsrmn=ngos+'ena'
##        print 'Pridjev trpni: '
##        print slog2(ptrmrjd,naglasak)+'\t'+slog(ptrmrmn,naglasak)
##        print slog(ptrzrjd,naglasak)+'\t'+slog(ptrzrmn,naglasak)
##        print slog(ptrsrjd,naglasak)+'\t'+slog(ptrsrmn,naglasak)
        af.write(slog2(ptrmrjd,naglasak)+'\t')
        af.write(slog(ptrzrjd,naglasak)+'\t')
        af.write(slog(ptrsrjd,naglasak)+'\t')
        af.write(slog(ptrmrmn,naglasak)+'\t')
        af.write(slog(ptrzrmn,naglasak)+'\t')
        af.write(slog(ptrsrmn,naglasak)+'\t')

def ptrpni13(gos1,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos1+'t'
        ptrzrjd=gos1+'ta'
        ptrsrjd=gos1+'to'
        ptrmrmn=gos1+'ti'
        ptrzrmn=gos1+'te'
        ptrsrmn=gos1+'ta'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni14(ngos,naglasak,slog,slog2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=ngos+'ut'
        ptrzrjd=ngos+'uta'
        ptrsrjd=ngos+'uto'
        ptrmrmn=ngos+'uti'
        ptrzrmn=ngos+'ute'
        ptrsrmn=ngos+'uta'
##        print 'Pridjev trpni: '
##        print slog2(ptrmrjd,naglasak)+'\t'+slog(ptrmrmn,naglasak)
##        print slog(ptrzrjd,naglasak)+'\t'+slog(ptrzrmn,naglasak)
##        print slog(ptrsrjd,naglasak)+'\t'+slog(ptrsrmn,naglasak)
        af.write(slog2(ptrmrjd,naglasak)+'\t')
        af.write(slog(ptrzrjd,naglasak)+'\t')
        af.write(slog(ptrsrjd,naglasak)+'\t')
        af.write(slog(ptrmrmn,naglasak)+'\t')
        af.write(slog(ptrzrmn,naglasak)+'\t')
        af.write(slog(ptrsrmn,naglasak)+'\t')

def ptrpni15(gos1,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=gos1+'et'
        ptrzrjd=gos1+'eta'
        ptrsrjd=gos1+'eto'
        ptrmrmn=gos1+'eti'
        ptrzrmn=gos1+'ete'
        ptrsrmn=gos1+'eta'
##        print 'Pridjev trpni: '
##        print ptrmrjd+'\t'+ptrmrmn
##        print ptrzrjd+'\t'+ptrzrmn
##        print ptrsrjd+'\t'+ptrsrmn
        af.write(ptrmrjd+'\t')
        af.write(ptrzrjd+'\t')
        af.write(ptrsrjd+'\t')
        af.write(ptrmrmn+'\t')
        af.write(ptrzrmn+'\t')
        af.write(ptrsrmn+'\t')

def ptrpni16(ngos,naglasak,slog,slog2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=ngos+'ven'
        ptrzrjd=ngos+'vena'
        ptrsrjd=ngos+'veno'
        ptrmrmn=ngos+'veni'
        ptrzrmn=ngos+'vene'
        ptrsrmn=ngos+'vena'
##        print 'Pridjev trpni: '
##        print slog2(ptrmrjd,naglasak)+'\t'+slog(ptrmrmn,naglasak)
##        print slog(ptrzrjd,naglasak)+'\t'+slog(ptrzrmn,naglasak)
##        print slog(ptrsrjd,naglasak)+'\t'+slog(ptrsrmn,naglasak)
        af.write(slog2(ptrmrjd,naglasak)+'\t')
        af.write(slog(ptrzrjd,naglasak)+'\t')
        af.write(slog(ptrsrjd,naglasak)+'\t')
        af.write(slog(ptrmrmn,naglasak)+'\t')
        af.write(slog(ptrzrmn,naglasak)+'\t')
        af.write(slog(ptrsrmn,naglasak)+'\t')

def ptrpni17(ngos,naglasak,slog,slog2,prel):
    if prel==2:
        af.write('\t\t\t\t\t\t')
    else:
        ptrmrjd=ngos+'t'
        ptrzrjd=ngos+'ta'
        ptrsrjd=ngos+'to'
        ptrmrmn=ngos+'ti'
        ptrzrmn=ngos+'te'
        ptrsrmn=ngos+'ta'
##        print 'Pridjev trpni: '
##        print slog2(ptrmrjd,naglasak)+'\t'+slog(ptrmrmn,naglasak)
##        print slog(ptrzrjd,naglasak)+'\t'+slog(ptrzrmn,naglasak)
##        print slog(ptrsrjd,naglasak)+'\t'+slog(ptrsrmn,naglasak)
        af.write(slog2(ptrmrjd,naglasak)+'\t')
        af.write(slog(ptrzrjd,naglasak)+'\t')
        af.write(slog(ptrsrjd,naglasak)+'\t')
        af.write(slog(ptrmrmn,naglasak)+'\t')
        af.write(slog(ptrzrmn,naglasak)+'\t')
        af.write(slog(ptrsrmn,naglasak)+'\t')

def psad(gos2,svr):
    if svr==2:
        af.write('\t')
    else:
        psad=gos2+u'ūći'
##        print u'Glag. prilog sadašnji: '
##        print psad
        af.write(psad+'\t')
    
def psad2(gos2,svr):
    if svr==2:
        af.write('\t')
    else:
        psad=gos2+u'éći'
##        print u'Glag. prilog sadašnji: '
##        print psad
        af.write(psad+'\t')

def psad3(gos2,svr):
    if svr==2:
        af.write('\t')
    else:
        psad=gos2+u'êći'
##        print u'Glag. prilog sadašnji: '
##        print psad
        af.write(psad+'\t')

def psad4(gos2,svr):
    if svr==2:
        af.write('\t')
    else:
        psad=gos2+u'ûći'
##        print u'Glag. prilog sadašnji: '
##        print psad
        af.write(psad+'\t')

def psad5(gos2,svr):
    if svr==2:
        af.write('\t')
    else:
        psad=gos2+u'ūći'
##        print u'Glag. prilog sadašnji: '
##        print psad
        af.write(psad+'\t')

def psad6(gos2,svr):
    if svr==2:
        af.write('\t')
    else:
        psad=gos2+u'ēći'
##        print u'Glag. prilog sadašnji: '
##        print psad
        af.write(psad+'\t')

def psad7(gos2,svr):
    if svr==2:
        af.write('\t')
    else:
        psad=gos2+u'ajūći'
##        print u'Glag. prilog sadašnji: '
##        print psad
        af.write(psad+'\t')

def psad8(ngos,naglasak,slog,svr):
    if svr==2:
        af.write('\t')
    else:
        psad=ngos+u'ūći'
##        print u'Glag. prilog sadašnji: '
##        print slog(psad,naglasak)
        af.write(slog(psad,naglasak)+'\t')

def ppro1(gos1,nesvr):
    if nesvr==1:
        af.write('\t')
    else:
        ppro=gos1+u'vši'
##        print u'Glag. prilog prošli: '
##        print ppro
        af.write(ppro+'\t')

def ppro2(gos2,nesvr):
    if nesvr==1:
        af.write('\t')
    else:
        ppro=gos2+u'avši'
##        print u'Glag. prilog prošli: '
##        print ppro
        af.write(ppro+'\t')

def ppro3(gos2,nesvr):
    if nesvr==1:
        af.write('\t')
    else:
        ppro=gos2+u'âvši'
##        print u'Glag. prilog prošli: '
##        print ppro
        af.write(ppro+'\t')

def ppro4(gos2,nesvr):
    if nesvr==1:
        af.write('\t')
    else:
        ppro=gos2+u'avši'
##        print u'Glag. prilog prošli: '
##        print ppro
        af.write(ppro+'\t')

def ppro5(gos2,nesvr):
    if nesvr==1:
        af.write('\t')
    else:
        ppro=gos2+u'vši'
##        print u'Glag. prilog prošli: '
##        print ppro
        af.write(ppro+'\t')

def ppro6(ngos,naglasak,slog,nesvr):
    if nesvr==1:
        af.write('\t')
    else:
        ppro=ngos+u'avši'
##        print u'Glag. prilog prošli: '
##        print slog(ppro,naglasak)
        af.write(slog(ppro,naglasak)+'\t')

if __name__=='__main__':
    import codecs,re,sys,string

    af=codecs.open('zapis_2sl_3sl.txt','w','utf-8')
    tablica=[]

    for red in codecs.open('glagoli.txt','r','utf-8').readlines():
        infs=red[:string.find(red,'\t')]
        pres=red[string.find(red,'\t')+1:string.rfind(red,'\t')]
        svr_prel=red[string.rfind(red,'\t')+1:-1]
        tablica.append([])
        tablica[-1].append(infs)
        tablica[-1].append(pres)
        if 'svr/nesvr' in svr_prel:
            tablica[-1].append(0)
        elif 'nesvr' in svr_prel:
            tablica[-1].append(1)
        elif 'svr' in svr_prel:
            tablica[-1].append(2)
        else:
            tablica[-1].append(None)
        if 'prel/neprel' in svr_prel:
            tablica[-1].append(0)
        elif 'prel' in svr_prel:
            tablica[-1].append(1)
        elif 'neprel' in svr_prel:
            tablica[-1].append(2)
        else:
            tablica[-1].append(None)

        if infs[-3:] in ' se' or pres[-3:] in ' se':
            infs=infs[:-3]
            pres=pres[:-3]

        si=slog(infs)

        gos1=infs[:-2]
        gos2=pres[:-2]

        if si<4:
            af.write(nenag_sam(infs)+'\t'+infs+'\t')

        if si==3:
            ngos1=nenag_sam(gos1)
            ngos2=nenag_sam(gos2)

        ##  Dvosložni 1. grupa glagola: inf. -sti, prez. t-em d-em

        if infs[-3:] in 'sti' and pres[-3:] in u'tēmdēm' and si==2:
            ## 1. grupa a: bȍsti - bòdēm, b: jȅsti - jȅdēm, c: krȁsti -krádēm
            for bs in gos1: 
                if bs in u'ȑȁȅȉȍȕ':
                    for cs in gos2:
                        if cs in u'ŗàèìòù':
                            gos3=kratkosilazni(cs,gos2)
                            gos4=gos1[:-1]
                            prezent1(gos2)
                            aorist1(gos2,gos3,tablica[-1][2])
                            imperfekt1(gos2,tablica[-1][2])
                            imperativ1(gos2)
                            prad1(gos4,gos4)
                            ptrpni(gos2,tablica[-1][3])
                            psad(gos2,tablica[-1][2])
                            ppro1(gos4,tablica[-1][2])
                        elif cs in u'ȑȁȅȉȍȕ':
                            prezent1(gos2)
                            aorist1(gos2,gos2,tablica[-1][2])
                            gos3=gos2[:-1]+u'đ'
                            gos4=gos1[:-1]
                            imperfekt2(gos3,tablica[-1][2])
                            imperativ1(gos2)
                            prad1(gos4,gos4)
                            ptrpni(gos2,tablica[-1][3])
                            psad(gos2,tablica[-1][2])
                            ppro1(gos4,tablica[-1][2])
                        elif cs in u'ŕáéíóú':
                            gos3=kratkosilazni(cs,gos2)
                            gos4=dugosilazni(cs,gos2)
                            gos5=kratkouzlazni(cs,gos2)
                            gos6=gos1[:-1]
                            prezent1(gos2)
                            aorist1(gos3,gos4,tablica[-1][2])
                            imperfekt1(gos2,tablica[-1][2])
                            imperativ1(gos2)
                            prad1(gos6,gos6)
                            ptrpni(gos5,tablica[-1][3])
                            psad(gos2,tablica[-1][2])
                            ppro1(gos6,tablica[-1][2])
                ## 1. grupa b: râsti - rástēm
                elif bs in u'ȓâêîôû':
                    for cs in gos2:
                        if cs in u'ŕáéíóú':
                            gos3=dugosilazni(cs,gos2)
                            prezent1(gos2)
                            aorist1(gos2,gos3,tablica[-1][2])
                            imperfekt2(gos2,tablica[-1][2])
                            imperativ1(gos2)
                            prad3(gos3,gos1)
                            ptrpni(gos3,tablica[-1][3])
                            psad(gos2,tablica[-1][2])
                            ppro2(gos3,tablica[-1][2])
            af.write('\n')
                            
    ## Dvosložni 2. grupa glagola: inf. -sti, prez. s-em z-em 
            
        elif infs[-3:] in 'sti' and pres[-3:] in u'sēmzēm' and si==2:
            for bs in gos1: 
                ## 2. grupa: a: grȉsti - grízēm, b: svȅsti - svèzēm
                if bs in u'ȑȁȅȉȍȕ':
                    for cs in gos2:
                        if cs in u'ŕáéíóú':
                            gos3=kratkosilazni(cs,gos2)
                            gos4=dugosilazni(cs,gos2)
                            gos5=kratkouzlazni(cs,gos2)
                            prezent1(gos2)
                            aorist1(gos3,gos4,tablica[-1][2])
                            imperfekt1(gos2,tablica[-1][2])
                            imperativ1(gos2)
                            prad2(gos3)
                            ptrpni(gos5,tablica[-1][3])
                            psad(gos2,tablica[-1][2])
                            ppro2(gos3,tablica[-1][2])
                        elif cs in u'ŗàèìòù':
                            gos3=kratkosilazni(cs,gos2)
                            prezent1(gos2)
                            aorist1(gos2,gos3,tablica[-1][2])
                            imperfekt1(gos2,tablica[-1][2])
                            imperativ1(gos2)
                            prad2(gos3)
                            ptrpni(gos2,tablica[-1][3])
                            psad(gos2,tablica[-1][2])
                            ppro2(gos2,tablica[-1][2])
                ## 2. grupa: c: vêsti - vézēm
                elif bs in u'ȓâêîôû':
                    for cs in gos2:
                        if cs in u'ŕáéíóú':
                            gos3=dugosilazni(cs,gos2)
                            prezent1(gos2)
                            aorist1(gos2,gos3,tablica[-1][2])
                            imperfekt1(gos2,tablica[-1][2])
                            imperativ1(gos2)
                            prad2(gos3)
                            ptrpni(gos3,tablica[-1][3])
                            psad(gos2,tablica[-1][2])
                            ppro2(gos3,tablica[-1][2])
            af.write('\n')

    ## Dvosložni 3. grupa glagola: inf. -sti, prez. p-em b-em
            
        elif infs[-3:] in 'sti' and pres[-3:] in u'pēmbēm' and si==2:
            for bs in gos1: 
                ## 3. grupa: a: cȓpsti - cŕpēm
                if bs in u'ȓâêîôû':
                    for cs in gos2:
                        if cs in u'ŕáéíóú':
                            gos3=dugosilazni(cs,gos2)
                            prezent1(gos2)
                            aorist1(gos2,gos3,tablica[-1][2])
                            imperfekt2(gos2,tablica[-1][2])
                            imperativ1(gos2)
                            prad3(gos3,gos1)
                            ptrpni(gos3,tablica[-1][3])
                            psad(gos2,tablica[-1][2])
                            ppro2(gos3,tablica[-1][2])
                ## 3. grupa: b: grȅpsti - grèbēm
                if bs in u'ȑȁȅȉȍȕ':
                    for cs in gos2:
                        if cs in u'ŗàèìòù':
                            gos3=kratkosilazni(cs,gos2)
                            prezent1(gos2)
                            aorist1(gos2,gos3,tablica[-1][2])
                            imperfekt1(gos2,tablica[-1][2])
                            imperativ1(gos2)
                            prad3(gos3,gos1)
                            ptrpni(gos2,tablica[-1][3])
                            psad(gos2,tablica[-1][2])
                            ppro2(gos2,tablica[-1][2])
            af.write('\n')

    ## Dvosložni 4. grupa glagola: inf. -ći, prez. č-em, ž-em, š-em

        elif infs[-2:] in u'ći' and pres[-3:] in u'čēmžēmšēm' and si==2:
            for bs in gos1: 
                if bs in u'ȑȁȅȉȍȕ':
                    for cs in gos2:
                        ## 4. grupa: a: pȅći - pèčēm
                        if cs in u'ŗàèìòù':
                            gos3=palatalizacija(gos2)
                            gos4=sibilarizacija(gos2)
                            gos5=kratkosilazni(cs,gos2)
                            gos6=kratkosilazni(cs,gos3)
                            prezent2(gos2,gos3)
                            aorist1(gos3,gos5,tablica[-1][2])
                            imperfekt1(gos4,tablica[-1][2])
                            imperativ1(gos4)
                            prad2(gos6)
                            ptrpni(gos2,tablica[-1][3])
                            psad(gos3,tablica[-1][2])
                            ppro2(gos3,tablica[-1][2])
                        ## 4. grupa: b: sjȅći - sijéčēm
                        elif cs in u'ŕáéíóú':
                            gos3=krati(gos2)
                            gos4=palatalizacija(gos2)
                            gos5=krati(gos4)
                            gos7=sibilarizacija(gos2)
                            gos6=krati(gos7)
                            gos8=kratkosilazni(cs,gos5)
                            gos9=dugosilazni(cs,gos3)
                            gos10=kratkouzlazni(cs,gos3)
                            prezent2(gos2,gos4)
                            aorist1(gos8,gos9,tablica[-1][2])
                            imperfekt1(gos6,tablica[-1][2])
                            imperativ1(gos7)
                            prad2(gos8)
                            ptrpni(gos10,tablica[-1][3])
                            psad(gos4,tablica[-1][2])
                            ppro2(gos8,tablica[-1][2])
                        ## 4. grupa: d: rȅći - rȅčēm
                        elif cs in u'ȑȁȅȉȍȕ':
                            gos3=palatalizacija(gos2)
                            gos4=sibilarizacija(gos2)
                            prezent2(gos2,gos3)
                            aorist1(gos3,gos2,tablica[-1][2])
                            imperfekt1(gos4,tablica[-1][2])
                            imperativ1(gos4)
                            prad2(gos3)
                            ptrpni(gos2,tablica[-1][3])
                            psad(gos3,tablica[-1][2])
                            ppro2(gos3,tablica[-1][2])
                ## 4. grupa: c: vûći - vúčēm
                elif bs in u'ȓâêîôû':
                    for cs in gos2:
                        if cs in u'ŕáéíóú':
                            gos3=palatalizacija(gos2)
                            gos4=sibilarizacija(gos2)
                            gos5=dugosilazni(cs,gos2)
                            gos6=kratkouzlazni(cs,gos2)
                            gos7=dugosilazni(cs,gos3)
                            prezent2(gos2,gos3)
                            aorist1(gos3,gos5,tablica[-1][2])
                            imperfekt1(gos4,tablica[-1][2])
                            imperativ1(gos4)
                            prad2(gos7)                    
                            ptrpni(gos6,tablica[-1][3])
                            psad(gos3,tablica[-1][2])
                            ppro2(gos3,tablica[-1][2])
            af.write('\n')
                            
    ## Dvosložni 5. grupa glagola: inf. -eti, prez. m-em žêti - žnjêm
        elif infs[-3:] in u'êti' and pres[-4:] in u'njêm' and si==2:
            for bs in gos1:
                if bs in u'ȓâêîôû':
                    gos3=kratkouzlazni(bs,gos1)
                    gos4=dugouzlazni(bs,gos1)
            prezent6(gos2)
            aorist2(gos3,gos3,gos3,tablica[-1][2])
            imperfekt4(gos2,tablica[-1][2])
            imperativ6(gos2)
            prad1(gos4,gos3)
            ptrpni5(gos1,tablica[-1][3])
            psad4(gos2,tablica[-1][2])
            ppro1(gos1,tablica[-1][2])
            af.write('\n')

    ## Dvosložni 6. grupa glagola: inf. -eti, prez. enj-em, anj-em
        elif infs[-3:] in u'êtiȅti' and pres[-5:] in u'ȅnjēmȁnjēm' and si==2:
            for bs in gos1:
                ## 6. grupa: a: pêti se - pȅnjem se
                if bs in u'ȓâêîôû':
                    gos3=kratkosilazni(bs,gos1)
                    prezent1(gos2)
                    aorist2(gos1,gos1,gos1,tablica[-1][2])
                    imperfekt2(gos2,tablica[-1][2])
                    imperativ1(gos2)
                    prad1(gos1,gos3)
                    ptrpni5(gos1,tablica[-1][3])
                    psad(gos2,tablica[-1][2])
                    ppro1(gos1,tablica[-1][2])
                ## 6. grupa: b: žȅti - žȁnjēm
                elif bs in u'ȑȁȅȉȍȕ':
                    for cs in gos2:
                        if cs in u'ȑȁȅȉȍȕ':
                            gos3=gos2[:-3]+'nj'
                            gos4=kratkouzlazni(cs,gos2)
                    prezent1(gos2)
                    aorist3(gos3,tablica[-1][2])
                    imperfekt2(gos2,tablica[-1][2])
                    imperativ1(gos4)
                    prad7(gos3)
                    ptrpni8(gos3,tablica[-1][3])
                    psad(gos2,tablica[-1][2])
                    ppro3(gos3,tablica[-1][2])
            af.write('\n')

    ## Dvosložni 7. grupa glagola: inf. kleti, prez. n-em klêti - kùnēm
        elif infs[-5:] in u'klêti' and pres[-3:] in u'nēm' and si==2:
            for bs in gos1:
                if bs in u'ȓâêîôû':
                    gos3=kratkosilazni(bs,gos1)
            prezent1(gos2)
            aorist2(gos1,gos1,gos1,tablica[-1][2])
            imperfekt1(gos2,tablica[-1][2])
            imperativ1(gos2)
            prad1(gos1,gos3)
            ptrpni5(gos1,tablica[-1][3])
            psad(gos2,tablica[-1][2])
            ppro1(gos1,tablica[-1][2])
            af.write('\n')

    ## Dvosložni 8. grupa glagola: inf. -moći, prez. n-em smȍći - smȍgnēm
        elif infs[-4:] in u'mȍći' and pres[-3:] in u'nēm' and si==2:
            gos4=gos2[:-1]
            gos3=sibilarizacija2(gos4)
            gos5=palatalizacija2(gos4)
            prezent1(gos2)
            aorist1(gos4,gos5,tablica[-1][2])
            imperfekt1(gos3,tablica[-1][2])
            imperativ1(gos2)
            prad2(gos4)
            ptrpni7(gos2,tablica[-1][3])
            psad(gos4,tablica[-1][2])
            ppro2(gos4,tablica[-1][2])
            af.write('\n')

    ## Dvosložni 9. grupa glagola: inf. -reći, prez. n-em rèći - rȅknēm
        elif infs[-4:] in u'rèći' and pres[-3:] in u'nēm' and si==2:
            gos4=gos2[:-1]
            gos3=sibilarizacija2(gos4)
            gos5=palatalizacija2(gos4)
            for cs in gos2:
                if cs in u'ȑȁȅȉȍȕ':
                    gos6=kratkouzlazni(cs,gos4)
                    gos7=kratkouzlazni(cs,gos2)
            prezent1(gos2)
            aorist1(gos6,gos5,tablica[-1][2])
            imperfekt1(gos3,tablica[-1][2])
            imperativ1(gos7)
            prad3(gos4,gos4)
            ptrpni7(gos7,tablica[-1][3])
            psad(gos4,tablica[-1][2])
            ppro2(gos6,tablica[-1][2])
            af.write('\n')

    ## Dvosložni 10. grupa glagola: inf. -leći, prez. n-em slȅći - slȅgnēm
        elif infs[-4:] in u'lȅći' and pres[-3:] in u'nēm' and si==2:
            gos4=gos2[:-1]
            gos3=sibilarizacija2(gos4)
            gos5=palatalizacija2(gos4)
            prezent1(gos2)
            aorist1(gos4,gos5,tablica[-1][2])
            imperfekt1(gos3,tablica[-1][2])
            imperativ1(gos2)
            prad3(gos4,gos4)
            ptrpni7(gos2,tablica[-1][3])
            psad(gos4,tablica[-1][2])
            ppro2(gos4,tablica[-1][2])
            af.write('\n')

    ##  Dvosložni 11. grupa glagola: 1. sl. inf. dugosilazni, 1. sl. prez. dugosilazni (npr. drîjeti – drêm)

        elif infs[-5:] in u'îjeti' and pres[-2:] in u'êm' and si==2:
            for bs in gos1:
                if bs in u'ȓâêîôû':
                    gos3=dugouzlazni(bs,gos1)
            prezent4(gos2)
            aorist2(gos1,gos1,gos3,tablica[-1][2])
            imperfekt4(gos2,tablica[-1][2])
            imperativ4(gos2)
            gos4=naglasak_r(gos2)
            prad5(gos4,gos2)
            ptrpni5(gos4,tablica[-1][3])
            psad4(gos2,tablica[-1][2])   
            ppro1(gos1,tablica[-1][2])
            af.write('\n')
                
    ##  Dvosložni 12. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. kratkosilazni (npr. klȁti – kȍljēm)

    ##    if infs[-3:] in u'ȁti' and pres[-4:] in u'ljēm' and si==2:    --> poklapa se s 22. grupom
        elif infs[-3:] in u'ȁti' and pres[-4:] in u'ljēm' and si==2 and infs[-5:-4] not in 'sl':
            prezent1(gos2)
            aorist2(gos1,gos1,gos1,tablica[-1][2])
            imperfekt3(gos1,tablica[-1][2])
            for bs in gos2:
                if  bs in u'ȑȁȅȉȍȕ':
                    gos3=kratkouzlazni(bs,gos2)
                    imperativ1(gos3)
            prad1(gos1,gos1)
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos4=dugosilazni(bs,gos1)
                    ptrpni2(gos4,tablica[-1][3])
            psad(gos2,tablica[-1][2])
            ppro1(gos4,tablica[-1][2])
            af.write('\n')

    ##  Dvosložni 13. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. kratkosilazni (npr. smljȅti – smȅljēm)

        elif infs[-6:] in u'mljȅti' and pres[-2:] in u'ēm' and si==2:
            prezent1(gos2)
            aorist2(gos1,gos1,gos1,tablica[-1][2])
            imperfekt3(gos1,tablica[-1][2])
            for bs in gos2:
                if  bs in u'ȑȁȅȉȍȕ':
                    gos3=kratkouzlazni(bs,gos2)
                    imperativ1(gos3)
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos3=dugosilazni(bs,gos1)
                    gos4=kratkouzlazni(bs,gos1)
            prad1(gos1,gos1)
            ptrpni3(gos4,tablica[-1][3])
            psad(gos2,tablica[-1][2])
            ppro1(gos3,tablica[-1][2])
            af.write('\n')

    ##  Dvosložni 14. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. dugosilazni (npr. tȑti – tȁrēm)

        elif infs[-3:] in u'rtiȑtiŕtiȓtiŗti' and pres[-3:] in u'rēm' and si==2:
            ngos1=nenag_sam(gos1)
            prezent1(gos2)
            af.write(u'\t\t\t\t\t\t') #umjesto aorista
            imperfekt4(ngos1,tablica[-1][2])
            imperativ4(ngos1)
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos3=dugosilazni(bs,gos1)
                    prad5(gos3,ngos1)
                    ptrpni5(gos3,tablica[-1][3])
            psad(gos2,tablica[-1][2])
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos3=dugosilazni(bs,gos1)
                    ppro1(gos3,tablica[-1][2])
            af.write('\n')
                
    ##  Dvosložni 15. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. kratkosilazni (npr. pȉti – pȉjēm; čȕti – čȕjēm)

        elif infs[-3:] in u'ȉtiȕti' and pres[-3:] in u'jēm' and si==2:
            prezent1(gos2)
            for bs in gos2:
                if bs in u'ȑȁȅȉȍȕ':
                    gos3=dugosilazni(bs,gos2)
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos4=dugosilazni(bs,gos1)
                    gos5=kratkouzlazni(bs,gos1)
                    gos6=dugouzlazni(bs,gos1)
            aorist2(gos1,gos4,gos1,tablica[-1][2])
            imperfekt2(gos2,tablica[-1][2])
            imperativ2(gos3)
            prad1(gos6,gos1)
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    if infs[-3] in u'ȉ':
                        ptrpni4(gos5,tablica[-1][3])
                    elif infs[-3] in u'ȕ':
                        ptrpni3(gos5,tablica[-1][3])
            psad(gos2,tablica[-1][2])
            ppro1(gos4,tablica[-1][2])
            af.write('\n')

    ##  Dvosložni 16. grupa glagola: 1. sl. inf. dugosilazni, 1. sl. prez. dugosilazni (npr. nâći – nâđēm)

        elif infs[-2:] in u'ći' and pres[-3:] in u'đēm' and si==2:
            prezent1(gos2)
            for bs in gos2:
                if bs in u'ȓâêîôû':
                    gos3=dugouzlazni(bs,gos2)
                    aorist1(gos3,gos3,tablica[-1][2])
                    imperfekt2(gos3,tablica[-1][2])
                    imperativ1(gos3)
            for bs in gos1:
                if bs in u'ȓâêîôû':
                    gos3=kratkouzlazni(bs,gos1)
                    gos4=kratkosilazni(bs,gos1)
            prad2(gos3+u'š') 
            ptrpni(gos2,tablica[-1][3])
            psad(gos2,tablica[-1][2])
            ppro2(gos4+u'š',tablica[-1][2])
            af.write('\n')

    ##  Dvosložni 17. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. dugosilazni (npr. spȁti – spîm)

        elif infs[-3:] in u'ȁti' and pres[-2:] in u'îm' and si==2:
            prezent5(gos2)
            aorist2(gos1,gos1,gos1,tablica[-1][2])
            imperfekt3(gos1,tablica[-1][2])
            imperativ5(gos2)
            prad1(gos1,gos1)
            af.write(u'\t\t\t\t\t\t')#nedostaje pridjev trpni
            psad2(gos2,tablica[-1][2])
            ppro1(gos1,tablica[-1][2])
            af.write('\n')

    ##  Dvosložni 18. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. dugosilazni (npr. bdjȅti – bdîm)

        elif infs[-3:] in u'ȅti' and pres[-2:] in u'îm' and si==2:
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos4=dugosilazni(bs,gos1)
                    for bs in gos4:
                        if bs in u'ȓâêîôû':
                            gos5=dugouzlazni(bs,gos4)
            for bs in gos2:
                if bs in u'ȓâêîôû':
                    gos6=kratkosilazni(bs,gos2)
            prezent5(gos2)
            aorist2(gos4,gos4,gos5,tablica[-1][2])
            gos3=d_pretvorba(gos2)
            imperfekt2(gos3,tablica[-1][2])
            imperativ5(gos2)
            prad6(gos4,gos2)
            af.write(u'\t\t\t\t\t\t') #nedostaje pridjev trpni
            psad3(gos2,tablica[-1][2])
            ppro1(gos4,tablica[-1][2])
            af.write('\n')
            
    ##  Dvosložni 19. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. kratkosilazni (npr. brȁti – bȅrēm)

        elif infs[-5:] in u'brȁti' and pres[-2:] in u'ēm' and si==2:
            prezent1(gos2)
            aorist2(gos1,gos1,gos1,tablica[-1][2])
            imperfekt3(gos1,tablica[-1][2])
            for bs in gos2:
                if bs in u'ȑȁȅȉȍȕ':
                    gos3=kratkouzlazni(bs,gos2)
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos4=dugosilazni(bs,gos1)
            imperativ1(gos3)
            prad1(gos1,gos1)
            ptrpni2(gos4,tablica[-1][3])
            psad(gos3,tablica[-1][2])
            ppro1(gos4,tablica[-1][2])
            af.write('\n')
                    
    ##  Dvosložni 20. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. kratkosilazni (npr. prȁti – pȅrēm)

        elif infs[-5:] in u'prȁti' and pres[-2:] in u'ēm' and si==2:
            prezent1(gos2)
            aorist2(gos1,gos1,gos1,tablica[-1][2])
            imperfekt3(gos1,tablica[-1][2])
            for bs in gos2:
                if bs in u'ȑȁȅȉȍȕ':
                    gos3=kratkouzlazni(bs,gos2)
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos4=dugosilazni(bs,gos1)
            imperativ1(gos3)
            prad1(gos1,gos1)
            ptrpni2(gos4,tablica[-1][3])
            psad(gos3,tablica[-1][2])
            ppro1(gos4,tablica[-1][2])
            af.write('\n')
                    
    ##  Dvosložni 21. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. kratkouzlazni (npr. zvȁti – zòvēm)

        elif infs[-5:] in u'zvȁti' and pres[-2:] in u'ēm' and si==2:
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos4=kratkouzlazni(bs,gos1)
                    gos5=dugosilazni(bs,gos1)
            prezent1(gos2)
            aorist2(gos4,gos4,gos4,tablica[-1][2])
            imperfekt3(gos4,tablica[-1][2])
            imperativ1(gos2)
            prad1(gos4,gos1)
            ptrpni2(gos5,tablica[-1][3])
            psad(gos2,tablica[-1][2])
            ppro1(gos4,tablica[-1][2])
            af.write('\n')
                    
    ##  Dvosložni 22. grupa glagola: 1. sl. inf. kratkosilazni, 1. sl. prez. kratkosilazni (npr. slȁti – šȁljēm)

        elif infs[-5:] in u'slȁti' and pres[-2:] in u'ēm' and si==2:
            prezent1(gos2)
            aorist2(gos1,gos1,gos1,tablica[-1][2])
            imperfekt3(gos1,tablica[-1][2])
            for bs in gos1:
                if bs in u'ȑȁȅȉȍȕ':
                    gos3=dugosilazni(bs,gos1)
            for bs in gos2:
                if bs in u'ȑȁȅȉȍȕ':
                    gos4=kratkouzlazni(bs,gos2)
            imperativ1(gos4)
            prad1(gos1,gos1)
            ptrpni2(gos3,tablica[-1][3])
            psad(gos4,tablica[-1][2])
            ppro1(gos3,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 1. grupa glagola: inf. -sti, prez. t-em d-em
            
        elif infs[-3:] in 'sti' and pres[-3:] in u'tēmdēm' and si==3:
            ai=slog_prez(pres)
            for bs in gos2:
                #a) ìsplesti – isplètēm    
                if bs in u'àèìòùŗ' and ai==2:
                    prezent11(gos2,ngos2,gos2,kratkouzlazni1,slog3unazad)
                    aorist7(ngos2,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
                    imperfekt6(gos2,ngos2,kratkouzlazni1,slog3unazad,slog4unazad,tablica[-1][2])
                    imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2,slog3unazad)
                    prad9(gos1[:-1])
                    ptrpni12(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    psad8(ngos2,kratkouzlazni1,slog3unazad,tablica[-1][2])
                    ppro5(gos1[:-1],tablica[-1][2])
                #b) ìzrasti - izrástēm
                elif bs in u'áéíóúŕ' and ai==2:
                    prezent11(gos2,ngos2,gos2,dugouzlazni1,slog3unazad)
                    aorist7(ngos2,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
                    imperfekt7(ngos2,dugouzlazni1,slog3unazad,slog4unazad,tablica[-1][2]) 
                    imperativ7(ngos2,dugouzlazni1,dugouzlazni1,slog2,slog3unazad)
                    prad12(ngos2,gos1,kratkouzlazni1,slog1)
                    ptrpni12(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    psad8(ngos2,dugouzlazni1,slog3unazad,tablica[-1][2])
                    ppro6(ngos2,kratkouzlazni1,slog1,tablica[-1][2])
                #c) pòjesti – pòjedēm
                elif bs in u'àèìòùŗ' and ai==1:
                    prezent7(gos2)
                    aorist7(ngos2,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
                    imperfekt5(gos2,tablica[-1][2])
                    imperativ8(gos2)
                    prad9(gos1[:-1])
                    ptrpni12(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    psad5(gos2,tablica[-1][2])
                    ppro5(gos1[:-1],tablica[-1][2])
            af.write('\n')

    ##  Trosložni 2. grupa glagola: inf. -sti, prez. s-em z-em

        elif infs[-3:] in 'sti' and pres[-3:] in u'sēmzēm' and si==3:
            for bs in gos2:
                #a) nàgristi – nagrízēm  
                if bs in u'áéíóúŕ':
                    prezent11(gos2,ngos2,gos2,dugouzlazni1,slog3unazad)
                    aorist7(ngos2,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
                    af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
                    imperativ7(ngos2,dugouzlazni1,dugouzlazni1,slog2,slog3unazad)
                    prad13(ngos2,kratkouzlazni1,slog1)
                    ptrpni12(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    af.write(u'\t') #nedostaje prilog sadašnji
                    ppro6(ngos2,kratkouzlazni1,slog1,tablica[-1][2])
                #b) ìzvesti – izvèzēm  
                elif bs in u'àèìòùŗ':
                    prezent11(gos2,ngos2,gos2,kratkouzlazni1,slog3unazad)
                    aorist7(ngos2,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
                    af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
                    imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
                    prad13(ngos2,kratkouzlazni1,slog1)
                    ptrpni12(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    af.write(u'\t') #nedostaje prilog sadašnji
                    ppro6(ngos2,kratkouzlazni1,slog1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 3. grupa glagola: inf. -sti, prez. b-em p-em

        elif infs[-3:] in 'sti' and pres[-3:] in u'bēmpēm' and si==3:
            for bs in gos2:
                #a) ìzgrepsti – izgrèbēm
                if bs in u'ŗàèìòù':
                    prezent11(gos2,ngos2,gos2,kratkouzlazni1,slog3unazad)
                    aorist7(ngos2,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
                    af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
                    imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2,slog3unazad)
                    prad13(ngos2,kratkouzlazni1,slog1)
                    ptrpni12(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    af.write(u'\t') #nedostaje prilog sadašnji
                    ppro6(ngos2,kratkouzlazni1,slog1,tablica[-1][2])
                #b) ìscrpsti – iscŕpēm  
                elif bs in u'ŕáéíóú':
                    prezent11(gos2,ngos2,gos2,dugouzlazni1,slog3unazad)
                    aorist7(ngos2,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
                    af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
                    imperativ7(ngos2,dugouzlazni1,dugouzlazni1,slog2,slog3unazad)
                    prad13(ngos2,kratkouzlazni1,slog1)
                    ptrpni12(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    af.write(u'\t') #nedostaje prilog sadašnji
                    ppro6(ngos2,kratkouzlazni1,slog1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 4. grupa glagola: inf. -ći, prez. č-em ž-em š-em
                    
        elif infs[-2:] in u'ći' and pres[-3:] in u'čēmžēmšēm' and si==3:
            for bs in gos2:
                #a) ìspeći – ispèčēm
                if bs in u'ŗàèìòù':
                    gos3=krati(gos2)
                    gos4=palatalizacija(gos3)
                    ngos4=nenag_sam(gos4)
                    gos5=sibilarizacija(gos2)
                    ngos5=nenag_sam(gos5)
                    prezent11(gos2,ngos2,gos4,kratkouzlazni1,slog3unazad)
                    aorist8(ngos4,ngos2,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
                    af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
                    imperativ7(ngos5,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
                    prad13(ngos4,kratkouzlazni1,slog1)
                    ptrpni12(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    psad5(gos4,tablica[-1][2])
                    ppro6(ngos4,kratkouzlazni1,slog1,tablica[-1][2])
                #b) pòsjeći – posjéčēm / ràzvući – razvúčēm
                elif bs in u'ŕáéíóú':
                    gos3=krati(gos2)
                    ngos3=nenag_sam(gos3)
                    gos4=palatalizacija(gos3)
                    ngos4=nenag_sam(gos4)
                    gos5=sibilarizacija(gos2) #samo sibilarizacija, bez kraćenja
                    ngos5=nenag_sam(gos5)
                    gos6=palatalizacija(gos2) #samo palatalizacija, bez kraćenja
                    gos7=sibilarizacija(gos3)
                    prezent11(gos2,ngos2,gos6,dugouzlazni1,slog3unazad)
                    aorist8(ngos4,ngos3,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
                    imperfekt8(gos7,tablica[-1][2])
                    imperativ7(ngos5,dugouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
                    prad13(ngos4,kratkouzlazni1,slog1)
                    ptrpni12(ngos3,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    psad5(gos6,tablica[-1][2])
                    ppro6(ngos4,kratkouzlazni1,slog1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 5. grupa glagola: inf. -ati/-eti/-uti, prez. n-em m-em p-em

        elif infs[-3:] in 'atietiuti' and pres[-3:] in u'nēmmēmpēm' and si==3:
            for bs in gos1:
                for cs in gos2:
                    #a) òteti – ȍtmēm / pòpeti - pȍpnēm / sàžeti - sȁžmēm
                    if bs in u'ŗàèìòù' and cs in u'ȑȁȅȉȍȕ':
                        for ds in gos1:
                            if ds in u'ŗàèìòù':
                                gos3=kratkosilazni(ds,gos1)
                        for ds in gos2:
                            if ds in u'ȑȁȅȉȍȕ':
                                gos4=kratkouzlazni(ds,gos2)
                        prezent7(gos2)
                        aorist6(gos3,gos3,tablica[-1][2])
                        af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
                        imperativ8(gos4)
                        prad9(gos3)
                        ptrpni13(gos3,tablica[-1][3])
                        af.write(u'\t') #nedostaje prilog sadašnji
                        ppro5(gos1,tablica[-1][2])
                    #b) béknuti – bêknēm
                    elif bs in u'ŕáéíóú' and cs in u'ȓâêîôû':
                        prezent7(gos2)
                        for cs in gos1:
                            if cs in u'ŕáéíóú':
                                gos3=dugosilazni(cs,gos1)
                                gos4=kratkosilazni(cs,gos1)
                        aorist6(gos3,gos4,tablica[-1][2])
                        af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
                        for cs in gos2:
                            if cs in u'ȓâêîôû':
                                gos5=dugouzlazni(cs,gos2)
                        imperativ8(gos5)
                        prad9(gos1)
                        ptrpni13(gos3,tablica[-1][3])
                        af.write(u'\t') #nedostaje prilog sadašnji
                        ppro5(gos1,tablica[-1][2])
                    #c) prȁsnuti – prȁsnēm
                    elif bs in u'ȑȁȅȉȍȕ' and cs in u'ȑȁȅȉȍȕ':
                        prezent7(gos2)
                        aorist6(gos1,gos1,tablica[-1][2])
                        af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
                        imperativ8(gos2)
                        prad9(gos1)
                        ptrpni13(gos1,tablica[-1][3])
                        af.write(u'\t') #nedostaje prilog sadašnji
                        ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 6. grupa glagola: inf. -kleti, prez. n-em (npr. pròkleti – prokùnēm)

        elif infs[-5:] in 'kleti' and pres[-3:] in u'nēm' and si==3:
            prezent11(gos2,ngos2,gos2,kratkouzlazni1,slog3unazad)
            aorist9(ngos1,ngos1,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
            imperfekt8(gos2,tablica[-1][2])
            imperativ8(gos2)
            for cs in gos1:
                if cs in u'ŗàèìòù':
                    gos3=kratkosilazni(cs,gos1)
            prad9(gos3)
            ptrpni13(gos3,tablica[-1][3])
            psad5(gos2,tablica[-1][2])
            ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 7. grupa glagola: inf. -moći, prez. n-em (npr. pòmoći – pòmognēm)

        elif infs[-4:] in u'moći' and pres[-3:] in u'nēm' and si==3:
            prezent7(gos2)
            gos5=pres[:-3]
            ngos5=nenag_sam(gos5)
            gos3=palatalizacija2(gos5)
            ngos3=nenag_sam(gos3)
            aorist8(ngos5,ngos3,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
            gos4=sibilarizacija2(gos5)
            imperfekt8(gos4,tablica[-1][2])
            imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
            prad8(gos5)
            ptrpni10(gos2,tablica[-1][3])
            psad5(gos5,tablica[-1][2])
            ppro4(gos5,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 8. grupa glagola: inf. -reći, prez. n-em (npr. ìzreći – ìzreknēm)

        elif infs[-4:] in u'reći' and pres[-3:] in u'nēm' and si==3:
            prezent7(gos2)
            gos3=pres[:-3]
            ngos3=nenag_sam(gos3)
            gos4=palatalizacija2(gos3)
            ngos4=nenag_sam(gos4)
            aorist8(ngos3,ngos4,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
            gos5=sibilarizacija2(gos3)
            ngos5=nenag_sam(gos5)
            imperativ7(ngos5,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
            prad8(gos3)
            ptrpni14(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
            af.write(u'\t') #nedostaje prilog sadašnji
            ppro4(gos3,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 9. grupa glagola: inf. -leći, prez. n-em (npr. pòleći – pòlegnēm)

        elif infs[-4:] in u'leći' and pres[-3:] in u'nēm' and si==3:
            prezent7(gos2)
            gos3=pres[:-3]
            ngos3=nenag_sam(gos3)
            gos4=palatalizacija2(gos3)
            ngos4=nenag_sam(gos4)
            aorist8(ngos3,ngos4,slog1,kratkouzlazni1,kratkosilazni1,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
            gos5=sibilarizacija2(gos3)
            ngos5=nenag_sam(gos5)
            imperativ7(ngos5,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
            prad8(gos3)
            ptrpni14(ngos2,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
            af.write(u'\t') #nedostaje prilog sadašnji
            ppro4(gos3,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 10. grupa glagola: inf. -rijeti, prez. r-em (npr. ùprijeti – ȕprēm / nàzreti – nȁzrēm / pròdrijeti – prȍdrēm)

        elif infs[-6:] in u'rijeti' and pres[-3:] in u'rēm' and si==3:
            prezent7(gos2)
            aorist10(gos2,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
            for bs in gos2:
                if bs in u'ȑȁȅȉȍȕ':
                    gos3=kratkouzlazni(bs,gos2)
            imperativ8(gos3)
            prad9(gos2)
            ptrpni15(gos2,tablica[-1][3])
            af.write(u'\t') #nedostaje prilog sadašnji
            ppro5(gos3,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 10. grupa glagola: inf. -eti, prez. r-em (npr. ùprijeti – ȕprēm / nàzreti – nȁzrēm / pròdrijeti – prȍdrēm)

        elif infs[-3:] in u'eti' and pres[-3:] in u'rēm' and si==3 and infs[-6:-4:] not in 'rij':
            prezent7(gos2)
            aorist10(gos2,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') #nedostaje imperfekt
            for bs in gos2:
                if bs in u'ȑȁȅȉȍȕ':
                    gos3=kratkouzlazni(bs,gos2)
            imperativ8(gos3)
            prad9(gos2)
            ptrpni15(gos2,tablica[-1][3])
            af.write(u'\t') #nedostaje prilog sadašnji
            ppro5(gos3,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 11. grupa glagola: inf. -ati, prez. lj-em (npr. škàkljati – škàkljēm)

        elif infs[-3:] in u'ati' and pres[-4:] in u'ljēm' and infs[-5] not in 'k' and infs[-5:-4] not in 'sl' and si==3:
            prezent7(gos2)
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
            aorist6(gos1,gos3,tablica[-1][2])
            imperfekt9(gos1,tablica[-1][2])
            imperativ8(gos2)
            prad9(gos1)
            ptrpni11(gos1,tablica[-1][3])
            psad5(gos2,tablica[-1][2])
            ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 12. grupa glagola: inf. -klati, prez. -em (npr. pòklati – pòkoljēm)

        elif infs[-5:] in u'klati' and pres[-2:] in u'ēm' and si==3:
            prezent7(gos2)
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
            aorist6(gos1,gos3,tablica[-1][2])
            imperfekt9(gos1,tablica[-1][2])
            imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
            prad9(gos1)
            ptrpni11(gos3,tablica[-1][3])
            psad5(gos2,tablica[-1][2])
            ppro5(gos1,tablica[-1][2])
            af.write('\n')   
                  
    ##  Trosložni 13. grupa glagola: inf. -mljeti, prez. -em (npr. sàmljeti – sàmeljēm)

        elif infs[-6:] in u'mljeti' and pres[-2:] in u'ēm' and si==3:
            prezent7(gos2)
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
            aorist6(gos1,gos3,tablica[-1][2])
            imperfekt9(gos1,tablica[-1][2])
            imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
            prad9(gos1)
            ptrpni16(ngos1,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
            psad5(gos2,tablica[-1][2])
            ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 14. grupa glagola: inf. -trti, prez. -em (npr. sàtrti – sȁtrēm)

        elif infs[-4:] in u'trti' and pres[-2:] in u'ēm' and si==3:
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
            for cs in gos2:
                if cs in u'ȑȁȅȉȍȕ':
                    gos4=kratkouzlazni(cs,gos2)
            prezent7(gos2)
            aorist11(gos3,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt()
            imperativ8(gos4)
            prad9(gos3)
            ptrpni17(ngos1,kratkouzlazni1,slog1,slog1,tablica[-1][3])
            af.write(u'\t') ## nedostaje psad()
            ppro5(gos4,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 15. grupa glagola: inf. -brati, prez. -em (npr. ùbrati – ùberēm)

        elif infs[-5:] in u'brati' and pres[-2:] in u'ēm' and si==3:
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
            prezent7(gos2)
            aorist6(gos1,gos3,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt()
            imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
            prad9(gos3)
            ptrpni11(gos3,tablica[-1][3])
            af.write(u'\t') ## nedostaje psad()
            ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 16. grupa glagola: inf. -prati, prez. -em (npr. òprati – òperēm)

        elif infs[-5:] in u'prati' and pres[-2:] in u'ēm' and si==3:
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
            prezent7(gos2)
            aorist6(gos1,gos3,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt()
            imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
            prad9(gos3)
            ptrpni11(gos3,tablica[-1][3])
            af.write(u'\t') ## nedostaje psad()
            ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 17. grupa glagola: inf. -zvati, prez. -em (npr. nàzvati – nazòvēm)

        elif infs[-5:] in u'zvati' and pres[-2:] in u'ēm' and si==3:
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
            prezent7(gos2)
            aorist6(gos1,gos3,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt()
            imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
            prad9(gos3)
            ptrpni11(gos3,tablica[-1][3])
            af.write(u'\t') ## nedostaje psad()
            ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 18. grupa glagola: inf. -slati, prez. -em (npr. pòslati – pòšaljēm)

        elif infs[-5:] in u'slati' and pres[-2:] in u'ēm' and si==3:
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
            prezent7(gos2)
            aorist6(gos1,gos3,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt()
            imperativ7(ngos2,kratkouzlazni1,kratkouzlazni1,slog2unazad,slog3unazad)
            prad9(gos1)
            ptrpni11(gos3,tablica[-1][3])
            af.write(u'\t') ## nedostaje psad()
            ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 19. grupa glagola: inf. -eti, prez. -em (npr. pròbdjeti – pròbdīm)

        elif infs[-4:] in u'jeti' and pres[-2:] in u'īm' and infs[-5] not in 'l' and si==3:
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
                    prezent8(gos2)
                    aorist6(gos1,gos3,tablica[-1][2])
                    af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt()
                    imperativ10(gos2)
                    prad10(gos2,gos1)
                    ptrpni16(ngos1,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    psad6(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## 24. grupa b) vȉdjeti - vȉdīm
                elif bs in u'ȑȁȅȉȍȕ':
                    gos3=jotacija(gos2)
                    prezent9(gos2)
                    aorist6(gos1,gos1,tablica[-1][2])
                    imperfekt5(gos3,tablica[-1][2])
                    imperativ8(gos2)
                    prad10(gos2,gos1)
                    ptrpni9(gos3,tablica[-1][3])
                    af.write(u'\t') ## nedostaje psad
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 20. grupa glagola: inf. -iti/uti, prez. -jem/ujem (npr. pròbdjeti – pròbdīm)

        elif infs[-3:] in u'itiutieti' and pres[-3:] in u'jēm' or pres[-4:] in u'ujēm' and si==3:
            for bs in gos2:
                #a) òbuti – ȍbujēm / ràzbiti - rȁzbijēm
                if bs in u'ȑȁȅȉȍȕ':
                    for cs in gos2:
                        if cs in u'ȑȁȅȉȍȕ':
                            gos3=kratkouzlazni(cs,gos2)
                    for ds in gos1:
                        if ds in u'ŗàèìòù':
                            gos4=kratkosilazni(ds,gos1)
                    prezent7(gos2)
                    aorist6(gos4,gos4,tablica[-1][2])
                    af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt()
                    imperativ11(gos3)
                    prad9(gos1)
                    ptrpni16(ngos1,kratkouzlazni1,slog3unazad,slog2unazad,tablica[-1][3])
                    af.write(u'\t') ## nedostaje psad()
                    ppro5(gos1,tablica[-1][2])
                #b) ùmjeti – ùmijēm ili ?ùmiti – ùmijēm/ dòčuti - dòčujēm    
                elif bs in u'ŗàèìòù':
                    for ds in gos1:
                        if ds in u'ŗàèìòù':
                            gos3=kratkosilazni(ds,gos1)
                    prezent7(gos2)
                    aorist6(gos1,gos3,tablica[-1][2])
                    af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt()
                    imperativ11(gos2)
                    prad9(gos1)
                    ptrpni16(ngos1,kratkouzlazni1,slog1,slog1,tablica[-1][3])
                    af.write(u'\t') ## nedostaje psad()
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')
            
    ##  Trosložni 21. grupa glagola: inf. -ići, prez. -đem (npr. nàīći - nàīđēm)

        elif infs[-3:] in u'īći' and pres[-3:] in u'đēm' and si==3:
            prezent7(gos2)
            for cs in gos2:
                if cs in u'ŗàèìòù':
                    gos3=kratkosilazni(cs,gos2)
                    aorist4(gos2,gos3,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt()
            imperativ7(ngos2,dugouzlazni1,dugouzlazni1,slog2unazad,slog3unazad)
            gos4=gos1+u'š'
            prad8(gos4)
            ptrpni9(gos2,tablica[-1][3])
            af.write(u'\t') ## nedostaje psad()
            ppro4(gos4,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 22. grupa glagola: inf. -spati, prez. -im (npr. zàspati - zàspīm)

        elif infs[-5:] in 'spati' and pres[-4:] in u'spīm' and si==3:
            prezent8(gos2)
            for cs in gos2:
                if cs in u'ŗàèìòù':
                    gos3=kratkosilazni(cs,gos2)
            aorist5(gos2,gos3,tablica[-1][2])
            af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt
            imperativ8(gos2)
            prad11(gos3)
            af.write(u'\t\t\t\t\t\t') ## nedostaje ptrpni()
            af.write(u'\t') ## nedostaje psad()
            ppro4(gos2,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 23. grupa glagola: inf. -nuti, prez. -nem

        elif infs[-4:] in 'nuti' and pres[-3:] in u'nēm' and si==3:
            for bs in gos1: 
                ## a) dȉgnuti - dȉgnēm
    ##            if bs in u'ȑȁȅȉȍȕ':
    ##                prezent7(gos2)
    ##                aorist6(gos1,gos1,tablica[-1][2])
    ##                af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt
    ##                imperativ8(gos2)
    ##                prad9(gos1)
    ##                ptrpni10(gos2,tablica[-1][3])
    ##                af.write(u'\t') ## nedostaje psad
    ##                ppro5(gos1,tablica[-1][2])
                ## b) vènuti - vȅnēm
                if bs in u'àèìòù':
                    gos3=kratkosilazni(bs,gos1)
                    prezent7(gos2)
                    aorist6(gos3,gos3,tablica[-1][2])
                    af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt
                    imperativ8(gos2)
                    prad9(gos3)
                    ptrpni10(gos2,tablica[-1][3])
                    af.write(u'\t') ## nedostaje psad
                    ppro5(gos3,tablica[-1][2])
            af.write('\n')
                ## c) víknuti - vîknēm
    ##            elif bs in u'ŕáéíóú':
    ##                for cs in gos2:
    ##                    if cs in u'ȓâêîôû':
    ##                        gos3=dugouzlazni(cs,gos2)
    ##                gos4=dugosilazni(bs,gos1)
    ##                gos5=kratkosilazni(bs,gos1)
    ##                prezent7(gos2)
    ##                aorist6(gos4,gos5,tablica[-1][2])
    ##                af.write(u'\t\t\t\t\t\t') ## nedostaje imperfekt
    ##                imperativ8(gos3)
    ##                prad9(gos1)
    ##                ptrpni10(gos2,tablica[-1][3])
    ##                af.write(u'\t') ## nedostaje psad
    ##                ppro5(gos1,tablica[-1][2])

    ##  Trosložni 24. grupa glagola: inf. (j,lj,nj,r)-eti, prez. (d,l,n,r)-im

        elif infs[-4:] in 'jetireti' and pres[-3:] in u'dīmlīmnīmrīm' and si==3:
            for bs in gos1: 
                ## a) žèljeti - žèlīm i c) vòljeti - vȍlīm
                if bs in u'ŗàèìòù' and infs[-5] not in 'd':
                    for cs in gos2:
                        if cs in u'ŗàèìòù':
                            gos3=jotacija(gos2)
                            gos4=kratkosilazni(bs,gos1)
                            gos5=kratkosilazni(cs,gos3)
                            prezent9(gos2)
                            aorist6(gos1,gos4,tablica[-1][2])
                            imperfekt5(gos3,tablica[-1][2])
                            imperativ8(gos2)
                            prad10(gos2,gos1)
                            ptrpni9(gos5,tablica[-1][3])
                            af.write(u'\t') ## nedostaje psad
                            ppro5(gos1,tablica[-1][2])
                        elif cs in u'ȑȁȅȉȍȕ':
                            gos3=jotacija(gos2)
                            gos4=kratkosilazni(bs,gos1)
                            gos5=kratkouzlazni(cs,gos2)
                            prezent9(gos2)
                            aorist6(gos4,gos4,tablica[-1][2])
                            imperfekt5(gos3,tablica[-1][2])
                            imperativ8(gos5)
                            prad10(gos5,gos1)
                            ptrpni9(gos3,tablica[-1][3])
                            af.write(u'\t') ## nedostaje psad
                            ppro5(gos1,tablica[-1][2])
                ## b) vȉdjeti - vȉdīm
##                elif bs in u'ȑȁȅȉȍȕ':
##                    gos3=jotacija(gos2)
##                    prezent9(gos2)
##                    aorist6(gos1,gos1,tablica[-1][2])
##                    imperfekt5(gos3,tablica[-1][2])
##                    imperativ8(gos2)
##                    prad10(gos2,gos1)
##                    ptrpni9(gos3,tablica[-1][3])
##                    af.write(u'\t') ## nedostaje psad
##                    ppro5(gos1,tablica[-1][2])
                ## d) cvíljeti - cvílīm
                elif bs in u'ŕáéíóú':
                    gos3=jotacija(gos2)
                    gos4=kratkosilazni(bs,gos1)
                    prezent9(gos2)
                    aorist6(gos1,gos4,tablica[-1][2])
                    imperfekt5(gos3,tablica[-1][2])
                    imperativ8(gos2)
                    prad10(gos2,gos1)
                    ptrpni9(gos3,tablica[-1][3])
                    af.write(u'\t') ## nedostaje psad
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 25. grupa glagola: inf. (č,ž,j,št,žd)-ati, prez. -im

        elif infs[-4:] in u'čatižatijatitatižati' and pres[-2:] in u'īm' and si==3:
            for bs in gos1: 
                if bs in u'ŗàèìòù':
                    for cs in gos2:
                        ## a) dŗžati - dŗžīm
                        if cs in u'ŗàèìòù':
                            gos3=kratkosilazni(bs,gos1)
                            prezent9(gos2)
                            aorist6(gos1,gos3,tablica[-1][2])
                            imperfekt5(gos2,tablica[-1][2])
                            imperativ8(gos2)
                            prad9(gos1)
                            ptrpni11(gos3,tablica[-1][3])
                            af.write(u'\t') ## nedostaje psad
                            ppro5(gos1,tablica[-1][2])
                        ## c) cìčati - cíčīm
                        elif cs in u'ŕáéíóú':
                            gos3=dugouzlazni(bs,gos1)
                            gos4=kratkosilazni(bs,gos1)
                            prezent9(gos2)
                            aorist6(gos3,gos4,tablica[-1][2])
                            imperfekt5(gos2,tablica[-1][2])
                            imperativ8(gos2)
                            prad9(gos3)
                            ptrpni11(gos3,tablica[-1][3])
                            af.write(u'\t') ## nedostaje psad
                            ppro5(gos3,tablica[-1][2])
                ## b) čúčati - čúčīm
                elif bs in u'ŕáéíóú':
                    gos3=kratkosilazni(bs,gos1)
                    prezent9(gos2)
                    aorist6(gos1,gos3,tablica[-1][2])
                    imperfekt5(gos2,tablica[-1][2])
                    imperativ8(gos2)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    af.write(u'\t') ## nedostaje psad
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 26. grupa glagola: inf. -iti, prez. -im

        elif infs[-3:] in 'iti' and pres[-2:] in u'īm' and si==3:
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    for cs in gos2:
                        ## a) vòziti - vȍzīm
                        if cs in u'ȑȁȅȉȍȕ':
                            gos3=jotacija(gos2)
                            gos4=kratkosilazni(bs,gos1)
                            gos5=kratkouzlazni(cs,gos2)
                            prezent9(gos2)
                            aorist6(gos4,gos4,tablica[-1][2])
                            imperfekt5(gos3,tablica[-1][2])
                            imperativ8(gos5)
                            prad9(gos1)
                            ptrpni9(gos3,tablica[-1][3])
                            psad6(gos2,tablica[-1][2])
                            ppro5(gos1,tablica[-1][2])
                        ## f) bròjiti - bròjīm
                        elif cs in u'ŗàèìòù':
                            gos3=jotacija(gos2)
                            gos4=kratkosilazni(bs,gos1)
                            prezent9(gos2)
                            aorist6(gos1,gos4,tablica[-1][2])
                            imperfekt5(gos3,tablica[-1][2])
                            imperativ8(gos2)
                            prad9(gos1)
                            ptrpni9(gos3,tablica[-1][3])
                            psad6(gos2,tablica[-1][2])
                            ppro5(gos1,tablica[-1][2])
                ## b) brȁšniti - brȁšnīm
                elif bs in u'ȑȁȅȉȍȕ':
                    gos3=jotacija(gos2)
                    prezent9(gos2)
                    aorist6(gos1,gos1,tablica[-1][2])
                    imperfekt5(gos3,tablica[-1][2])
                    imperativ8(gos2)
                    prad9(gos1)
                    ptrpni9(gos3,tablica[-1][3])
                    psad6(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                elif bs in u'ŕáéíóú':
                    for cs in gos2:
                        ## c) ljúbiti - ljûbīm
                        if cs in u'ȓâêîôû':
                            gos3=jotacija(gos2)
                            gos4=dugosilazni(bs,gos1)
                            gos5=dugouzlazni(cs,gos2)
                            gos6=kratkosilazni(bs,gos1)
                            prezent9(gos2)
                            aorist6(gos4,gos6,tablica[-1][2])
                            imperfekt5(gos3,tablica[-1][2])
                            imperativ8(gos5)
                            prad9(gos1)
                            ptrpni9(gos3,tablica[-1][3])
                            psad6(gos5,tablica[-1][2])
                            ppro5(gos1,tablica[-1][2])
                        ## d) žúriti - žúrīm
                        elif cs in u'ŕáéíóú':
                            gos3=jotacija(gos2)
                            gos4=kratkosilazni(bs,gos1)
                            prezent9(gos2)
                            aorist6(gos1,gos4,tablica[-1][2])
                            imperfekt5(gos3,tablica[-1][2])
                            imperativ8(gos2)
                            prad9(gos1)
                            ptrpni9(gos3,tablica[-1][3])
                            psad6(gos2,tablica[-1][2])
                            ppro5(gos1,tablica[-1][2])
                ## e) bânčiti - bânčīm
                elif bs in u'ȓâêîôû':
                    gos3=jotacija(gos2)
                    gos4=kratkosilazni(bs,gos1)
                    prezent9(gos2)
                    aorist6(gos1,gos4,tablica[-1][2])
                    imperfekt5(gos3,tablica[-1][2])
                    imperativ8(gos2)
                    prad9(gos1)
                    ptrpni9(gos3,tablica[-1][3])
                    psad6(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 27. grupa glagola: inf. -ijevati, prez. -am (ijevati i ati)

        elif infs[-7:] in u'ijévatiijèvatiijȅvatiijêvati' and pres[-2:] in u'ām' and si==3:
            for bs in gos1:
                ## a) pítati - pîtām
                if bs in u'ŕáéíóú':
                    gos3=dugosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȓâêîôû':
                            gos4=dugouzlazni(cs,gos2)
                    gos5=kratkosilazni(bs,gos1)
                    prezent10(gos2)
                    aorist6(gos3,gos5,tablica[-1][2])
                    imperfekt5(gos2,tablica[-1][2])
                    imperativ9(gos4)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad7(gos4,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## b) jàčati - jàčām
                elif bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
                    prezent10(gos2)
                    aorist6(gos1,gos3,tablica[-1][2])
                    imperfekt5(gos2,tablica[-1][2])
                    imperativ9(gos2)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad7(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## c) kȕhati - kȕhām
                elif bs in u'ȑȁȅȉȍȕ':
                    prezent10(gos2)
                    aorist6(gos1,gos1,tablica[-1][2])
                    imperfekt5(gos2,tablica[-1][2])
                    imperativ9(gos2)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad7(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 27. grupa glagola: inf. -ati, prez. -am (ijevati i ati)

        elif infs[-3:] in 'ati' and pres[-2:] in u'ām' and si==3:
            for bs in gos1:
                ## a) pítati - pîtām
                if bs in u'ŕáéíóú':
                    gos3=dugosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȓâêîôû':
                            gos4=dugouzlazni(cs,gos2)
                    gos5=kratkosilazni(bs,gos1)
                    prezent10(gos2)
                    aorist6(gos3,gos5,tablica[-1][2])
                    imperfekt5(gos2,tablica[-1][2])
                    imperativ9(gos4)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad7(gos4,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## b) jàčati - jàčām
                elif bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
                    prezent10(gos2)
                    aorist6(gos1,gos3,tablica[-1][2])
                    imperfekt5(gos2,tablica[-1][2])
                    imperativ9(gos2)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad7(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## c) kȕhati - kȕhām
                elif bs in u'ȑȁȅȉȍȕ':
                    prezent10(gos2)
                    aorist6(gos1,gos1,tablica[-1][2])
                    imperfekt5(gos2,tablica[-1][2])
                    imperativ9(gos2)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad7(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 28. grupa glagola: inf. -ati, prez. -em (đ,ć,ž,š,č)

        elif infs[-3:] in 'ati' and pres[-3:] in u'đēmćēmžēmšēmčēm' and si==3:
            for bs in gos1:
                ## a) písati - pîšēm
                if bs in u'ŕáéíóú':
                    gos3=dugosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȓâêîôû':
                            gos4=dugouzlazni(cs,gos2)
                    gos5=kratkosilazni(bs,gos1)
                    prezent7(gos2)
                    aorist6(gos3,gos5,tablica[-1][2])
                    gos6=gos3[:-1]
                    imperfekt5(gos6,tablica[-1][2])
                    imperativ8(gos4)
                    prad9(gos1)
                    ptrpni11(gos3,tablica[-1][3])
                    psad5(gos4,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## b) mètati - mȅćēm
                elif bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȑȁȅȉȍȕ':
                            gos4=kratkouzlazni(cs,gos2)
                    prezent7(gos2)
                    aorist6(gos3,gos3,tablica[-1][2])
                    gos5=gos3[:-1]
                    imperfekt5(gos5,tablica[-1][2])
                    imperativ8(gos4)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad5(gos4,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## c) mȉcati - mȉčēm
                elif bs in u'ȑȁȅȉȍȕ':
                    prezent7(gos2)
                    aorist6(gos1,gos1,tablica[-1][2])
                    gos3=gos1[:-1]
                    imperfekt5(gos3,tablica[-1][2])
                    imperativ8(gos2)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad5(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 28. grupa glagola: inf. -ati, prez. -em (št)

        elif infs[-3:] in 'ati' and pres[-4:] in u'štēm' and si==3:
            for bs in gos1:
                ## a) písati - pîšēm
                if bs in u'ŕáéíóú':
                    gos3=dugosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȓâêîôû':
                            gos4=dugouzlazni(cs,gos2)
                    gos5=kratkosilazni(bs,gos1)
                    prezent7(gos2)
                    aorist6(gos3,gos5,tablica[-1][2])
                    gos6=gos3[:-1]
                    imperfekt5(gos6,tablica[-1][2])
                    imperativ8(gos4)
                    prad9(gos1)
                    ptrpni11(gos3,tablica[-1][3])
                    psad5(gos4,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## b) mètati - mȅćēm
                elif bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȑȁȅȉȍȕ':
                            gos4=kratkouzlazni(cs,gos2)
                    prezent7(gos2)
                    aorist6(gos3,gos3,tablica[-1][2])
                    gos5=gos3[:-1]
                    imperfekt5(gos5,tablica[-1][2])
                    imperativ8(gos4)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad5(gos4,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## c) mȉcati - mȉčēm
                elif bs in u'ȑȁȅȉȍȕ':
                    prezent7(gos2)
                    aorist6(gos1,gos1,tablica[-1][2])
                    gos3=gos1[:-1]
                    imperfekt5(gos3,tablica[-1][2])
                    imperativ8(gos2)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad5(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 28. grupa glagola: inf. -ati, prez. -em (blj,plj,mlj,vlj)

        elif infs[-3:] in 'ati' and pres[-5:] in u'bljēmpljēmmljēmvljēm' and si==3:
            for bs in gos1:
                ## a) písati - pîšēm
                if bs in u'ŕáéíóú':
                    gos3=dugosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȓâêîôû':
                            gos4=dugouzlazni(cs,gos2)
                    gos5=kratkosilazni(bs,gos1)
                    prezent7(gos2)
                    aorist6(gos3,gos5,tablica[-1][2])
                    gos6=gos3[:-1]
                    imperfekt5(gos6,tablica[-1][2])
                    imperativ8(gos4)
                    prad9(gos1)
                    ptrpni11(gos3,tablica[-1][3])
                    psad5(gos4,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## b) mètati - mȅćēm
                elif bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȑȁȅȉȍȕ':
                            gos4=kratkouzlazni(cs,gos2)
                    prezent7(gos2)
                    aorist6(gos3,gos3,tablica[-1][2])
                    gos5=gos3[:-1]
                    imperfekt5(gos5,tablica[-1][2])
                    imperativ8(gos4)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad5(gos4,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## c) mȉcati - mȉčēm
                elif bs in u'ȑȁȅȉȍȕ':
                    prezent7(gos2)
                    aorist6(gos1,gos1,tablica[-1][2])
                    gos3=gos1[:-1]
                    imperfekt5(gos3,tablica[-1][2])
                    imperativ8(gos2)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad5(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 29. grupa glagola: inf. -ati, prez. -em

        elif infs[-3:] in 'ati' and pres[-2:] in u'ēm' and pres[-3:] not in u'jēm' and infs[-5:-4] not in 'brprzv' and si==3:
            for bs in gos1:
                if bs in u'ŗàèìòù':
                    for cs in gos2:
                        ## a) òrati - ȍrēm
                        if cs in u'ȑȁȅȉȍȕ':            
                            gos3=kratkosilazni(bs,gos1)
                            gos4=kratkouzlazni(cs,gos2)
                            prezent7(gos2)
                            aorist6(gos3,gos3,tablica[-1][2])
                            gos5=gos3[:-1]
                            imperfekt5(gos5,tablica[-1][2])
                            imperativ8(gos4)
                            prad9(gos3)
                            ptrpni11(gos3,tablica[-1][3])
                            psad5(gos2,tablica[-1][2])
                            ppro5(gos3,tablica[-1][2])
                        ## b) rèvati - rèvēm
                        elif cs in u'ŗàèìòù':
                            gos3=kratkosilazni(bs,gos1)
                            prezent7(gos2)
                            aorist6(gos1,gos3,tablica[-1][2])
                            gos4=gos1[:-1]
                            imperfekt5(gos4,tablica[-1][2])
                            imperativ8(gos2)
                            prad9(gos3)
                            ptrpni11(gos3,tablica[-1][3])
                            psad5(gos2,tablica[-1][2])
                            ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 30. grupa glagola: inf. -jati,vati prez. -jem

        elif infs[-4:] in 'jativati' and pres[-3:] in u'jēm' and pres[-4:] not in u'ȕjēm' and infs[-5] not in 'l' and si==3:
            for bs in gos1:
                ## c) grȉjati - grȉjēm
                if bs in u'ȑȁȅȉȍȕ':
                    prezent7(gos2)
                    aorist6(gos1,gos1,tablica[-1][2])
                    gos3=gos1[:-1]
                    imperfekt5(gos3,tablica[-1][2])
                    imperativ11(gos2)
                    prad9(gos1)
                    ptrpni11(gos1,tablica[-1][3])
                    psad5(gos2,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## b) dávati - dâjēm
                elif bs in u'ŕáéíóú':
                    gos3=dugosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȓâêîôû':
                            gos4=dugouzlazni(cs,gos2)
                    gos5=kratkosilazni(bs,gos1)
                    prezent7(gos2)
                    aorist6(gos3,gos5,tablica[-1][2])
                    gos6=gos3[:-1]
                    imperfekt5(gos6,tablica[-1][2])
                    imperativ11(gos4)
                    prad9(gos1)
                    ptrpni11(gos3,tablica[-1][3])
                    psad5(gos4,tablica[-1][2])
                    ppro5(gos1,tablica[-1][2])
                ## c) pòjati - pòjēm
                elif bs in u'ŗàèìòù':
                    for cs in gos2:
                        if cs in u'ŗàèìòù':
                            gos3=kratkosilazni(bs,gos1)
                            prezent7(gos2)
                            aorist6(gos1,gos3,tablica[-1][2])
                            gos4=gos1[:-1]
                            imperfekt5(gos4,tablica[-1][2])
                            imperativ11(gos2)
                            prad9(gos3)
                            ptrpni11(gos3,tablica[-1][3])
                            psad5(gos2,tablica[-1][2])
                            ppro5(gos1,tablica[-1][2])
            af.write('\n')

    ##  Trosložni 31. grupa glagola: inf. -ovati,evati,ivati prez. -ujem

        elif infs[-5:] in u'òvatièvatiìvati' and pres[-4:] in u'ȕjēm' and si==3:
            for bs in gos1:
                ## a) kòvati - kȕjēm
                if bs in u'ŗàèìòù':
                    gos3=kratkosilazni(bs,gos1)
                    for cs in gos2:
                        if cs in u'ȑȁȅȉȍȕ':
                            gos4=kratkouzlazni(cs,gos2)
                    prezent7(gos2)
                    aorist6(gos3,gos3,tablica[-1][2])
                    gos5=gos3[:-1]
                    imperfekt5(gos5,tablica[-1][2])
                    imperativ11(gos4)
                    prad9(gos3)
                    ptrpni11(gos3,tablica[-1][3])
                    psad5(gos2,tablica[-1][2])
                    ppro5(gos3,tablica[-1][2])
            af.write('\n')
        else:
            if si<4:
                af.write('\n')

    af.close()
    
