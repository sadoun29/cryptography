# Tp1 : Décryptage par la chiffreement de céssar
#  	Sadoun Habib
#	M1 RESYS 2020/2021	


ctexte="bu haahxbhua wlba hbzzp lzzhfly k’hsalyly sl wyvavjvsl wvby sl avbyuly h zvu hchuahnl pswlba wylalukyl layl xblsxb’bu k’hbayl pualyjhsly kl uvbclhbe tlzzhnlz zbwwyptly klztlzzhnlz yltwshjly bu tlzzhnl why bu hbayl lucvfly bu cplbe tlzzhnl klaybpyl sljhuhs kl jvttbupjhapvu vb lujvyl tvkpmply s’pumvythapvu luylnpzayll why bu vykpuhalbyvu whyslyh hsvyz k’haahxblz hjapclz jhy lsslz ylxbplylua bul haapabkl hjapcl kl sh whyakl s’haahxbhua sh thuplyl kvua zvua tlullz jlz haahxblz klwluklua kb ylzlhbslz haahxbhuaz whzzpmz ul zvua pualylzzlz xbl why s’pumvythapvu xb’psz wlbclua nshulyjvujlyuhua slz whyapjpwhuaz hb wyvavjvsl psz jvssljapvuulua slz tlzzhnlz xbp jpyjbslualuayl slz kpmmlyluaz whyapjpwhuaz la lu lzzhfhua kl slz jyfwahuhsfzly slz haahxblz hjapclzwlbclua hb jvuayhpyl hcvpy iplu k’hbaylz viqljapmz s’haahxbhua wlba cvbsvpy zvpavialupy kl s’pumvythapvu zvpa klnyhkly slz wlymvythujlz kb zfzaltl zvpa jvyyvtwyl kls’pumvythapvu lepzahual zvpa lujvyl hcvpy hjjlz h klz ylzzvbyjlz uvu hbavypzllz"


alphabt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

tab_freq_fr={'A':9.4,
			'B':1,
			'C':2.6,
			'D':3.4,
			'E':15.9,
			'F':1,
			'G':1,
			'H':0.8,
			'I':8.4,
			'J':0.9,
			'K':0,
			'L':5.3,
			'M':3.2,
			'N':7.2,
			'O':5.1,
			'P':2.9,
			'Q':1.1,
			'R':6.5,
			'S':7.9,
			'T':7.3,
			'U':6.2,
			'V':2.1,
			'W':0,
			'X':0.3,
			'Y':0,
			'Z':0.3
			}

def Cessar_Crypt(txt,decalage):
    rst=''
    txt = txt.upper()
    for lettre in txt:
        ordr =alphabt.find(lettre)
        if ordr!=-1:
            indice = ordr + decalage
            if indice > 25:
                indice = indice % 26
            rst += alphabt[indice]
        else:
            rst += ' '
    return rst

def Encrypter_m(txt,decalage):
    return Cessar_Crypt(txt,decalage)

def Decrypter_c(txt,decalage):
    return Cessar_Crypt(txt,-decalage)


def analyse_frequece(txt):
	decalage=0
	txt=txt.upper()
	tab_freq={}

# Compter la fréquence des letrres 
	for lettre in alphabt:
		tab_freq[lettre] = txt.count(lettre)

	
	max_freq=0
	lettre_choix=''
	print('  Lettre		Repeat			Frequence   ')
	print('---------------------------------------------------------------')
	

	for freq in tab_freq.keys():
		taux =   tab_freq[freq]/len(txt)*100
		if max_freq<taux :
			max_freq = taux
			lettre_choix=freq 

		print('    %s			%d			%.2f ' % (freq , tab_freq[freq] ,taux))

	print('Lettre plus fréquenter du texte : %s  taux  : %.2f \n' % (lettre_choix , max_freq))

	# choix de lettre crypter

	max_freq_crypt = 0
	lettre_crypt=''
	for freq in tab_freq_fr.keys():
		taux =   tab_freq_fr[freq]
		if max_freq_crypt<taux :
			max_freq_crypt = taux
			lettre_crypt=freq 
	
	print('Lettre plus fréquenter frençais : %s  taux  : %.2f \n' % (lettre_crypt , max_freq_crypt))

	decalage = ord(lettre_choix)-ord(lettre_crypt)

	print(' Le décalage est : % d  \n'%(decalage))
	
	return decalage


#------------------------------ main ---------------------------------------

decalage = analyse_frequece(ctexte)

mtexte = Decrypter_c(ctexte,decalage)

print('Texte déchiffrer : \n',mtexte)
   
