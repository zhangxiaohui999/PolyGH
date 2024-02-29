import re
from collections import defaultdict


def write(filePath, content):
    with open(filePath, mode='a') as f:
        f.write(content)


list1 = [
    'utg000001l_pilon', 'utg000070l_pilon', 'utg000134l_pilon',
    'utg001062l_pilon', 'utg001654l_pilon', 'utg002268l_pilon',
    'utg000005l_pilon_10001_2400000', 'utg000005l_pilon_3620001_5900000',
    'utg000005l_pilon_5910001_10500000', 'utg000099l_pilon_10001_2760000',
    'utg000227l_pilon_10001_2170000', 'utg000277l_pilon_20001_3570000',
    'utg000323l_pilon_1840001_5260000', 'utg000323l_pilon_5280001_9160000',
    'utg000902l_pilon_10001_3400000'
]
list2 = [
    'utg000002l_pilon', 'utg000056l_pilon_1_3910000',
    'utg000056l_pilon_3910001_3930000', 'utg000056l_pilon_3930001_5193133',
    'utg000062l_pilon_1_880000', 'utg000062l_pilon_880001_890000',
    'utg000062l_pilon_890001_7500000', 'utg000062l_pilon_7500001_7520000',
    'utg000062l_pilon_7520001_9710000', 'utg000062l_pilon_9710001_9730000',
    'utg000062l_pilon_9730001_10740000', 'utg000062l_pilon_10740001_10750000',
    'utg000062l_pilon_10750001_13250000', 'utg000062l_pilon_13250001_13270000',
    'utg000062l_pilon_13270001_15032148', 'utg000145l_pilon_1_10000',
    'utg000145l_pilon_10001_280000', 'utg000145l_pilon_280001_300000',
    'utg000145l_pilon_300001_1090000', 'utg000145l_pilon_1090001_1100000',
    'utg000145l_pilon_1100001_1720000', 'utg000145l_pilon_1720001_1740000',
    'utg000145l_pilon_1740001_2056871', 'utg000219l_pilon_1_7430000',
    'utg000219l_pilon_7430001_7450000', 'utg000219l_pilon_7450001_8239636',
    'utg000459l_pilon', 'utg000932l_pilon_1_400000',
    'utg000932l_pilon_400001_420000', 'utg000932l_pilon_420001_2774695',
    'utg000983l_pilon', 'utg001073l_pilon_1_2030000',
    'utg001073l_pilon_2030001_2034999', 'utg002375l_pilon', 'utg003478l_pilon'
]
list3 = [
    'utg000003l_pilon', 'utg000036l_pilon_1_1880000',
    'utg000036l_pilon_1880001_1890000', 'utg000036l_pilon_1890001_2828971',
    'utg000617l_pilon', 'utg000708l_pilon_1_70000',
    'utg000708l_pilon_70001_90000', 'utg000708l_pilon_90001_422230',
    'utg001264l_pilon', 'utg001551l_pilon', 'utg001720l_pilon',
    'utg002132l_pilon', 'utg000076l_pilon_70001_2510000'
]
list4 = [
    'utg000004l_pilon', 'utg000038l_pilon', 'utg000067l_pilon',
    'utg000131l_pilon', 'utg000178l_pilon', 'utg000200l_pilon',
    'utg000251l_pilon', 'utg000348l_pilon', 'utg000367l_pilon',
    'utg000379l_pilon', 'utg000514l_pilon', 'utg000627l_pilon',
    'utg000697l_pilon', 'utg000770l_pilon', 'utg000772l_pilon',
    'utg000773l_pilon_1_20000', 'utg000773l_pilon_20001_350000',
    'utg000773l_pilon_350001_370000', 'utg000773l_pilon_370001_629621',
    'utg000783l_pilon', 'utg000823l_pilon_1_10000',
    'utg000823l_pilon_10001_20000', 'utg000823l_pilon_20001_1509597',
    'utg000957l_pilon', 'utg001336l_pilon', 'utg001492l_pilon',
    'utg001544l_pilon', 'utg001754l_pilon', 'utg001808l_pilon',
    'utg001941l_pilon', 'utg002488l_pilon', 'utg002708l_pilon',
    'utg002712l_pilon', 'utg002755l_pilon', 'utg002865l_pilon',
    'utg002993l_pilon', 'utg003793l_pilon', 'utg004154l_pilon',
    'utg004433l_pilon', 'utg000549l_pilon_20001_4440000'
]
list5 = [
    'utg000006l_pilon', 'utg000475l_pilon', 'utg000537l_pilon',
    'utg000809l_pilon', 'utg000967l_pilon', 'utg000978l_pilon',
    'utg001040l_pilon', 'utg001227l_pilon', 'utg001361l_pilon',
    'utg001455l_pilon', 'utg006357l_pilon', 'utg000198l_pilon_30001_3150000'
]
list6 = [
    'utg000007l_pilon_1_1420000', 'utg000007l_pilon_1420001_1440000',
    'utg000007l_pilon_1440001_5800000', 'utg000007l_pilon_5800001_5810000',
    'utg000007l_pilon_5810001_7250000', 'utg000007l_pilon_7250001_7270000',
    'utg000007l_pilon_7270001_8031946', 'utg000129l_pilon', 'utg000172l_pilon',
    'utg000193l_pilon', 'utg000229l_pilon', 'utg000253l_pilon',
    'utg000269l_pilon', 'utg000286l_pilon_1_1810000',
    'utg000286l_pilon_1810001_1830000', 'utg000286l_pilon_1830001_2210979',
    'utg000303l_pilon', 'utg000324l_pilon', 'utg000352l_pilon',
    'utg000356l_pilon', 'utg000442l_pilon', 'utg000458l_pilon',
    'utg000473l_pilon', 'utg000488l_pilon', 'utg000522l_pilon_1_80000',
    'utg000522l_pilon_80001_90000', 'utg000522l_pilon_90001_373488',
    'utg000541l_pilon', 'utg000612l_pilon', 'utg000673l_pilon_1_4650000',
    'utg000673l_pilon_4650001_4662171', 'utg000763l_pilon', 'utg000843l_pilon',
    'utg001110l_pilon_1_440000', 'utg001110l_pilon_440001_450000',
    'utg001110l_pilon_450001_455799', 'utg001143l_pilon', 'utg001178l_pilon',
    'utg001228l_pilon', 'utg001249l_pilon', 'utg001319l_pilon',
    'utg001335l_pilon', 'utg001527l_pilon', 'utg001528l_pilon',
    'utg001606l_pilon', 'utg001662l_pilon', 'utg001688l_pilon',
    'utg001710l_pilon', 'utg001996l_pilon', 'utg002037l_pilon',
    'utg002079l_pilon', 'utg002198l_pilon', 'utg002531l_pilon',
    'utg002660l_pilon', 'utg002788l_pilon', 'utg002930l_pilon',
    'utg002940l_pilon', 'utg002945l_pilon', 'utg003070l_pilon',
    'utg003866l_pilon', 'utg004025l_pilon', 'utg004096l_pilon',
    'utg004253l_pilon', 'utg004680l_pilon_1_100000',
    'utg004680l_pilon_100001_110000', 'utg004680l_pilon_110001_112388',
    'utg005430l_pilon'
]
list7 = [
    'utg000008l_pilon_1_1150000', 'utg000008l_pilon_1150001_1160000',
    'utg000008l_pilon_1160001_7406417', 'utg000272l_pilon', 'utg000592l_pilon',
    'utg000674l_pilon_1_740000', 'utg000674l_pilon_740001_750000',
    'utg000674l_pilon_750001_845899', 'utg000934l_pilon', 'utg001112l_pilon',
    'utg001255l_pilon', 'utg001296l_pilon', 'utg001482l_pilon_1_730000',
    'utg001482l_pilon_730001_750000', 'utg001482l_pilon_750001_756299',
    'utg001508l_pilon', 'utg001536l_pilon', 'utg001753l_pilon',
    'utg003578l_pilon', 'utg003641l_pilon', 'utg000029l_pilon_1_3050000',
    'utg000243l_pilon_1120001_4890000', 'utg000243l_pilon_6840001_9050000',
    'utg000267l_pilon_1150001_4200000', 'utg000406l_pilon_2960001_5489075',
    'utg000568l_pilon_1_4560000'
]
list8 = [
    'utg000009l_pilon', 'utg000061l_pilon_1_20000',
    'utg000061l_pilon_20001_3930665', 'utg000075l_pilon', 'utg000121l_pilon',
    'utg000260l_pilon', 'utg000275l_pilon', 'utg000441l_pilon',
    'utg000599l_pilon', 'utg000647l_pilon', 'utg000793l_pilon',
    'utg000829l_pilon', 'utg000938l_pilon', 'utg000962l_pilon',
    'utg001213l_pilon', 'utg001413l_pilon', 'utg001436l_pilon',
    'utg001533l_pilon', 'utg001682l_pilon', 'utg001705l_pilon',
    'utg001756l_pilon', 'utg001833l_pilon', 'utg002110l_pilon',
    'utg002227l_pilon', 'utg002559l_pilon', 'utg002968l_pilon',
    'utg003917l_pilon', 'utg004079l_pilon', 'utg005590l_pilon'
]
list9 = [
    'utg000010l_pilon_1_2500000', 'utg000010l_pilon_2500001_2520000',
    'utg000010l_pilon_2520001_4305603', 'utg000155l_pilon', 'utg000238l_pilon',
    'utg000351l_pilon_1_10000', 'utg000351l_pilon_10001_30000',
    'utg000351l_pilon_30001_40000', 'utg000351l_pilon_40001_502697',
    'utg000354l_pilon', 'utg000412l_pilon', 'utg000425l_pilon_1_10000',
    'utg000425l_pilon_10001_20000', 'utg000425l_pilon_20001_638001',
    'utg000433l_pilon', 'utg000449l_pilon', 'utg000795l_pilon',
    'utg000836l_pilon', 'utg001017l_pilon_1_5020000',
    'utg001017l_pilon_5020001_5030000', 'utg001017l_pilon_5030001_5036897',
    'utg001045l_pilon', 'utg001085l_pilon', 'utg001125l_pilon',
    'utg001175l_pilon', 'utg001250l_pilon_1_10000',
    'utg001250l_pilon_10001_30000', 'utg001250l_pilon_30001_323752',
    'utg001434l_pilon', 'utg002083l_pilon', 'utg003008l_pilon',
    'utg003104l_pilon', 'utg003208l_pilon', 'utg003567l_pilon',
    'utg004942l_pilon'
]
list10 = [
    'utg000011l_pilon', 'utg000065l_pilon', 'utg000094l_pilon',
    'utg000257l_pilon', 'utg000631l_pilon', 'utg000689l_pilon_1_300000',
    'utg000689l_pilon_300001_310000', 'utg000689l_pilon_310001_1818913',
    'utg000711l_pilon', 'utg001022l_pilon', 'utg001149l_pilon',
    'utg001171l_pilon', 'utg001221l_pilon', 'utg001259l_pilon',
    'utg001495l_pilon', 'utg001518l_pilon_1_560000',
    'utg001518l_pilon_560001_580000', 'utg001518l_pilon_580001_681825',
    'utg001560l_pilon', 'utg001671l_pilon_1_1370000',
    'utg001671l_pilon_1370001_1387579', 'utg001712l_pilon', 'utg001768l_pilon',
    'utg001825l_pilon', 'utg002109l_pilon', 'utg002484l_pilon',
    'utg002745l_pilon', 'utg003565l_pilon', 'utg003746l_pilon'
]
list11 = [
    'utg000012l_pilon', 'utg000064l_pilon', 'utg000249l_pilon_1_3620000',
    'utg000249l_pilon_3620001_3640000', 'utg000249l_pilon_3640001_4460000',
    'utg000249l_pilon_4460001_4470000', 'utg000249l_pilon_4470001_4490000',
    'utg000249l_pilon_4490001_4498021', 'utg000670l_pilon', 'utg001236l_pilon',
    'utg001412l_pilon', 'utg001590l_pilon', 'utg001641l_pilon',
    'utg001839l_pilon', 'utg002029l_pilon', 'utg002206l_pilon',
    'utg002282l_pilon', 'utg002390l_pilon', 'utg002608l_pilon',
    'utg002980l_pilon', 'utg003633l_pilon', 'utg003639l_pilon'
]
list12 = [
    'utg000013l_pilon_1_4030000', 'utg000013l_pilon_4030001_4039976',
    'utg000137l_pilon', 'utg000188l_pilon', 'utg000191l_pilon',
    'utg000305l_pilon_1_10000', 'utg000305l_pilon_10001_2129191',
    'utg000319l_pilon_1_10000', 'utg000319l_pilon_10001_20000',
    'utg000319l_pilon_20001_4424738', 'utg000400l_pilon', 'utg000453l_pilon',
    'utg000501l_pilon', 'utg000540l_pilon', 'utg000563l_pilon',
    'utg000704l_pilon', 'utg000816l_pilon', 'utg000913l_pilon',
    'utg000993l_pilon', 'utg001004l_pilon', 'utg001048l_pilon',
    'utg001582l_pilon', 'utg001588l_pilon', 'utg001786l_pilon',
    'utg001985l_pilon', 'utg002071l_pilon', 'utg002101l_pilon_1_1120000',
    'utg002101l_pilon_1120001_1150000', 'utg002101l_pilon_1150001_1245124',
    'utg002773l_pilon', 'utg003126l_pilon', 'utg003659l_pilon',
    'utg004674l_pilon', 'utg005845l_pilon'
]
list13 = [
    'utg000014l_pilon_1_1380000', 'utg000014l_pilon_1380001_1390000',
    'utg000014l_pilon_1390001_2441410', 'utg000040l_pilon', 'utg000142l_pilon',
    'utg000143l_pilon', 'utg000150l_pilon', 'utg000166l_pilon',
    'utg000258l_pilon', 'utg000273l_pilon_1_4190000',
    'utg000273l_pilon_4190001_4200000', 'utg000273l_pilon_4200001_4220000',
    'utg000273l_pilon_4220001_4420000', 'utg000273l_pilon_4420001_4440000',
    'utg000273l_pilon_4440001_4490000', 'utg000273l_pilon_4490001_4501731',
    'utg000300l_pilon', 'utg000533l_pilon', 'utg000573l_pilon',
    'utg000610l_pilon_1_580000', 'utg000610l_pilon_580001_590000',
    'utg000610l_pilon_590001_2163257', 'utg000629l_pilon', 'utg000724l_pilon',
    'utg000778l_pilon', 'utg000781l_pilon', 'utg000808l_pilon',
    'utg000927l_pilon', 'utg000958l_pilon', 'utg001006l_pilon',
    'utg001054l_pilon', 'utg001584l_pilon', 'utg001618l_pilon_1_10000',
    'utg001618l_pilon_10001_50000', 'utg001618l_pilon_50001_130000',
    'utg001618l_pilon_130001_150000', 'utg001618l_pilon_150001_922795',
    'utg001634l_pilon', 'utg001717l_pilon', 'utg001750l_pilon',
    'utg001758l_pilon', 'utg002479l_pilon_1_360000',
    'utg002479l_pilon_360001_370000', 'utg002479l_pilon_370001_534532',
    'utg002577l_pilon', 'utg002674l_pilon', 'utg002830l_pilon',
    'utg002852l_pilon', 'utg003006l_pilon', 'utg003160l_pilon_1_10000',
    'utg003160l_pilon_10001_103811', 'utg004832l_pilon',
    'utg000749l_pilon_10001_2920000'
]
list14 = [
    'utg000016l_pilon', 'utg000074l_pilon', 'utg000122l_pilon',
    'utg000123l_pilon', 'utg000164l_pilon_1_1420000',
    'utg000164l_pilon_1420001_1450000', 'utg000164l_pilon_1450001_3500000',
    'utg000164l_pilon_3500001_3520000', 'utg000164l_pilon_3520001_9311899',
    'utg000226l_pilon', 'utg000374l_pilon', 'utg000438l_pilon',
    'utg000656l_pilon', 'utg000663l_pilon_1_410000',
    'utg000663l_pilon_410001_420000', 'utg000663l_pilon_420001_3987703',
    'utg000717l_pilon', 'utg000741l_pilon', 'utg000834l_pilon',
    'utg000853l_pilon_1_670000', 'utg000853l_pilon_670001_690000',
    'utg000853l_pilon_690001_780000', 'utg000853l_pilon_780001_790000',
    'utg000853l_pilon_790001_837926', 'utg001035l_pilon', 'utg001049l_pilon',
    'utg001235l_pilon', 'utg001238l_pilon', 'utg001341l_pilon',
    'utg001415l_pilon', 'utg001497l_pilon', 'utg001532l_pilon',
    'utg001652l_pilon', 'utg001673l_pilon', 'utg001855l_pilon',
    'utg001951l_pilon', 'utg002074l_pilon', 'utg002224l_pilon',
    'utg002343l_pilon', 'utg002463l_pilon', 'utg002532l_pilon',
    'utg003175l_pilon', 'utg003487l_pilon', 'utg003998l_pilon',
    'utg004168l_pilon'
]
list15 = [
    'utg000022l_pilon', 'utg000093l_pilon', 'utg000675l_pilon',
    'utg000898l_pilon', 'utg001141l_pilon', 'utg001208l_pilon',
    'utg001309l_pilon', 'utg001703l_pilon', 'utg002013l_pilon',
    'utg002095l_pilon', 'utg002436l_pilon', 'utg002566l_pilon',
    'utg002725l_pilon', 'utg002950l_pilon', 'utg003030l_pilon',
    'utg003123l_pilon', 'utg003682l_pilon', 'utg000571l_pilon_670001_3340000'
]
list16 = [
    'utg000023l_pilon', 'utg000031l_pilon', 'utg000051l_pilon',
    'utg000054l_pilon', 'utg000060l_pilon_1_2920000',
    'utg000060l_pilon_2920001_2930000', 'utg000060l_pilon_2930001_5110000',
    'utg000060l_pilon_5110001_5120000', 'utg000060l_pilon_5120001_5130674',
    'utg000077l_pilon_1_8580000', 'utg000077l_pilon_8580001_8590000',
    'utg000077l_pilon_8590001_8641989', 'utg000158l_pilon', 'utg000186l_pilon',
    'utg000231l_pilon', 'utg000232l_pilon', 'utg000233l_pilon_1_4310000',
    'utg000233l_pilon_4310001_4330000', 'utg000233l_pilon_4330001_5202486',
    'utg000251l_pilon', 'utg000252l_pilon_1_960000',
    'utg000252l_pilon_960001_980000', 'utg000252l_pilon_980001_984918',
    'utg000280l_pilon', 'utg000304l_pilon', 'utg000310l_pilon',
    'utg000417l_pilon', 'utg000429l_pilon', 'utg000511l_pilon',
    'utg000516l_pilon', 'utg000638l_pilon_1_1910000',
    'utg000638l_pilon_1910001_1930000', 'utg000638l_pilon_1930001_5746053',
    'utg000868l_pilon', 'utg000893l_pilon_1_790000',
    'utg000893l_pilon_790001_800000', 'utg000893l_pilon_800001_811908',
    'utg000907l_pilon', 'utg001034l_pilon', 'utg001070l_pilon',
    'utg001360l_pilon', 'utg001382l_pilon', 'utg001443l_pilon',
    'utg001515l_pilon', 'utg001547l_pilon', 'utg001598l_pilon',
    'utg001649l_pilon', 'utg002255l_pilon', 'utg002585l_pilon',
    'utg002632l_pilon', 'utg002776l_pilon', 'utg002846l_pilon',
    'utg002943l_pilon', 'utg003535l_pilon', 'utg003856l_pilon',
    'utg004042l_pilon', 'utg004354l_pilon', 'utg004698l_pilon',
    'utg004734l_pilon', 'utg004958l_pilon', 'utg006028l_pilon'
]
list17 = [
    'utg000026l_pilon_1_10000', 'utg000026l_pilon_10001_50000',
    'utg000026l_pilon_50001_11092605', 'utg000259l_pilon', 'utg000411l_pilon',
    'utg000416l_pilon_1_10000', 'utg000416l_pilon_10001_20000',
    'utg000416l_pilon_20001_1242103', 'utg000455l_pilon', 'utg000530l_pilon',
    'utg000609l_pilon', 'utg000722l_pilon', 'utg000788l_pilon',
    'utg000946l_pilon', 'utg000949l_pilon', 'utg001076l_pilon',
    'utg001327l_pilon', 'utg001358l_pilon', 'utg001368l_pilon',
    'utg001441l_pilon', 'utg001460l_pilon', 'utg001531l_pilon',
    'utg001559l_pilon', 'utg001624l_pilon', 'utg001956l_pilon',
    'utg002007l_pilon', 'utg002185l_pilon', 'utg002299l_pilon',
    'utg002307l_pilon', 'utg002568l_pilon', 'utg003042l_pilon',
    'utg003172l_pilon', 'utg003369l_pilon', 'utg004241l_pilon',
    'utg005393l_pilon', 'utg006052l_pilon', 'utg007232l_pilon'
]
list18 = [
    'utg000027l_pilon', 'utg000043l_pilon', 'utg000120l_pilon',
    'utg000237l_pilon', 'utg000283l_pilon', 'utg000295l_pilon',
    'utg000299l_pilon', 'utg000347l_pilon', 'utg000373l_pilon',
    'utg000409l_pilon', 'utg000519l_pilon', 'utg000570l_pilon',
    'utg000687l_pilon', 'utg000707l_pilon', 'utg000915l_pilon',
    'utg001083l_pilon', 'utg001091l_pilon', 'utg001146l_pilon',
    'utg001197l_pilon', 'utg001379l_pilon', 'utg001386l_pilon',
    'utg001392l_pilon', 'utg001483l_pilon', 'utg001562l_pilon',
    'utg001653l_pilon', 'utg001737l_pilon', 'utg002010l_pilon',
    'utg002367l_pilon', 'utg002554l_pilon', 'utg002604l_pilon',
    'utg002845l_pilon', 'utg002861l_pilon', 'utg003595l_pilon',
    'utg003734l_pilon', 'utg000749l_pilon_10001_2920000'
]
list19 = [
    'utg000028l_pilon', 'utg000058l_pilon', 'utg000092l_pilon',
    'utg000100l_pilon_1_70000', 'utg000100l_pilon_70001_100000',
    'utg000100l_pilon_100001_370000', 'utg000100l_pilon_370001_380000',
    'utg000100l_pilon_380001_410000', 'utg000100l_pilon_410001_430000',
    'utg000100l_pilon_430001_3242382', 'utg000102l_pilon_1_450000',
    'utg000102l_pilon_450001_460000', 'utg000102l_pilon_460001_480000',
    'utg000102l_pilon_480001_2270000', 'utg000102l_pilon_2270001_2290000',
    'utg000102l_pilon_2290001_2350000', 'utg000102l_pilon_2350001_2360000',
    'utg000102l_pilon_2360001_2370000', 'utg000102l_pilon_2370001_2380000',
    'utg000102l_pilon_2380001_2390000', 'utg000102l_pilon_2390001_3530000',
    'utg000102l_pilon_3530001_3540000', 'utg000102l_pilon_3540001_3560000',
    'utg000102l_pilon_3560001_3570000', 'utg000102l_pilon_3570001_3980000',
    'utg000102l_pilon_3980001_4000000', 'utg000102l_pilon_4000001_4010000',
    'utg000102l_pilon_4010001_4040000', 'utg000102l_pilon_4040001_4050000',
    'utg000102l_pilon_4050001_4070000', 'utg000102l_pilon_4070001_4080000',
    'utg000102l_pilon_4080001_4100000', 'utg000102l_pilon_4100001_4120000',
    'utg000102l_pilon_4120001_4490000', 'utg000102l_pilon_4490001_4500000',
    'utg000102l_pilon_4500001_4510000', 'utg000102l_pilon_4510001_4520000',
    'utg000102l_pilon_4520001_5586663', 'utg000151l_pilon_1_290000',
    'utg000151l_pilon_290001_310000', 'utg000151l_pilon_310001_1489274',
    'utg000171l_pilon', 'utg000181l_pilon', 'utg000209l_pilon',
    'utg000211l_pilon_1_1410000', 'utg000211l_pilon_1410001_1430000',
    'utg000211l_pilon_1430001_1590000', 'utg000211l_pilon_1590001_1610000',
    'utg000211l_pilon_1610001_2720000', 'utg000211l_pilon_2720001_2730000',
    'utg000211l_pilon_2730001_2740000', 'utg000211l_pilon_2740001_2780000',
    'utg000211l_pilon_2780001_2800000', 'utg000211l_pilon_2800001_3370000',
    'utg000211l_pilon_3370001_3390000', 'utg000211l_pilon_3390001_3440000',
    'utg000211l_pilon_3440001_3450000', 'utg000211l_pilon_3450001_3780000',
    'utg000211l_pilon_3780001_3790000', 'utg000211l_pilon_3790001_5450000',
    'utg000211l_pilon_5450001_5470000', 'utg000211l_pilon_5470001_5920000',
    'utg000211l_pilon_5920001_5930000', 'utg000211l_pilon_5930001_5960000',
    'utg000211l_pilon_5960001_5970000', 'utg000211l_pilon_5970001_6160000',
    'utg000211l_pilon_6160001_6180000', 'utg000211l_pilon_6180001_6380000',
    'utg000211l_pilon_6380001_6400000', 'utg000211l_pilon_6400001_6445863',
    'utg000236l_pilon_1_1210000', 'utg000236l_pilon_1210001_1230000',
    'utg000236l_pilon_1230001_1340000', 'utg000236l_pilon_1340001_1350000',
    'utg000236l_pilon_1350001_1380000', 'utg000236l_pilon_1380001_1390000',
    'utg000236l_pilon_1390001_1590000', 'utg000236l_pilon_1590001_1610000',
    'utg000236l_pilon_1610001_1710000', 'utg000236l_pilon_1710001_1720000',
    'utg000236l_pilon_1720001_1740000', 'utg000236l_pilon_1740001_1750000',
    'utg000236l_pilon_1750001_1930000', 'utg000236l_pilon_1930001_1950000',
    'utg000236l_pilon_1950001_1970000', 'utg000236l_pilon_1970001_2430000',
    'utg000236l_pilon_2430001_2450000', 'utg000236l_pilon_2450001_2470000',
    'utg000236l_pilon_2470001_2480000', 'utg000236l_pilon_2480001_2570000',
    'utg000236l_pilon_2570001_2580000', 'utg000236l_pilon_2580001_3510000',
    'utg000236l_pilon_3510001_3520000', 'utg000236l_pilon_3520001_3540000',
    'utg000236l_pilon_3540001_3550000', 'utg000236l_pilon_3550001_3560000',
    'utg000236l_pilon_3560001_3570000', 'utg000236l_pilon_3570001_3580000',
    'utg000236l_pilon_3580001_3590000', 'utg000236l_pilon_3590001_3690000',
    'utg000236l_pilon_3690001_3710000', 'utg000236l_pilon_3710001_4390000',
    'utg000236l_pilon_4390001_4400000', 'utg000236l_pilon_4400001_4770000',
    'utg000236l_pilon_4770001_4800000', 'utg000236l_pilon_4800001_5050000',
    'utg000236l_pilon_5050001_5060000', 'utg000236l_pilon_5060001_5950000',
    'utg000236l_pilon_5950001_5970000', 'utg000236l_pilon_5970001_6366415',
    'utg000325l_pilon_1_830000', 'utg000325l_pilon_830001_840000',
    'utg000325l_pilon_840001_2380000', 'utg000325l_pilon_2380001_2400000',
    'utg000325l_pilon_2400001_2440000', 'utg000325l_pilon_2440001_2470000',
    'utg000325l_pilon_2470001_2480000', 'utg000325l_pilon_2480001_3143154',
    'utg000384l_pilon_1_210000', 'utg000384l_pilon_210001_240000',
    'utg000384l_pilon_240001_1300000', 'utg000384l_pilon_1300001_1320000',
    'utg000384l_pilon_1320001_1340000', 'utg000384l_pilon_1340001_1350000',
    'utg000384l_pilon_1350001_1380000', 'utg000384l_pilon_1380001_1400000',
    'utg000384l_pilon_1400001_1410000', 'utg000384l_pilon_1410001_1430000',
    'utg000384l_pilon_1430001_1750000', 'utg000384l_pilon_1750001_1770000',
    'utg000384l_pilon_1770001_1940000', 'utg000384l_pilon_1940001_1960000',
    'utg000384l_pilon_1960001_2010000', 'utg000384l_pilon_2010001_2020000',
    'utg000384l_pilon_2020001_3008123', 'utg000443l_pilon_1_60000',
    'utg000443l_pilon_60001_80000', 'utg000443l_pilon_80001_1720714',
    'utg000463l_pilon', 'utg000481l_pilon_1_20000',
    'utg000481l_pilon_20001_40000', 'utg000481l_pilon_40001_600000',
    'utg000481l_pilon_600001_610000', 'utg000481l_pilon_610001_1000000',
    'utg000481l_pilon_1000001_1020000', 'utg000481l_pilon_1020001_1040000',
    'utg000481l_pilon_1040001_1250000', 'utg000481l_pilon_1250001_1260000',
    'utg000481l_pilon_1260001_1270000', 'utg000481l_pilon_1270001_1280000',
    'utg000481l_pilon_1280001_3134422', 'utg000584l_pilon_1_160000',
    'utg000584l_pilon_160001_170000', 'utg000584l_pilon_170001_210000',
    'utg000584l_pilon_210001_520000', 'utg000584l_pilon_520001_530000',
    'utg000584l_pilon_530001_540000', 'utg000584l_pilon_540001_660000',
    'utg000584l_pilon_660001_680000', 'utg000584l_pilon_680001_1190000',
    'utg000584l_pilon_1190001_1200000', 'utg000584l_pilon_1200001_1320000',
    'utg000584l_pilon_1320001_1330000', 'utg000584l_pilon_1330001_1340000',
    'utg000584l_pilon_1340001_2777094', 'utg000607l_pilon', 'utg000632l_pilon',
    'utg000636l_pilon', 'utg000738l_pilon', 'utg000912l_pilon',
    'utg000966l_pilon', 'utg000994l_pilon', 'utg001016l_pilon',
    'utg001041l_pilon', 'utg001056l_pilon_1_160000',
    'utg001056l_pilon_160001_170000', 'utg001056l_pilon_170001_180000',
    'utg001056l_pilon_180001_200000', 'utg001056l_pilon_200001_210000',
    'utg001056l_pilon_210001_240000', 'utg001056l_pilon_240001_630000',
    'utg001056l_pilon_630001_640000', 'utg001056l_pilon_640001_660000',
    'utg001056l_pilon_660001_1351804', 'utg001124l_pilon', 'utg001139l_pilon',
    'utg001313l_pilon', 'utg001353l_pilon', 'utg001680l_pilon',
    'utg001882l_pilon', 'utg001888l_pilon_1_290000',
    'utg001888l_pilon_290001_300000', 'utg001888l_pilon_300001_301545',
    'utg001894l_pilon', 'utg002336l_pilon', 'utg002363l_pilon',
    'utg002383l_pilon', 'utg002418l_pilon', 'utg002696l_pilon',
    'utg002716l_pilon', 'utg003034l_pilon', 'utg003230l_pilon',
    'utg003724l_pilon', 'utg004302l_pilon', 'utg004795l_pilon',
    'utg006046l_pilon', 'utg006397l_pilon', 'utg000691l_pilon_10001_2310000'
]
list20 = [
    'utg000032l_pilon', 'utg000039l_pilon', 'utg000042l_pilon',
    'utg000046l_pilon', 'utg000079l_pilon', 'utg000114l_pilon',
    'utg000169l_pilon', 'utg000176l_pilon', 'utg000201l_pilon',
    'utg000340l_pilon_1_5400000', 'utg000340l_pilon_5400001_5410000',
    'utg000340l_pilon_5410001_5418456', 'utg000382l_pilon', 'utg000403l_pilon',
    'utg000407l_pilon', 'utg000604l_pilon_1_690000',
    'utg000604l_pilon_690001_710000', 'utg000604l_pilon_710001_859689',
    'utg000720l_pilon', 'utg000735l_pilon_1_10000',
    'utg000735l_pilon_10001_30000', 'utg000735l_pilon_30001_692144',
    'utg000766l_pilon', 'utg000851l_pilon', 'utg000890l_pilon',
    'utg001105l_pilon', 'utg001377l_pilon', 'utg001472l_pilon',
    'utg002063l_pilon', 'utg002441l_pilon', 'utg003985l_pilon',
    'utg004789l_pilon', 'utg004941l_pilon', 'utg000336l_pilon_40001_2280000',
    'utg000536l_pilon_20001_2530000', 'utg000990l_pilon_480001_3270000'
]
list21 = [
    'utg000035l_pilon', 'utg000095l_pilon_1_4620000',
    'utg000095l_pilon_4620001_4640000', 'utg000095l_pilon_4640001_5600438',
    'utg000140l_pilon', 'utg000230l_pilon', 'utg000413l_pilon',
    'utg000586l_pilon', 'utg000681l_pilon', 'utg000693l_pilon',
    'utg000710l_pilon', 'utg000718l_pilon', 'utg000744l_pilon',
    'utg000955l_pilon', 'utg001003l_pilon', 'utg001036l_pilon',
    'utg001663l_pilon', 'utg001664l_pilon', 'utg001711l_pilon',
    'utg001842l_pilon', 'utg002060l_pilon', 'utg002170l_pilon',
    'utg002256l_pilon', 'utg002688l_pilon', 'utg002750l_pilon',
    'utg003009l_pilon', 'utg003067l_pilon', 'utg003244l_pilon',
    'utg003334l_pilon', 'utg003519l_pilon', 'utg003588l_pilon',
    'utg003661l_pilon', 'utg003764l_pilon', 'utg003937l_pilon',
    'utg004617l_pilon', 'utg004646l_pilon', 'utg005233l_pilon',
    'utg005296l_pilon'
]
list22 = [
    'utg000045l_pilon', 'utg000090l_pilon', 'utg000128l_pilon',
    'utg000254l_pilon', 'utg000335l_pilon', 'utg000729l_pilon_1_400000',
    'utg000729l_pilon_400001_410000', 'utg000729l_pilon_410001_2476576',
    'utg000910l_pilon', 'utg001078l_pilon', 'utg001172l_pilon',
    'utg001644l_pilon', 'utg001739l_pilon', 'utg001869l_pilon_1_540000',
    'utg001869l_pilon_540001_550000', 'utg001869l_pilon_550001_1043015',
    'utg001962l_pilon', 'utg002648l_pilon', 'utg004244l_pilon',
    'utg005492l_pilon', 'utg001302l_pilon_800001_2960000'
]
list23 = [
    'utg000047l_pilon', 'utg000408l_pilon', 'utg000440l_pilon_1_410000',
    'utg000440l_pilon_410001_420000', 'utg000440l_pilon_420001_1607742',
    'utg000556l_pilon', 'utg000596l_pilon', 'utg000622l_pilon',
    'utg000964l_pilon', 'utg001702l_pilon', 'utg001880l_pilon_1_60000',
    'utg001880l_pilon_60001_80000', 'utg001880l_pilon_80001_269907',
    'utg001890l_pilon', 'utg001983l_pilon', 'utg002386l_pilon',
    'utg002437l_pilon', 'utg004024l_pilon', 'utg004463l_pilon',
    'utg004546l_pilon', 'utg000571l_pilon_670001_3340000'
]
list24 = [
    'utg000050l_pilon', 'utg000550l_pilon', 'utg000605l_pilon',
    'utg000726l_pilon', 'utg001342l_pilon', 'utg001505l_pilon',
    'utg001845l_pilon', 'utg002008l_pilon', 'utg002043l_pilon',
    'utg002780l_pilon', 'utg003152l_pilon', 'utg003284l_pilon',
    'utg003671l_pilon', 'utg004072l_pilon', 'utg005075l_pilon',
    'utg000029l_pilon_1_3050000', 'utg000243l_pilon_1120001_4890000',
    'utg000243l_pilon_6840001_9050000', 'utg000267l_pilon_1150001_4200000',
    'utg000406l_pilon_2960001_5489075', 'utg000568l_pilon_1_4560000'
]
list25 = [
    'utg000053l_pilon', 'utg000163l_pilon', 'utg000206l_pilon',
    'utg000402l_pilon', 'utg000466l_pilon', 'utg000471l_pilon',
    'utg000507l_pilon', 'utg000821l_pilon_1_50000',
    'utg000821l_pilon_50001_70000', 'utg000821l_pilon_70001_673005',
    'utg000965l_pilon', 'utg001012l_pilon', 'utg001573l_pilon',
    'utg001791l_pilon', 'utg001800l_pilon', 'utg001935l_pilon',
    'utg002882l_pilon', 'utg000549l_pilon_20001_4440000'
]
list26 = [
    'utg000055l_pilon', 'utg000148l_pilon', 'utg000167l_pilon',
    'utg000245l_pilon', 'utg000281l_pilon', 'utg000313l_pilon_1_8650000',
    'utg000313l_pilon_8650001_8660000', 'utg000313l_pilon_8660001_8666052',
    'utg000343l_pilon', 'utg000345l_pilon', 'utg000378l_pilon',
    'utg000393l_pilon', 'utg000419l_pilon', 'utg000437l_pilon',
    'utg000491l_pilon', 'utg000508l_pilon_1_660000',
    'utg000508l_pilon_660001_670000', 'utg000508l_pilon_670001_674928',
    'utg000554l_pilon', 'utg000560l_pilon', 'utg000676l_pilon',
    'utg000695l_pilon', 'utg000705l_pilon', 'utg000713l_pilon',
    'utg001008l_pilon', 'utg001047l_pilon', 'utg001220l_pilon',
    'utg001283l_pilon_1_290000', 'utg001283l_pilon_290001_300000',
    'utg001283l_pilon_300001_305060', 'utg001308l_pilon', 'utg001343l_pilon',
    'utg001514l_pilon', 'utg001666l_pilon', 'utg001700l_pilon',
    'utg001795l_pilon', 'utg001902l_pilon', 'utg001915l_pilon',
    'utg002459l_pilon', 'utg002835l_pilon', 'utg002863l_pilon_1_10000',
    'utg002863l_pilon_10001_30000', 'utg002863l_pilon_30001_218689',
    'utg003052l_pilon', 'utg003860l_pilon', 'utg000175l_pilon_10001_2840000'
]
list27 = [
    'utg000097l_pilon', 'utg000170l_pilon', 'utg000222l_pilon',
    'utg000242l_pilon', 'utg000306l_pilon', 'utg000383l_pilon',
    'utg000401l_pilon', 'utg000418l_pilon_1_12110000',
    'utg000418l_pilon_12110001_12137239', 'utg000587l_pilon',
    'utg000652l_pilon', 'utg000815l_pilon', 'utg000926l_pilon',
    'utg001108l_pilon', 'utg001115l_pilon', 'utg001137l_pilon',
    'utg001233l_pilon', 'utg001272l_pilon', 'utg001696l_pilon',
    'utg001892l_pilon_1_10000', 'utg001892l_pilon_10001_20000',
    'utg001892l_pilon_20001_181232', 'utg002118l_pilon', 'utg002284l_pilon',
    'utg002438l_pilon', 'utg002495l_pilon', 'utg002509l_pilon',
    'utg002609l_pilon', 'utg002808l_pilon', 'utg003532l_pilon',
    'utg004532l_pilon', 'utg004723l_pilon', 'utg006926l_pilon'
]
list28 = [
    'utg000105l_pilon', 'utg000184l_pilon', 'utg000341l_pilon',
    'utg000582l_pilon', 'utg000998l_pilon', 'utg001204l_pilon',
    'utg001311l_pilon', 'utg001391l_pilon', 'utg001578l_pilon',
    'utg001591l_pilon', 'utg001623l_pilon', 'utg001708l_pilon',
    'utg001879l_pilon', 'utg002124l_pilon', 'utg002550l_pilon',
    'utg002713l_pilon', 'utg002841l_pilon', 'utg004161l_pilon_1_10000',
    'utg004161l_pilon_10001_20000', 'utg004161l_pilon_20001_290676',
    'utg004461l_pilon', 'utg000048l_pilon_20001_3620000',
    'utg000086l_pilon_10001_2790000'
]
list29 = [
    'utg000106l_pilon', 'utg000391l_pilon_1_570000',
    'utg000391l_pilon_570001_580000', 'utg000391l_pilon_580001_1261836',
    'utg000493l_pilon', 'utg000623l_pilon', 'utg000855l_pilon',
    'utg000865l_pilon_1_10000', 'utg000865l_pilon_10001_30000',
    'utg000865l_pilon_30001_789969', 'utg000943l_pilon', 'utg001005l_pilon',
    'utg001010l_pilon', 'utg001217l_pilon', 'utg001218l_pilon',
    'utg001234l_pilon', 'utg001298l_pilon', 'utg001435l_pilon',
    'utg001814l_pilon', 'utg001875l_pilon', 'utg001916l_pilon',
    'utg002273l_pilon', 'utg002346l_pilon', 'utg002408l_pilon',
    'utg002728l_pilon', 'utg002923l_pilon', 'utg003514l_pilon',
    'utg005428l_pilon'
]
list30 = [
    'utg000108l_pilon_1_2030000', 'utg000108l_pilon_2030001_2040000',
    'utg000108l_pilon_2040001_2050619', 'utg000240l_pilon', 'utg001307l_pilon',
    'utg001333l_pilon_1_10000', 'utg001333l_pilon_10001_1022706',
    'utg001422l_pilon', 'utg002527l_pilon', 'utg002959l_pilon',
    'utg000103l_pilon_550001_3440000', 'utg000452l_pilon_10001_2560000'
]
list31 = [
    'utg000115l_pilon', 'utg000117l_pilon', 'utg000138l_pilon',
    'utg000165l_pilon_1_20000', 'utg000165l_pilon_20001_1661595',
    'utg000179l_pilon', 'utg000203l_pilon', 'utg000342l_pilon',
    'utg000395l_pilon', 'utg000423l_pilon_1_2600000',
    'utg000423l_pilon_2600001_2620000', 'utg000423l_pilon_2620001_2968026',
    'utg000498l_pilon', 'utg000597l_pilon', 'utg000716l_pilon',
    'utg000737l_pilon', 'utg000894l_pilon', 'utg001014l_pilon',
    'utg001432l_pilon', 'utg001465l_pilon', 'utg001742l_pilon_1_350000',
    'utg001742l_pilon_350001_360000', 'utg001742l_pilon_360001_371278',
    'utg001988l_pilon', 'utg002266l_pilon', 'utg002483l_pilon',
    'utg002601l_pilon', 'utg002962l_pilon', 'utg003424l_pilon',
    'utg003626l_pilon', 'utg004146l_pilon', 'utg004320l_pilon'
]
list32 = [
    'utg000124l_pilon', 'utg000633l_pilon_1_310000',
    'utg000633l_pilon_310001_320000', 'utg000633l_pilon_320001_6454187',
    'utg000885l_pilon', 'utg000908l_pilon', 'utg001057l_pilon',
    'utg001151l_pilon', 'utg001169l_pilon', 'utg001191l_pilon',
    'utg001373l_pilon', 'utg001493l_pilon', 'utg001628l_pilon',
    'utg001661l_pilon', 'utg001670l_pilon', 'utg001836l_pilon',
    'utg002711l_pilon'
]
list33 = [
    'utg000126l_pilon', 'utg000180l_pilon', 'utg000327l_pilon',
    'utg000405l_pilon', 'utg000746l_pilon', 'utg000863l_pilon',
    'utg001058l_pilon', 'utg001096l_pilon', 'utg001281l_pilon',
    'utg001437l_pilon', 'utg001459l_pilon', 'utg001461l_pilon',
    'utg002016l_pilon', 'utg002454l_pilon', 'utg002805l_pilon',
    'utg004215l_pilon', 'utg004218l_pilon', 'utg004424l_pilon',
    'utg006403l_pilon', 'utg000024l_pilon_1_2180000',
    'utg000024l_pilon_2200001_10680000', 'utg000082l_pilon_180001_3110000',
    'utg000082l_pilon_3540001_6430000', 'utg000220l_pilon_20001_2548736',
    'utg000723l_pilon_1580001_4380000', 'utg001029l_pilon_10001_2380000'
]
list34 = [
    'utg000127l_pilon', 'utg000505l_pilon_1_10000',
    'utg000505l_pilon_10001_680889', 'utg000591l_pilon', 'utg000694l_pilon',
    'utg000794l_pilon_1_420000', 'utg000794l_pilon_420001_440000',
    'utg000794l_pilon_440001_516294', 'utg000831l_pilon', 'utg000841l_pilon',
    'utg000870l_pilon_1_600000', 'utg000870l_pilon_600001_620000',
    'utg000870l_pilon_620001_1465585', 'utg001499l_pilon', 'utg001982l_pilon',
    'utg002014l_pilon', 'utg002159l_pilon', 'utg002245l_pilon',
    'utg002287l_pilon_1_10000', 'utg002287l_pilon_10001_128468',
    'utg002413l_pilon', 'utg000005l_pilon_10001_2400000',
    'utg000005l_pilon_3620001_5900000', 'utg000005l_pilon_5910001_10500000',
    'utg000099l_pilon_10001_2760000', 'utg000227l_pilon_10001_2170000',
    'utg000277l_pilon_20001_3570000', 'utg000323l_pilon_1840001_5260000',
    'utg000323l_pilon_5280001_9160000', 'utg000902l_pilon_10001_3400000'
]
list35 = [
    'utg000136l_pilon', 'utg000278l_pilon', 'utg000813l_pilon',
    'utg000822l_pilon', 'utg000973l_pilon', 'utg001396l_pilon',
    'utg001491l_pilon_1_1000000', 'utg001491l_pilon_1000001_1020000',
    'utg001491l_pilon_1020001_1747875', 'utg001595l_pilon', 'utg002165l_pilon',
    'utg002199l_pilon', 'utg002687l_pilon', 'utg002691l_pilon'
]
list36 = [
    'utg000139l_pilon_1_10000', 'utg000139l_pilon_10001_4406762',
    'utg000160l_pilon', 'utg000247l_pilon', 'utg000322l_pilon',
    'utg000368l_pilon', 'utg000594l_pilon', 'utg000901l_pilon',
    'utg000925l_pilon', 'utg001323l_pilon', 'utg001615l_pilon',
    'utg001807l_pilon', 'utg001919l_pilon', 'utg002330l_pilon',
    'utg002347l_pilon', 'utg002587l_pilon', 'utg002721l_pilon',
    'utg003571l_pilon', 'utg007303l_pilon'
]
list37 = [
    'utg000146l_pilon', 'utg000153l_pilon', 'utg000195l_pilon',
    'utg000248l_pilon', 'utg000301l_pilon', 'utg000334l_pilon',
    'utg000496l_pilon', 'utg000524l_pilon', 'utg000529l_pilon',
    'utg000559l_pilon', 'utg000628l_pilon', 'utg000639l_pilon',
    'utg000658l_pilon', 'utg000765l_pilon', 'utg000886l_pilon_1_10000',
    'utg000886l_pilon_10001_20000', 'utg000886l_pilon_20001_30000',
    'utg000886l_pilon_30001_1060310', 'utg000891l_pilon', 'utg001069l_pilon',
    'utg001128l_pilon', 'utg001132l_pilon', 'utg001265l_pilon',
    'utg001428l_pilon_1_140000', 'utg001428l_pilon_140001_150000',
    'utg001428l_pilon_150001_170000', 'utg001428l_pilon_170001_180000',
    'utg001428l_pilon_180001_268687', 'utg001457l_pilon', 'utg002427l_pilon',
    'utg002534l_pilon', 'utg002575l_pilon_1_50000',
    'utg002575l_pilon_50001_60000', 'utg002575l_pilon_60001_118489',
    'utg003035l_pilon', 'utg003234l_pilon', 'utg003683l_pilon',
    'utg004178l_pilon_1_10000', 'utg004178l_pilon_10001_149264',
    'utg004877l_pilon'
]
list38 = [
    'utg000159l_pilon', 'utg000217l_pilon', 'utg000376l_pilon',
    'utg000460l_pilon', 'utg000492l_pilon', 'utg000598l_pilon',
    'utg000666l_pilon', 'utg000719l_pilon', 'utg000800l_pilon',
    'utg000805l_pilon', 'utg000953l_pilon', 'utg001088l_pilon',
    'utg001119l_pilon', 'utg001195l_pilon', 'utg001261l_pilon',
    'utg001294l_pilon', 'utg001316l_pilon', 'utg001322l_pilon',
    'utg001478l_pilon', 'utg001643l_pilon', 'utg001849l_pilon',
    'utg001932l_pilon', 'utg002593l_pilon', 'utg003512l_pilon',
    'utg003729l_pilon'
]
list39 = [
    'utg000173l_pilon', 'utg000216l_pilon', 'utg000264l_pilon',
    'utg000499l_pilon', 'utg000692l_pilon', 'utg000854l_pilon',
    'utg001026l_pilon', 'utg001926l_pilon', 'utg002183l_pilon',
    'utg002430l_pilon', 'utg002666l_pilon', 'utg006881l_pilon',
    'utg001302l_pilon_800001_2960000'
]
list40 = [
    'utg000223l_pilon_1_20000', 'utg000223l_pilon_20001_940093',
    'utg000282l_pilon', 'utg000349l_pilon_1_10000',
    'utg000349l_pilon_10001_30000', 'utg000349l_pilon_30001_743328',
    'utg000640l_pilon', 'utg000996l_pilon', 'utg001068l_pilon',
    'utg001494l_pilon', 'utg001540l_pilon_1_10000',
    'utg001540l_pilon_10001_30000', 'utg001540l_pilon_30001_316704',
    'utg001685l_pilon', 'utg001780l_pilon', 'utg002407l_pilon',
    'utg002702l_pilon', 'utg003955l_pilon', 'utg004716l_pilon',
    'utg005920l_pilon', 'utg006711l_pilon', 'utg000048l_pilon_20001_3620000',
    'utg000086l_pilon_10001_2790000'
]
list41 = [
    'utg000274l_pilon', 'utg000316l_pilon_1_860000',
    'utg000316l_pilon_860001_870000', 'utg000316l_pilon_870001_1279194',
    'utg000377l_pilon_1_1410000', 'utg000377l_pilon_1410001_1430000',
    'utg000377l_pilon_1430001_7753866', 'utg000399l_pilon', 'utg000525l_pilon',
    'utg000526l_pilon', 'utg000572l_pilon', 'utg000575l_pilon',
    'utg000585l_pilon', 'utg000625l_pilon', 'utg000645l_pilon_1_120000',
    'utg000645l_pilon_120001_131194', 'utg000660l_pilon', 'utg000909l_pilon',
    'utg000944l_pilon', 'utg001118l_pilon_1_460000',
    'utg001118l_pilon_460001_470000', 'utg001118l_pilon_470001_1642402',
    'utg001314l_pilon', 'utg001626l_pilon', 'utg002000l_pilon',
    'utg002320l_pilon_1_10000', 'utg002320l_pilon_10001_430677',
    'utg002798l_pilon', 'utg005892l_pilon'
]
list42 = [
    'utg000287l_pilon', 'utg000428l_pilon', 'utg000624l_pilon',
    'utg000677l_pilon', 'utg001027l_pilon', 'utg001469l_pilon',
    'utg000198l_pilon_30001_3150000', 'utg000576l_pilon_10001_2190000',
    'utg000923l_pilon_10001_2210000'
]
list43 = [
    'utg000298l_pilon', 'utg000398l_pilon', 'utg000517l_pilon',
    'utg000739l_pilon', 'utg000752l_pilon', 'utg000774l_pilon',
    'utg000872l_pilon_1_210000', 'utg000872l_pilon_210001_220000',
    'utg000872l_pilon_220001_232980', 'utg000883l_pilon',
    'utg001037l_pilon_1_10000', 'utg001037l_pilon_10001_20000',
    'utg001037l_pilon_20001_191590', 'utg001044l_pilon', 'utg001109l_pilon',
    'utg001177l_pilon', 'utg001223l_pilon', 'utg001331l_pilon',
    'utg001449l_pilon', 'utg001526l_pilon', 'utg001681l_pilon_1_530000',
    'utg001681l_pilon_530001_540000', 'utg001681l_pilon_540001_550000',
    'utg001681l_pilon_550001_559816', 'utg001743l_pilon', 'utg001806l_pilon',
    'utg001993l_pilon', 'utg002004l_pilon', 'utg002011l_pilon',
    'utg002020l_pilon', 'utg002130l_pilon', 'utg002514l_pilon',
    'utg002668l_pilon', 'utg002785l_pilon_1_160000',
    'utg002785l_pilon_160001_170000', 'utg002785l_pilon_170001_177881',
    'utg003331l_pilon', 'utg003467l_pilon_1_330000',
    'utg003467l_pilon_330001_340000', 'utg003467l_pilon_340001_354032',
    'utg003782l_pilon', 'utg000691l_pilon_10001_2310000'
]
list44 = [
    'utg000311l_pilon', 'utg000546l_pilon', 'utg000768l_pilon',
    'utg000776l_pilon', 'utg000844l_pilon', 'utg000931l_pilon',
    'utg001042l_pilon', 'utg001072l_pilon', 'utg001148l_pilon',
    'utg001188l_pilon', 'utg001240l_pilon', 'utg001253l_pilon',
    'utg003516l_pilon', 'utg000024l_pilon_1_2180000',
    'utg000024l_pilon_2200001_10680000', 'utg000082l_pilon_180001_3110000',
    'utg000082l_pilon_3540001_6430000', 'utg000220l_pilon_20001_2548736',
    'utg000723l_pilon_1580001_4380000', 'utg001029l_pilon_10001_2380000'
]
list45 = [
    'utg000396l_pilon', 'utg000485l_pilon', 'utg000518l_pilon',
    'utg000579l_pilon', 'utg000840l_pilon', 'utg001256l_pilon',
    'utg001541l_pilon', 'utg001713l_pilon', 'utg001820l_pilon',
    'utg002186l_pilon', 'utg004975l_pilon', 'utg000576l_pilon_10001_2190000',
    'utg000923l_pilon_10001_2210000'
]
list46 = [
    'utg000538l_pilon', 'utg000564l_pilon', 'utg000796l_pilon',
    'utg001409l_pilon', 'utg001558l_pilon', 'utg001656l_pilon',
    'utg002148l_pilon', 'utg002221l_pilon', 'utg002789l_pilon',
    'utg003262l_pilon', 'utg003288l_pilon', 'utg003561l_pilon',
    'utg000103l_pilon_550001_3440000', 'utg000452l_pilon_10001_2560000'
]
list47 = [
    'utg001028l_pilon', 'utg002305l_pilon', 'utg002806l_pilon',
    'utg002834l_pilon_1_20000', 'utg002834l_pilon_20001_230348',
    'utg000076l_pilon_70001_2510000'
]
list48 = [
    'utg000071l_pilon', 'utg000109l_pilon_1_1940000',
    'utg000109l_pilon_1940001_1950000', 'utg000109l_pilon_1950001_1955116',
    'utg000130l_pilon', 'utg000189l_pilon', 'utg000207l_pilon',
    'utg000210l_pilon', 'utg000256l_pilon', 'utg000480l_pilon',
    'utg000486l_pilon', 'utg000688l_pilon', 'utg000702l_pilon',
    'utg000733l_pilon', 'utg000748l_pilon', 'utg000846l_pilon',
    'utg000921l_pilon', 'utg000995l_pilon', 'utg001063l_pilon',
    'utg001089l_pilon', 'utg001159l_pilon', 'utg001289l_pilon',
    'utg001318l_pilon_1_1010000', 'utg001318l_pilon_1010001_1020000',
    'utg001318l_pilon_1020001_1687351', 'utg001356l_pilon', 'utg001390l_pilon',
    'utg001439l_pilon', 'utg001539l_pilon', 'utg001563l_pilon',
    'utg001607l_pilon', 'utg001676l_pilon_1_240000',
    'utg001676l_pilon_240001_250000', 'utg001676l_pilon_250001_254045',
    'utg001724l_pilon', 'utg001774l_pilon', 'utg001866l_pilon',
    'utg001899l_pilon', 'utg001969l_pilon', 'utg002012l_pilon',
    'utg002105l_pilon', 'utg002151l_pilon', 'utg002280l_pilon',
    'utg002357l_pilon', 'utg000175l_pilon_10001_2840000',
    'utg000336l_pilon_40001_2280000', 'utg000536l_pilon_20001_2530000',
    'utg000990l_pilon_480001_3270000'
]

homoDict = {
    'G1': ['list5', 'list11', 'list42', 'list45'],
    'G2': ['list8', 'list12', 'list27', 'list31'],
    'G3': ['list13', 'list14', 'list18', 'list21'],
    'G4': ['list15', 'list17', 'list23', 'list36'],
    'G5': ['list9', 'list19', 'list29', 'list43'],
    'G6': ['list6', 'list20', 'list26', 'list48'],
    'G7': ['list7', 'list22', 'list24', 'list39'],
    'G8': ['list4', 'list25', 'list37', 'list38'],
    'G9': ['list16', 'list28', 'list40', 'list41'],
    'G10': ['list2', 'list3', 'list35', 'list47'],
    'G11': ['list10', 'list30', 'list32', 'list46'],
    'G12': ['list1', 'list33', 'list34', 'list44']
}

# 得到已经聚类好的utg[notHap]的id_size_type ————> 310.utgNotHapType.done.txt

listId = [
    list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,
    list11, list12, list13, list14, list15, list16, list17, list18, list19,
    list20, list21, list22, list23, list24, list25, list26, list27, list28,
    list29, list30, list31, list32, list33, list34, list35, list36, list37,
    list38, list39, list40, list41, list42, list43, list44, list45, list46,
    list47, list48
]


# 创建嵌套的列表 [[...],[...],[...],[...],[...],[...]]
def createMerged_48_list():
    merged_48_list = [[] for _ in range(48)]
    for id in range(48):
        merged_48_list[id] = listId[id]
    return merged_48_list


# merged_list ——> 48个list的总合集
merged_list = sum([
    list1, list2, list3, list4, list5, list6, list7, list8, list9, list10,
    list11, list12, list13, list14, list15, list16, list17, list18, list19,
    list20, list21, list22, list23, list24, list25, list26, list27, list28,
    list29, list30, list31, list32, list33, list34, list35, list36, list37,
    list38, list39, list40, list41, list42, list43, list44, list45, list46,
    list47, list48
], [])


# 得到某个utg的分组与权重的字典
def getGroup(hicNormalFilePath):
    utgInfoDict = defaultdict(int)
    tmpInfoDict = defaultdict(int)
    tmpList = []
    with open(hicNormalFilePath, 'r', encoding='utf-8') as mf:
        lines = mf.readlines()
        for line in lines:
            splits = line.strip().split()
            groupId = ''.join(re.findall(r'\d+', splits[2]))
            utgName = splits[0]
            if utgName not in tmpInfoDict:
                tmpInfoDict[utgName] = [groupId]
            else:
                tmpInfoDict[utgName].append(groupId)
                # {'utg001l_pilon': {'25',45}, 'utg002l_pilon': {'13',46}}
        for utgName in tmpInfoDict.keys():
            for index, groupId in enumerate(tmpInfoDict[utgName]):
                weight = str(48 - index)
                groupId_weight = {'list' + groupId: weight}
                tmpList.append(groupId_weight)
                utgInfoDict[utgName] = tmpList
            tmpList = []
        return utgInfoDict
    # {'utg001l_pilon': [{'list1':'48'}, {'list34':'47'}...], 'utg002l_pilon': [{'list2':'48'}, {'list45':'47'}...]}
    # 上面分组是按照顺序排列的


# 确定utg的最后分组——>读文件310.utgType.will_220k_235k.txt——>写入文件result.tmp.txt
def selectGroup(filePath,filePath1,filePath2):
    '''
    utg001l_pilon 类型为trip 在G1(list1 list2 list3)的权重为: 555
    '''
    utgTypeDict = {}
    utgInfoDict = getGroup(hicNormalFilePath)
    # {'utg001l_pilon': [{'list1':'48'}, {'list34':'47'}...], 'utg002l_pilon': [{'list2':'48'}, {'list45':'47'}...]}
    utgInfoDict_new = {}
    for utgName, tmplist in utgInfoDict.items():
        listDict = {}
        for tempDict in tmplist:
            listDict.update(tempDict)
        utgInfoDict_new[utgName] = listDict
    # {'utg001l_pilon':{'list1':'48','list34':'47'}, 'utg002l_pilon':{'list2':'48','list45':'47'}}
    tmpId = []  # 匹配上G1的['list5','list11']
    tmpWeight = 0  # 匹配上G1的list的权重和
    with open(filePath, 'r') as mf, \
            open(filePath1, 'w') as fw1, \
            open(filePath2, 'w') as fw2:
        '''
            310.utgType.will_220k_235k.txt  [utg length type]
            result.tmp0.txt:  utg007l 在G1...G12分别的权重  ——————只有dip和trip
            result.tmp0.txt:  utg007l 在G1...G12找一个最大的G的权重  ——————四种类型都有~最后文件~
        '''
        lines = mf.readlines()
        for line in lines:
            splits = line.strip().split()
            utgTypeDict[splits[0]] = splits[2]
            # {'utg000007l_pilon_1_1420000':hap}
        for utgName, utgType in utgTypeDict.items():
            if utgName in utgInfoDict.keys():
                if utgType == 'hap':
                    selectGroup = 1
                    idList = []
                    for id, weight in utgInfoDict_new[utgName].items():
                        idList.append(id)
                    groupIdLast = idList[0]  # [{'list1':'48'}]
                    groupWeightLast = utgInfoDict_new[utgName][groupIdLast]

                    for key in homoDict.keys():
                        if groupIdLast in homoDict[key]:
                            group_G = key

                    fw2.write(
                        utgName + ' 类型为' + utgType + ' 在' + group_G + '(' + groupIdLast + ')的权重为  :' + groupWeightLast + '\n')
                elif utgType == 'dip':
                    # 把12组里面权重最大的两个list+权重输出
                    selectGroup = 2
                    tmpId = []
                    # {'G1': ['list5', 'list11', 'list42', 'list45'],...}
                    for key in homoDict.keys():  # 自己定义的G1-G12
                        if utgName in utgInfoDict_new.keys():  # {'utg001l_pilon':{'list1':'48','list34':'47'},...}
                            for listId, weight in utgInfoDict_new[utgName].items():
                                if len(tmpId) < selectGroup:
                                    if listId in homoDict[key]:
                                        if len(tmpId) == 0:
                                            tmpId = [listId]
                                            tmpWeight += int(weight)
                                        else:
                                            tmpId.append(listId)
                                            tmpWeight += int(weight)
                            if len(tmpId) == selectGroup:  # 2
                                fw1.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                                          tmpId[1] + ')''的权重为: ' + str(tmpWeight) + '\n')
                            tmpId = []
                            tmpWeight = 0


                elif utgType == 'trip':
                    # 把12组里面权重最大的三个list+权重输出
                    selectGroup = 3
                    tmpId = []
                    # {'G1': ['list5', 'list11', 'list42', 'list45'],...}
                    for key in homoDict.keys():  # 自己定义的G1-G12
                        if utgName in utgInfoDict_new.keys():  # {'utg001l_pilon':{'list1':'48','list34':'47'},...}
                            for listId, weight in utgInfoDict_new[utgName].items():
                                if len(tmpId) < selectGroup:
                                    if listId in homoDict[key]:
                                        if len(tmpId) == 0:
                                            tmpId = [listId]
                                            tmpWeight += int(weight)
                                        else:
                                            tmpId.append(listId)
                                            tmpWeight += int(weight)
                            if len(tmpId) == selectGroup:  # 3
                                fw1.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                                          tmpId[1] + ',' + tmpId[2] + ')的权重为: ' + str(tmpWeight) + '\n')
                            tmpId = []
                            tmpWeight = 0
                elif utgType == 'tetrap':
                    selectGroup = 4
                    for key in homoDict.keys():  # 自己定义的G1-G12
                        if utgName in utgInfoDict_new.keys():  # {'utg001l_pilon':{'list1':'48','list34':'47'},...}
                            for listId, weight in utgInfoDict_new[utgName].items():
                                if len(tmpId) <= selectGroup:
                                    if listId in homoDict[key]:
                                        if len(tmpId) == 0:
                                            tmpId = [listId]
                                            tmpWeight += int(weight)
                                        else:
                                            tmpId.append(listId)
                                            tmpWeight += int(weight)
                            if len(tmpId) == selectGroup:
                                fw1.write(utgName + ' 类型为' + utgTypeDict[utgName] + ' 在' + key + '(' + tmpId[0] + ',' +
                                          tmpId[1] + ',' + tmpId[2] + ',' + tmpId[3] + ')的权重为: ' + str(
                                    tmpWeight) + '\n')
                            tmpId = []
                            tmpWeight = 0
                else:
                    pass


# 按照每个UtgId对12个组的关系从大到小排序
def readTmp0Sorted(file1,file2):
    lineData = []
    with open(file1, 'r') as fr, \
            open(file2, 'a') as fw2:
        lines = fr.readlines()
        # 对每12行排序
        for i in range(0, len(lines), 12):
            for line in lines:
                # splits = line.strip().split()
                # lineData.append(line)
                lineData = lines[i:i + 12]
            lineData.sort(key=lambda line: int(line.strip().split()[-1]), reverse=True)
            fw2.write(lineData[0])
            lineData = []


if __name__ == '__main__':
    filePath = 'diff_willUtg_350.txt'
    hicNormalFilePath = 'hic_normal.new.txt'
    filePath1, filePath2 = 'utg_group_350_hic.0.txt' , 'utg_group_350_hic.txt'
    selectGroup(filePath, filePath1, filePath2)
    readTmp0Sorted(filePath1, filePath2)
    # result.tmp1.txt ——> utg_group_310_hic.txt
