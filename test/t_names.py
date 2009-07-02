from Recode import listings
import common

class Tests(common.Test):

    def test_codings(self):
        # List of charsets and surfaces.
        output = '''\
/21-Permutation swabytes [21]
/4321-Permutation [432]
ANSI_X3.4-1968 367/CR-LF 646 ansix341986 ascii cp367/CR-LF ibm367/CR-LF iso646irv1991 iso646us isoir6 us usascii [3]
ASCII-BS bs [bs]
ASMO_449 arabic7 iso9036 isoir89 [iso9]
AtariST [at]
baltic isoir179 [bal]
Bang-Bang [ban]
/Base64 64 b64 base64codec [64]
BPI-101 afrl1101bpiocil tfra tfrancais tlatin1 [tla]
BPI-102 afrful102bpiocil bambara bra ewondo fulfulde [br]
BPI-103 afrful103bpiocil tbambara tbpi102 tbra tewondo tfulfulde [tba]
BPI-104 afrlin104bpiocil lin lingala sango wolof [wo]
BPI-105 afrlin105bpiocil tbpi104 tlin tlingala tsango twolof [ts]
BPI-106 [bpi106]
BPI-107 tbpi106 [bpi107]
BPI-108 [bpi108]
BPI-109 tbpi108 [bpi109]
BPI-110 [bpi110]
BPI-111 tbpi110 [bpi111]
BPI-112 [bpi112]
BPI-113 tbpi112 [bpi113]
BPI-JUCA-Translit tjuca [tj]
BS_4730 gb iso646gb isoir4 uk [gb]
BS_viewdata isoir47 [bsv]
CDC-NOS nos [cd]
combined-UCS-2 co [co]
CORK t1 [t1]
count-characters [cou]
cp1006 [cp1006]
cp1140 ibm1140 [cp11]
CP1250/CR-LF 1250/CR-LF msee windows1250 [mse]
CP1251/CR-LF 1251/CR-LF mscyrl windows1251 [msc]
CP1252/CR-LF 1252/CR-LF msansi windows1252 [1252]
CP1253/CR-LF 1253/CR-LF msgreek windows1253 [msg]
CP1254/CR-LF 1254/CR-LF msturk windows1254 [mst]
CP1255/CR-LF 1255/CR-LF mshebr windows1255 [msh]
CP1256/CR-LF 1256/CR-LF msarab windows1256 [1256]
CP1257/CR-LF 1257/CR-LF winbaltrim windows1257 [1257]
cp1258 [cp1258]
cp737 [cp73]
cp775 [cp77]
cp856 [cp856]
cp866 [cp866]
cp874 [cp874]
/CR [cr]
/CR-LF cl [cl]
CSA_Z243.4-1985-1 ca csa71 iso646ca isoir121 [ca]
CSA_Z243.4-1985-2 csa72 iso646ca2 isoir122 [csa72]
CSA_Z243.4-1985-gr isoir123 [isoir123]
CSN_369103 isoir139 koi8l2 [csn]
CWI cphu cwi2 [cwi]
/<Data> [da]
/Decimal-1 d d1 [d]
/Decimal-2 d2 [d2]
/Decimal-3 d3 [d3]
/Decimal-4 d4 [d4]
DEC-MCS dec [dec]
DIN_66003 de iso646de isoir21 [de]
DS_2089 dk iso646dk [dk]
dump-with-names [du]
EBCDIC-AT-DE [ebcdicatde]
EBCDIC-AT-DE-A [ebcdicatdea]
EBCDIC-CA-FR [ebcdicca]
EBCDIC-DK-NO [ebcdicdkno]
EBCDIC-DK-NO-A [ebcdicdknoa]
EBCDIC-ES [ebcdices]
EBCDIC-ES-A [ebcdicesa]
EBCDIC-ES-S [ebcdicess]
EBCDIC-FI-SE [ebcdicfise]
EBCDIC-FI-SE-A [ebcdicfisea]
EBCDIC-FR [ebcdicfr]
EBCDIC-IS-FRISS friss [fri]
EBCDIC-IT [ebcdicit]
EBCDIC-PT [ebcdicp]
EBCDIC-UK [ebcdicuk]
EBCDIC-US [ebcdicus]
ECMA-cyrillic ecma113 ecma1131986 isoir111 [ecmac]
ES iso646es isoir17 [es]
ES2 iso646es2 isoir85 [es2]
euc_kr ksc5601 [euck]
flat [fl]
GB_1988-80 cn iso646cn isoir57 [cn]
GOST_19768-87 isoir153 stsev35888 [st]
greek7 isoir88 [greek7]
greek7-old isoir18 [greek7o]
greek-ccitt isoir150 [greekc]
/Hexadecimal-1 x x1 [x]
/Hexadecimal-2 x2 [x2]
/Hexadecimal-3 x3 [x3]
/Hexadecimal-4 x4 [x4]
/hex_codec hex [hex]
hp-roman8 r8 roman8 [hp]
HTML_1.1 h1 [h1]
HTML_2.0 1866 h2 rfc1866 [18]
HTML_3.2 [html3]
HTML_4.0 h h4 html [h]
HTML-i18n 2070 h3 rfc2070 [20]
IBM037/CR-LF 037/CR-LF cp037/CR-LF ebcdiccpca ebcdiccpnl ebcdiccpus ebcdiccpwt ibm039 [037]
IBM038/CR-LF 038/CR-LF cp038/CR-LF ebcdicint [038]
IBM1004/CR-LF 1004/CR-LF cp1004/CR-LF os2latin1 [os]
IBM1026/CR-LF 1026/CR-LF cp1026/CR-LF [102]
IBM1047/CR-LF 1047/CR-LF cp1047/CR-LF [104]
IBM256/CR-LF 256/CR-LF cp256/CR-LF ebcdicint1 [25]
IBM273/CR-LF 273/CR-LF cp273/CR-LF [273]
IBM274/CR-LF 274/CR-LF cp274/CR-LF ebcdicbe [274]
IBM275/CR-LF 275/CR-LF cp275/CR-LF ebcdicbr [275]
IBM277/CR-LF ebcdiccpdk ebcdiccpno [ibm277]
IBM278/CR-LF 278/CR-LF cp278/CR-LF ebcdiccpfi ebcdiccpse [278]
IBM280/CR-LF 280/CR-LF cp280/CR-LF ebcdiccpit [280]
IBM281/CR-LF 281/CR-LF cp281/CR-LF ebcdicjpe [281]
IBM284/CR-LF 284/CR-LF cp284/CR-LF ebcdiccpes [284]
IBM285/CR-LF 285/CR-LF cp285/CR-LF ebcdiccpgb [285]
IBM290/CR-LF 290/CR-LF cp290/CR-LF ebcdicjpkana [290]
IBM297/CR-LF 297/CR-LF cp297/CR-LF ebcdiccpfr [297]
IBM420/CR-LF 420/CR-LF cp420/CR-LF ebcdiccpar1 [420]
IBM423/CR-LF 423/CR-LF cp423/CR-LF ebcdiccpgr [423]
IBM424/CR-LF 424/CR-LF cp424/CR-LF ebcdiccphe [424]
IBM437/CR-LF 437/CR-LF cp437/CR-LF dos/CR-LF ibmpc/CR-LF msdos/CR-LF pc/CR-LF [do]
IBM500/CR-LF 500/CR-LF 500v1 cp500/CR-LF ebcdiccpbe ebcdiccpch [500]
IBM850/CR-LF 850/CR-LF cp850/CR-LF [850]
IBM851/CR-LF 851/CR-LF cp851/CR-LF [851]
IBM852/CR-LF 852/CR-LF cp852/CR-LF pcl2 pclatin2 [852]
IBM855/CR-LF 855/CR-LF cp855/CR-LF [855]
IBM857/CR-LF 857/CR-LF cp857/CR-LF [857]
IBM860/CR-LF 860/CR-LF cp860/CR-LF [860]
IBM861/CR-LF 861/CR-LF cp861/CR-LF cpis [861]
IBM862/CR-LF 862/CR-LF cp862/CR-LF [862]
IBM863/CR-LF 863/CR-LF cp863/CR-LF [863]
IBM864/CR-LF 864/CR-LF cp864/CR-LF [864]
IBM865/CR-LF 865/CR-LF cp865/CR-LF [865]
IBM868/CR-LF 868/CR-LF cp868/CR-LF cpar [868]
IBM869/CR-LF 869/CR-LF cp869/CR-LF cpgr [869]
IBM870/CR-LF 870/CR-LF cp870/CR-LF ebcdiccproece ebcdiccpyu [870]
IBM871/CR-LF 871/CR-LF cp871/CR-LF ebcdiccpis [871]
IBM875/CR-LF 875/CR-LF cp875/CR-LF ebcdicgreek [875]
IBM880/CR-LF 880/CR-LF cp880/CR-LF ebcdiccyrillic [880]
IBM891/CR-LF 891/CR-LF cp891/CR-LF [89]
IBM903/CR-LF 903/CR-LF cp903/CR-LF [903]
IBM904/CR-LF 904/CR-LF cp904/CR-LF [904]
IBM905/CR-LF 905/CR-LF cp905/CR-LF ebcdiccptr [905]
IBM918/CR-LF 918/CR-LF cp918/CR-LF ebcdiccpar2 [918]
IEC_P27-1 isoir143 [ie]
INIS isoir49 [inis]
INIS-8 isoir50 [inis8]
INIS-cyrillic isoir51 [inisc]
INVARIANT isoir170 [inv]
ISO_10367-box isoir155 [iso103]
ISO-10646-UCS-2 bmp rune u2 ucs2 unicodeinternal [bm]
ISO_2033-1983 e13b isoir98 [e1]
ISO_5427 isoir37 [isoir3]
ISO_5427-ext iso54271981 isoir54 [isoir54]
ISO_5428 iso54281980 isoir55 [iso5428]
ISO_646.basic iso646basic1983 ref [re]
ISO_646.irv irv iso646irv1983 isoir2 [ir]
ISO_6937-2-25 isoir152 [iso69]
ISO-8859-1 819/CR-LF 8859 cp819/CR-LF ibm819/CR-LF iso8859 iso885911987 isoir100 l1 latin latin1 [81]
ISO-8859-10 iso8859101993 isoir157 l6 latin6 [l6]
ISO-8859-13 iso8859131998 isobaltic isoir179a l7 latin7 [l7]
ISO-8859-14 iso8859141998 isoceltic isoir199 l8 latin8 [l8]
ISO-8859-15 iso8859151998 isoir203 l9 latin9 [l9]
ISO-8859-2 912/CR-LF cp912/CR-LF ibm912/CR-LF iso885921987 isoir101 l2 latin2 [l2]
ISO-8859-3 iso885931988 isoir109 l3 latin3 [l3]
ISO-8859-4 iso885941988 isoir110 l4 latin4 [l4]
ISO-8859-5 cyrillic iso885951988 isoir144 [cy]
ISO-8859-6 arabic asmo708 ecma114 iso885961987 isoir127 [asmo7]
ISO-8859-7 ecma118 elot928 greek greek8 iso885971987 isoir126 [el]
ISO-8859-8 hebrew iso885981988 isoir138 [heb]
ISO-8859-9 iso885991989 isoir148 l5 latin5 [l5]
ISO_8859-supp isoir154 latin125 [latin12]
IT iso646it isoir15 [it]
JIS_C6220-1969-jp isoir13 jisc62201969 katakana x02017 [kat]
JIS_C6220-1969-ro iso646jp isoir14 jp [jp]
JIS_C6229-1984-b-add isoir93 jpocrbadd [isoir93]
JIS_C6229-1984-hand isoir94 jpocrhand [isoir94]
JIS_C6229-1984-hand-add isoir95 jpocrhandadd [isoir95]
JIS_C6229-1984-kana isoir96 [isoir96]
JIS_X0201 x0201 [jisx]
JUS_I.B1.002 iso646yu isoir141 js yu [y]
JUS_I.B1.003-mac isoir147 macedonian [mace]
JUS_I.B1.003-serb isoir146 serbian [ser]
KEYBCS2 kamenicky [ke]
KOI-7 [koi7]
KOI-8 gost1976874 [koi8]
KOI-8_CS2 [koi8c]
KOI8-R [koi8r]
KOI8-RU [koi8ru]
KOI8-U [koi8u]
KSC5636 iso646kr [ksc563]
LaTeX ltex tex [lt]
latin-greek isoir19 [isoir19]
Latin-greek-1 isoir27 [isoir27]
mac_cyrillic [maccy]
mac_greek [macg]
mac_iceland [macic]
macintosh/CR mac/CR [mac]
macintosh_ce/CR macce/CR [macce]
mac-is [macis]
mac_latin2 maccentraleurope [macl]
mac_roman [macr]
mac_turkish [mact]
MSZ_7795.3 hu iso646hu isoir86 [hu]
NATS-DANO isoir91 jisc62291984a jpocra [jpocra]
NATS-DANO-ADD iso646jpocrb isoir92 jisc62291984b jpocrb [jpocrb]
NATS-SEFI isoir81 [isoir81]
NATS-SEFI-ADD isoir82 [isoir82]
NC_NC00-10 cuba iso646cu isoir151 ncnc001081 [cu]
NeXTSTEP next [next]
NF_Z_62-010 fr iso646fr isoir69 [fr]
NF_Z_62-010_(1973) iso646fr1 isoir25 [isoir25]
NS_4551-1 iso646no isoir60 no [no]
NS_4551-2 iso646no2 isoir61 no2 [no2]
/Octal-1 o o1 [o]
/Octal-2 o2 [o2]
/Octal-3 o3 [o3]
/Octal-4 o4 [o4]
PT iso646pt isoir16 [pt]
PT2 iso646pt2 isoir84 [pt2]
/Quoted-Printable qp quopri quopricodec quoteprintable [qp]
raw_unicode_escape [ra]
/rot_13 [rot]
sami isoir158 lap latinlap [sam]
SEN_850200_B fi iso646fi iso646se isoir10 se ss636127 [fi]
SEN_850200_C iso646se2 isoir11 se2 [se2]
T.61-7bit isoir102 [t6]
TCVN [tc]
test15 [test15]
test16 [test16]
test7 [test7]
test8 [test8]
Texinfo texi ti [ti]
Texte txte [tx]
uhc [uh]
UNICODE-1-1-UTF-7 tf7 u7 utf7 [u7]
unicode_escape [unicodeescape]
Unicode-Escape-X java ue [ja]
<Ustring> [ust]
UTF-16 tf16 u16 u6 unicode [u1]
utf_16_be unicodebigunmarked [utf16b]
utf_16_le unicodelittleunmarked [utf16l]
UTF-8 fssutf tf8 u8 utf utf2 utf8ucs2 utf8ucs4 utffss [fs]
/uu_codec uu [uu]
VIQR [viq]
VISCII [vis]
VNI [vn]
VPS [vp]
XML-standalone h0 [h0]
/zlib_codec zip zlib [zi]
'''
        fragments = []
        listings.list_all_codings(fragments.append)
        # FIXME: Should produce diff, here.
        self.assertEqual(''.join(fragments), output)

    def test_subsets(self):
        # The `--find-subsets' option.
        output = '''\
[  0] IBM891 == IBM903
[  0] IBM903 == IBM891
[  3] IBM891 < IBM904
[  3] IBM903 < IBM904
[  3] JIS_C6229-1984-hand-add < JIS_C6229-1984-b-add
[  6] INVARIANT < T.61-7bit
[  6] T.61-7bit < ISO_646.irv
[ 10] INVARIANT < NATS-DANO-ADD
[ 12] INVARIANT < BS_4730
[ 12] INVARIANT < CSA_Z243.4-1985-1
[ 12] INVARIANT < CSA_Z243.4-1985-2
[ 12] INVARIANT < DIN_66003
[ 12] INVARIANT < DS_2089
[ 12] INVARIANT < ES
[ 12] INVARIANT < ES2
[ 12] INVARIANT < GB_1988-80
[ 12] INVARIANT < IBM891
[ 12] INVARIANT < IBM903
[ 12] INVARIANT < ISO_646.irv
[ 12] INVARIANT < IT
[ 12] INVARIANT < JIS_C6220-1969-ro
[ 12] INVARIANT < JUS_I.B1.002
[ 12] INVARIANT < KSC5636
[ 12] INVARIANT < MSZ_7795.3
[ 12] INVARIANT < NATS-SEFI
[ 12] INVARIANT < NC_NC00-10
[ 12] INVARIANT < NF_Z_62-010
[ 12] INVARIANT < NF_Z_62-010_(1973)
[ 12] INVARIANT < NS_4551-1
[ 12] INVARIANT < NS_4551-2
[ 12] INVARIANT < PT
[ 12] INVARIANT < PT2
[ 12] INVARIANT < SEN_850200_B
[ 12] INVARIANT < SEN_850200_C
[ 12] JIS_C6229-1984-kana < JIS_C6220-1969-jp
[ 13] INIS < BS_4730
[ 13] INIS < IBM891
[ 13] INIS < IBM903
[ 13] INIS < JIS_C6220-1969-ro
[ 13] INIS < KSC5636
[ 15] INVARIANT < IBM904
[ 16] INIS < IBM904
[ 28] JIS_C6229-1984-hand < NATS-DANO-ADD
[ 33] ISO_646.basic < INVARIANT
[ 39] ISO_646.basic < T.61-7bit
[ 43] ISO_646.basic < NATS-DANO-ADD
[ 45] ISO_646.basic < BS_4730
[ 45] ISO_646.basic < CSA_Z243.4-1985-1
[ 45] ISO_646.basic < CSA_Z243.4-1985-2
[ 45] ISO_646.basic < DIN_66003
[ 45] ISO_646.basic < DS_2089
[ 45] ISO_646.basic < ES
[ 45] ISO_646.basic < ES2
[ 45] ISO_646.basic < GB_1988-80
[ 45] ISO_646.basic < IBM891
[ 45] ISO_646.basic < IBM903
[ 45] ISO_646.basic < ISO_646.irv
[ 45] ISO_646.basic < IT
[ 45] ISO_646.basic < JIS_C6220-1969-ro
[ 45] ISO_646.basic < JUS_I.B1.002
[ 45] ISO_646.basic < KSC5636
[ 45] ISO_646.basic < MSZ_7795.3
[ 45] ISO_646.basic < NATS-SEFI
[ 45] ISO_646.basic < NC_NC00-10
[ 45] ISO_646.basic < NF_Z_62-010
[ 45] ISO_646.basic < NF_Z_62-010_(1973)
[ 45] ISO_646.basic < NS_4551-1
[ 45] ISO_646.basic < NS_4551-2
[ 45] ISO_646.basic < PT
[ 45] ISO_646.basic < PT2
[ 45] ISO_646.basic < SEN_850200_B
[ 45] ISO_646.basic < SEN_850200_C
[ 48] ISO_646.basic < IBM904
[ 61] IBM891 < ISO_10367-box
[ 61] IBM903 < ISO_10367-box
[ 63] IBM891 < KOI-8
[ 63] IBM903 < KOI-8
[ 64] T.61-7bit < ISO_6937-2-25
[ 65] KOI-8 < ECMA-cyrillic
[ 65] KOI-8 < KOI8-RU
[ 66] IBM891 < sami
[ 66] IBM903 < sami
[ 70] INVARIANT < ISO_6937-2-25
[ 73] INVARIANT < ISO_10367-box
[ 74] INIS < ISO_10367-box
[ 75] INVARIANT < KOI-8
[ 76] INIS < KOI-8
[ 78] INVARIANT < sami
[ 79] INIS < sami
[ 95] JIS_C6220-1969-ro < JIS_X0201
[ 96] EBCDIC-AT-DE < IBM273
[ 96] EBCDIC-DK-NO < IBM277
[ 96] EBCDIC-IT < IBM280
[ 96] EBCDIC-UK < IBM285
[ 96] IBM038 < IBM256
[100] IBM891 < GOST_19768-87
[100] IBM903 < GOST_19768-87
[103] IBM891 < IBM868
[103] IBM903 < IBM868
[103] ISO_646.basic < ISO_6937-2-25
[106] ISO_646.basic < ISO_10367-box
[107] INVARIANT < JIS_X0201
[108] INIS < JIS_X0201
[108] ISO_646.basic < KOI-8
[111] ISO_646.basic < sami
[112] IBM891 < KOI8-U
[112] IBM903 < KOI8-U
[112] INVARIANT < GOST_19768-87
[113] IBM891 < DEC-MCS
[113] IBM903 < DEC-MCS
[113] INIS < GOST_19768-87
[115] INVARIANT < IBM868
[116] INIS < IBM868
[119] IBM891 < IBM1004
[119] IBM903 < IBM1004
[121] IBM891 < NeXTSTEP
[121] IBM903 < NeXTSTEP
[122] IBM891 < ISO_8859-supp
[122] IBM903 < ISO_8859-supp
[124] INVARIANT < KOI8-U
[125] INIS < KOI8-U
[125] INVARIANT < DEC-MCS
[126] IBM891 < mac-is
[126] IBM891 < macintosh
[126] IBM903 < mac-is
[126] IBM903 < macintosh
[126] INIS < DEC-MCS
[127] IBM891 < IBM851
[127] IBM891 < hp-roman8
[127] IBM903 < IBM851
[127] IBM903 < hp-roman8
[128] IBM891 < CSA_Z243.4-1985-gr
[128] IBM891 < CWI
[128] IBM891 < ECMA-cyrillic
[128] IBM891 < IEC_P27-1
[128] IBM891 < KOI8-RU
[128] IBM891 < baltic
[128] IBM891 < macintosh_ce
[128] IBM903 < CSA_Z243.4-1985-gr
[128] IBM903 < CWI
[128] IBM903 < ECMA-cyrillic
[128] IBM903 < IEC_P27-1
[128] IBM903 < KOI8-RU
[128] IBM903 < baltic
[128] IBM903 < macintosh_ce
[131] INVARIANT < IBM1004
[132] INIS < IBM1004
[133] INVARIANT < NeXTSTEP
[134] INIS < NeXTSTEP
[134] INVARIANT < ISO_8859-supp
[134] T.61-7bit < CSN_369103
[135] INIS < ISO_8859-supp
[138] INVARIANT < mac-is
[138] INVARIANT < macintosh
[139] INIS < mac-is
[139] INIS < macintosh
[139] INVARIANT < IBM851
[139] INVARIANT < hp-roman8
[140] INIS < IBM851
[140] INIS < hp-roman8
[140] INVARIANT < CSA_Z243.4-1985-gr
[140] INVARIANT < CSN_369103
[140] INVARIANT < CWI
[140] INVARIANT < ECMA-cyrillic
[140] INVARIANT < IEC_P27-1
[140] INVARIANT < KOI8-RU
[140] INVARIANT < baltic
[140] INVARIANT < macintosh_ce
[140] ISO_646.basic < JIS_X0201
[141] INIS < CSA_Z243.4-1985-gr
[141] INIS < CWI
[141] INIS < ECMA-cyrillic
[141] INIS < IEC_P27-1
[141] INIS < KOI8-RU
[141] INIS < baltic
[141] INIS < macintosh_ce
[145] ISO_646.basic < GOST_19768-87
[148] ISO_646.basic < IBM868
[157] ISO_646.basic < KOI8-U
[158] ISO_646.basic < DEC-MCS
[164] ISO_646.basic < IBM1004
[164] ISO_646.basic < VPS
[166] ISO_646.basic < NeXTSTEP
[167] ISO_646.basic < ISO_8859-supp
[167] ISO_646.basic < TCVN
[171] ISO_646.basic < mac-is
[171] ISO_646.basic < macintosh
[172] ISO_646.basic < IBM851
[172] ISO_646.basic < hp-roman8
[173] ISO_646.basic < CSA_Z243.4-1985-gr
[173] ISO_646.basic < CSN_369103
[173] ISO_646.basic < CWI
[173] ISO_646.basic < ECMA-cyrillic
[173] ISO_646.basic < IEC_P27-1
[173] ISO_646.basic < KOI8-RU
[173] ISO_646.basic < VISCII
[173] ISO_646.basic < baltic
[173] ISO_646.basic < macintosh_ce
'''
        fragments = []
        listings.list_all_subsets(fragments.append)
        # FIXME: Should produce diff, here.
        self.assertEqual(''.join(fragments), output)

if __name__ == '__main__':
    import unittest
    unittest.main()
