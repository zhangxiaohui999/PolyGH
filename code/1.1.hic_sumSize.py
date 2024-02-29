from collections import defaultdict
import re


def write(filePath, content):
    with open(filePath, mode='a') as f:
        f.write(content)


list1 = [
    'utg000001l_pilon', 'utg000070l_pilon', 'utg000134l_pilon',
    'utg001062l_pilon', 'utg001654l_pilon', 'utg002268l_pilon'
]
list2 = [
    'utg000002l_pilon', 'utg000056l_pilon', 'utg000062l_pilon',
    'utg000145l_pilon', 'utg000219l_pilon', 'utg000459l_pilon',
    'utg000932l_pilon', 'utg000983l_pilon', 'utg001073l_pilon',
    'utg002375l_pilon', 'utg003478l_pilon'
]
list3 = [
    'utg000003l_pilon', 'utg000036l_pilon', 'utg000617l_pilon',
    'utg000708l_pilon', 'utg001264l_pilon', 'utg001551l_pilon',
    'utg001720l_pilon', 'utg002132l_pilon'
]
list4 = [
    'utg000004l_pilon', 'utg000038l_pilon', 'utg000067l_pilon',
    'utg000131l_pilon', 'utg000178l_pilon', 'utg000200l_pilon',
    'utg000251l_pilon', 'utg000348l_pilon', 'utg000367l_pilon',
    'utg000379l_pilon', 'utg000514l_pilon', 'utg000627l_pilon',
    'utg000697l_pilon', 'utg000770l_pilon', 'utg000772l_pilon',
    'utg000773l_pilon', 'utg000783l_pilon', 'utg000823l_pilon',
    'utg000957l_pilon', 'utg001336l_pilon', 'utg001492l_pilon',
    'utg001544l_pilon', 'utg001754l_pilon', 'utg001808l_pilon',
    'utg001941l_pilon', 'utg002488l_pilon', 'utg002708l_pilon',
    'utg002712l_pilon', 'utg002755l_pilon', 'utg002865l_pilon',
    'utg002993l_pilon', 'utg003793l_pilon', 'utg004154l_pilon',
    'utg004433l_pilon'
]
list5 = [
    'utg000006l_pilon', 'utg000475l_pilon', 'utg000537l_pilon',
    'utg000809l_pilon', 'utg000967l_pilon', 'utg000978l_pilon',
    'utg001040l_pilon', 'utg001227l_pilon', 'utg001361l_pilon',
    'utg001455l_pilon', 'utg006357l_pilon'
]
list6 = [
    'utg000007l_pilon', 'utg000129l_pilon', 'utg000172l_pilon',
    'utg000193l_pilon', 'utg000229l_pilon', 'utg000253l_pilon',
    'utg000269l_pilon', 'utg000286l_pilon', 'utg000303l_pilon',
    'utg000324l_pilon', 'utg000352l_pilon', 'utg000356l_pilon',
    'utg000442l_pilon', 'utg000458l_pilon', 'utg000473l_pilon',
    'utg000488l_pilon', 'utg000522l_pilon', 'utg000541l_pilon',
    'utg000612l_pilon', 'utg000673l_pilon', 'utg000763l_pilon',
    'utg000843l_pilon', 'utg001110l_pilon', 'utg001143l_pilon',
    'utg001178l_pilon', 'utg001228l_pilon', 'utg001249l_pilon',
    'utg001319l_pilon', 'utg001335l_pilon', 'utg001527l_pilon',
    'utg001528l_pilon', 'utg001606l_pilon', 'utg001662l_pilon',
    'utg001688l_pilon', 'utg001710l_pilon', 'utg001996l_pilon',
    'utg002037l_pilon', 'utg002079l_pilon', 'utg002198l_pilon',
    'utg002531l_pilon', 'utg002660l_pilon', 'utg002788l_pilon',
    'utg002930l_pilon', 'utg002940l_pilon', 'utg002945l_pilon',
    'utg003070l_pilon', 'utg003866l_pilon', 'utg004025l_pilon',
    'utg004096l_pilon', 'utg004253l_pilon', 'utg004680l_pilon',
    'utg005430l_pilon'
]
list7 = [
    'utg000008l_pilon', 'utg000272l_pilon', 'utg000592l_pilon',
    'utg000674l_pilon', 'utg000934l_pilon', 'utg001112l_pilon',
    'utg001255l_pilon', 'utg001296l_pilon', 'utg001482l_pilon',
    'utg001508l_pilon', 'utg001536l_pilon', 'utg001753l_pilon',
    'utg003578l_pilon', 'utg003641l_pilon'
]
list8 = [
    'utg000009l_pilon', 'utg000061l_pilon', 'utg000075l_pilon',
    'utg000121l_pilon', 'utg000260l_pilon', 'utg000275l_pilon',
    'utg000441l_pilon', 'utg000599l_pilon', 'utg000647l_pilon',
    'utg000793l_pilon', 'utg000829l_pilon', 'utg000938l_pilon',
    'utg000962l_pilon', 'utg001213l_pilon', 'utg001413l_pilon',
    'utg001436l_pilon', 'utg001533l_pilon', 'utg001682l_pilon',
    'utg001705l_pilon', 'utg001756l_pilon', 'utg001833l_pilon',
    'utg002110l_pilon', 'utg002227l_pilon', 'utg002559l_pilon',
    'utg002968l_pilon', 'utg003917l_pilon', 'utg004079l_pilon',
    'utg005590l_pilon'
]
list9 = [
    'utg000010l_pilon', 'utg000155l_pilon', 'utg000238l_pilon',
    'utg000351l_pilon', 'utg000354l_pilon', 'utg000412l_pilon',
    'utg000425l_pilon', 'utg000433l_pilon', 'utg000449l_pilon',
    'utg000795l_pilon', 'utg000836l_pilon', 'utg001017l_pilon',
    'utg001045l_pilon', 'utg001085l_pilon', 'utg001125l_pilon',
    'utg001175l_pilon', 'utg001250l_pilon', 'utg001434l_pilon',
    'utg002083l_pilon', 'utg003008l_pilon', 'utg003104l_pilon',
    'utg003208l_pilon', 'utg003567l_pilon', 'utg004942l_pilon'
]
list10 = [
    'utg000011l_pilon', 'utg000065l_pilon', 'utg000094l_pilon',
    'utg000257l_pilon', 'utg000631l_pilon', 'utg000689l_pilon',
    'utg000711l_pilon', 'utg001022l_pilon', 'utg001149l_pilon',
    'utg001171l_pilon', 'utg001221l_pilon', 'utg001259l_pilon',
    'utg001495l_pilon', 'utg001518l_pilon', 'utg001560l_pilon',
    'utg001671l_pilon', 'utg001712l_pilon', 'utg001768l_pilon',
    'utg001825l_pilon', 'utg002109l_pilon', 'utg002484l_pilon',
    'utg002745l_pilon', 'utg003565l_pilon', 'utg003746l_pilon'
]
list11 = [
    'utg000012l_pilon', 'utg000064l_pilon', 'utg000249l_pilon',
    'utg000670l_pilon', 'utg001236l_pilon', 'utg001412l_pilon',
    'utg001590l_pilon', 'utg001641l_pilon', 'utg001839l_pilon',
    'utg002029l_pilon', 'utg002206l_pilon', 'utg002282l_pilon',
    'utg002390l_pilon', 'utg002608l_pilon', 'utg002980l_pilon',
    'utg003633l_pilon', 'utg003639l_pilon'
]
list12 = [
    'utg000013l_pilon', 'utg000137l_pilon', 'utg000188l_pilon',
    'utg000191l_pilon', 'utg000305l_pilon', 'utg000319l_pilon',
    'utg000400l_pilon', 'utg000453l_pilon', 'utg000501l_pilon',
    'utg000540l_pilon', 'utg000563l_pilon', 'utg000704l_pilon',
    'utg000816l_pilon', 'utg000913l_pilon', 'utg000993l_pilon',
    'utg001004l_pilon', 'utg001048l_pilon', 'utg001582l_pilon',
    'utg001588l_pilon', 'utg001786l_pilon', 'utg001985l_pilon',
    'utg002071l_pilon', 'utg002101l_pilon', 'utg002773l_pilon',
    'utg003126l_pilon', 'utg003659l_pilon', 'utg004674l_pilon',
    'utg005845l_pilon'
]
list13 = [
    'utg000014l_pilon', 'utg000040l_pilon', 'utg000142l_pilon',
    'utg000143l_pilon', 'utg000150l_pilon', 'utg000166l_pilon',
    'utg000258l_pilon', 'utg000273l_pilon', 'utg000300l_pilon',
    'utg000533l_pilon', 'utg000573l_pilon', 'utg000610l_pilon',
    'utg000629l_pilon', 'utg000724l_pilon', 'utg000778l_pilon',
    'utg000781l_pilon', 'utg000808l_pilon', 'utg000927l_pilon',
    'utg000958l_pilon', 'utg001006l_pilon', 'utg001054l_pilon',
    'utg001584l_pilon', 'utg001618l_pilon', 'utg001634l_pilon',
    'utg001717l_pilon', 'utg001750l_pilon', 'utg001758l_pilon',
    'utg002479l_pilon', 'utg002577l_pilon', 'utg002674l_pilon',
    'utg002830l_pilon', 'utg002852l_pilon', 'utg003006l_pilon',
    'utg003160l_pilon', 'utg004832l_pilon'
]
list14 = [
    'utg000016l_pilon', 'utg000074l_pilon', 'utg000122l_pilon',
    'utg000123l_pilon', 'utg000164l_pilon', 'utg000226l_pilon',
    'utg000374l_pilon', 'utg000438l_pilon', 'utg000656l_pilon',
    'utg000663l_pilon', 'utg000717l_pilon', 'utg000741l_pilon',
    'utg000834l_pilon', 'utg000853l_pilon', 'utg001035l_pilon',
    'utg001049l_pilon', 'utg001235l_pilon', 'utg001238l_pilon',
    'utg001341l_pilon', 'utg001415l_pilon', 'utg001497l_pilon',
    'utg001532l_pilon', 'utg001652l_pilon', 'utg001673l_pilon',
    'utg001855l_pilon', 'utg001951l_pilon', 'utg002074l_pilon',
    'utg002224l_pilon', 'utg002343l_pilon', 'utg002463l_pilon',
    'utg002532l_pilon', 'utg003175l_pilon', 'utg003487l_pilon',
    'utg003998l_pilon', 'utg004168l_pilon'
]
list15 = [
    'utg000022l_pilon', 'utg000093l_pilon', 'utg000675l_pilon',
    'utg000898l_pilon', 'utg001141l_pilon', 'utg001208l_pilon',
    'utg001309l_pilon', 'utg001703l_pilon', 'utg002013l_pilon',
    'utg002095l_pilon', 'utg002436l_pilon', 'utg002566l_pilon',
    'utg002725l_pilon', 'utg002950l_pilon', 'utg003030l_pilon',
    'utg003123l_pilon', 'utg003682l_pilon'
]
list16 = [
    'utg000023l_pilon', 'utg000031l_pilon', 'utg000051l_pilon',
    'utg000054l_pilon', 'utg000060l_pilon', 'utg000077l_pilon',
    'utg000158l_pilon', 'utg000186l_pilon', 'utg000231l_pilon',
    'utg000232l_pilon', 'utg000233l_pilon', 'utg000252l_pilon',
    'utg000280l_pilon', 'utg000304l_pilon', 'utg000310l_pilon',
    'utg000417l_pilon', 'utg000429l_pilon', 'utg000511l_pilon',
    'utg000516l_pilon', 'utg000638l_pilon', 'utg000868l_pilon',
    'utg000893l_pilon', 'utg000907l_pilon', 'utg001034l_pilon',
    'utg001070l_pilon', 'utg001360l_pilon', 'utg001382l_pilon',
    'utg001443l_pilon', 'utg001515l_pilon', 'utg001547l_pilon',
    'utg001598l_pilon', 'utg001649l_pilon', 'utg002255l_pilon',
    'utg002585l_pilon', 'utg002632l_pilon', 'utg002776l_pilon',
    'utg002846l_pilon', 'utg002943l_pilon', 'utg003535l_pilon',
    'utg003856l_pilon', 'utg004042l_pilon', 'utg004354l_pilon',
    'utg004698l_pilon', 'utg004734l_pilon', 'utg004958l_pilon',
    'utg006028l_pilon'
]
list17 = [
    'utg000026l_pilon', 'utg000259l_pilon', 'utg000411l_pilon',
    'utg000416l_pilon', 'utg000455l_pilon', 'utg000530l_pilon',
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
    'utg003734l_pilon'
]
list19 = [
    'utg000028l_pilon', 'utg000058l_pilon', 'utg000092l_pilon',
    'utg000100l_pilon', 'utg000102l_pilon', 'utg000151l_pilon',
    'utg000171l_pilon', 'utg000181l_pilon', 'utg000209l_pilon',
    'utg000211l_pilon', 'utg000236l_pilon', 'utg000325l_pilon',
    'utg000384l_pilon', 'utg000443l_pilon', 'utg000463l_pilon',
    'utg000481l_pilon', 'utg000584l_pilon', 'utg000607l_pilon',
    'utg000632l_pilon', 'utg000636l_pilon', 'utg000738l_pilon',
    'utg000912l_pilon', 'utg000966l_pilon', 'utg000994l_pilon',
    'utg001016l_pilon', 'utg001041l_pilon', 'utg001056l_pilon',
    'utg001124l_pilon', 'utg001139l_pilon', 'utg001313l_pilon',
    'utg001353l_pilon', 'utg001680l_pilon', 'utg001882l_pilon',
    'utg001888l_pilon', 'utg001894l_pilon', 'utg002336l_pilon',
    'utg002363l_pilon', 'utg002383l_pilon', 'utg002418l_pilon',
    'utg002696l_pilon', 'utg002716l_pilon', 'utg003034l_pilon',
    'utg003230l_pilon', 'utg003724l_pilon', 'utg004302l_pilon',
    'utg004795l_pilon', 'utg006046l_pilon', 'utg006397l_pilon'
]
list20 = [
    'utg000032l_pilon', 'utg000039l_pilon', 'utg000042l_pilon',
    'utg000046l_pilon', 'utg000079l_pilon', 'utg000114l_pilon',
    'utg000169l_pilon', 'utg000176l_pilon', 'utg000201l_pilon',
    'utg000340l_pilon', 'utg000382l_pilon', 'utg000403l_pilon',
    'utg000407l_pilon', 'utg000604l_pilon', 'utg000720l_pilon',
    'utg000735l_pilon', 'utg000766l_pilon', 'utg000851l_pilon',
    'utg000890l_pilon', 'utg001105l_pilon', 'utg001377l_pilon',
    'utg001472l_pilon', 'utg002063l_pilon', 'utg002441l_pilon',
    'utg003985l_pilon', 'utg004789l_pilon', 'utg004941l_pilon'
]
list21 = [
    'utg000035l_pilon', 'utg000095l_pilon', 'utg000140l_pilon',
    'utg000230l_pilon', 'utg000413l_pilon', 'utg000586l_pilon',
    'utg000681l_pilon', 'utg000693l_pilon', 'utg000710l_pilon',
    'utg000718l_pilon', 'utg000744l_pilon', 'utg000955l_pilon',
    'utg001003l_pilon', 'utg001036l_pilon', 'utg001663l_pilon',
    'utg001664l_pilon', 'utg001711l_pilon', 'utg001842l_pilon',
    'utg002060l_pilon', 'utg002170l_pilon', 'utg002256l_pilon',
    'utg002688l_pilon', 'utg002750l_pilon', 'utg003009l_pilon',
    'utg003067l_pilon', 'utg003244l_pilon', 'utg003334l_pilon',
    'utg003519l_pilon', 'utg003588l_pilon', 'utg003661l_pilon',
    'utg003764l_pilon', 'utg003937l_pilon', 'utg004617l_pilon',
    'utg004646l_pilon', 'utg005233l_pilon', 'utg005296l_pilon'
]
list22 = [
    'utg000045l_pilon', 'utg000090l_pilon', 'utg000128l_pilon',
    'utg000254l_pilon', 'utg000335l_pilon', 'utg000729l_pilon',
    'utg000910l_pilon', 'utg001078l_pilon', 'utg001172l_pilon',
    'utg001644l_pilon', 'utg001739l_pilon', 'utg001869l_pilon',
    'utg001962l_pilon', 'utg002648l_pilon', 'utg004244l_pilon',
    'utg005492l_pilon'
]
list23 = [
    'utg000047l_pilon', 'utg000408l_pilon', 'utg000440l_pilon',
    'utg000556l_pilon', 'utg000596l_pilon', 'utg000622l_pilon',
    'utg000964l_pilon', 'utg001702l_pilon', 'utg001880l_pilon',
    'utg001890l_pilon', 'utg001983l_pilon', 'utg002386l_pilon',
    'utg002437l_pilon', 'utg004024l_pilon', 'utg004463l_pilon',
    'utg004546l_pilon'
]
list24 = [
    'utg000050l_pilon', 'utg000550l_pilon', 'utg000605l_pilon',
    'utg000726l_pilon', 'utg001342l_pilon', 'utg001505l_pilon',
    'utg001845l_pilon', 'utg002008l_pilon', 'utg002043l_pilon',
    'utg002780l_pilon', 'utg003152l_pilon', 'utg003284l_pilon',
    'utg003671l_pilon', 'utg004072l_pilon', 'utg005075l_pilon'
]
list25 = [
    'utg000053l_pilon', 'utg000163l_pilon', 'utg000206l_pilon',
    'utg000402l_pilon', 'utg000466l_pilon', 'utg000471l_pilon',
    'utg000507l_pilon', 'utg000821l_pilon', 'utg000965l_pilon',
    'utg001012l_pilon', 'utg001573l_pilon', 'utg001791l_pilon',
    'utg001800l_pilon', 'utg001935l_pilon', 'utg002882l_pilon'
]
list26 = [
    'utg000055l_pilon', 'utg000148l_pilon', 'utg000167l_pilon',
    'utg000245l_pilon', 'utg000281l_pilon', 'utg000313l_pilon',
    'utg000343l_pilon', 'utg000345l_pilon', 'utg000378l_pilon',
    'utg000393l_pilon', 'utg000419l_pilon', 'utg000437l_pilon',
    'utg000491l_pilon', 'utg000508l_pilon', 'utg000554l_pilon',
    'utg000560l_pilon', 'utg000676l_pilon', 'utg000695l_pilon',
    'utg000705l_pilon', 'utg000713l_pilon', 'utg001008l_pilon',
    'utg001047l_pilon', 'utg001220l_pilon', 'utg001283l_pilon',
    'utg001308l_pilon', 'utg001343l_pilon', 'utg001514l_pilon',
    'utg001666l_pilon', 'utg001700l_pilon', 'utg001795l_pilon',
    'utg001902l_pilon', 'utg001915l_pilon', 'utg002459l_pilon',
    'utg002835l_pilon', 'utg002863l_pilon', 'utg003052l_pilon',
    'utg003860l_pilon'
]
list27 = [
    'utg000097l_pilon', 'utg000170l_pilon', 'utg000222l_pilon',
    'utg000242l_pilon', 'utg000306l_pilon', 'utg000383l_pilon',
    'utg000401l_pilon', 'utg000418l_pilon', 'utg000587l_pilon',
    'utg000652l_pilon', 'utg000815l_pilon', 'utg000926l_pilon',
    'utg001108l_pilon', 'utg001115l_pilon', 'utg001137l_pilon',
    'utg001233l_pilon', 'utg001272l_pilon', 'utg001696l_pilon',
    'utg001892l_pilon', 'utg002118l_pilon', 'utg002284l_pilon',
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
    'utg002713l_pilon', 'utg002841l_pilon', 'utg004161l_pilon',
    'utg004461l_pilon'
]
list29 = [
    'utg000106l_pilon', 'utg000391l_pilon', 'utg000493l_pilon',
    'utg000623l_pilon', 'utg000855l_pilon', 'utg000865l_pilon',
    'utg000943l_pilon', 'utg001005l_pilon', 'utg001010l_pilon',
    'utg001217l_pilon', 'utg001218l_pilon', 'utg001234l_pilon',
    'utg001298l_pilon', 'utg001435l_pilon', 'utg001814l_pilon',
    'utg001875l_pilon', 'utg001916l_pilon', 'utg002273l_pilon',
    'utg002346l_pilon', 'utg002408l_pilon', 'utg002728l_pilon',
    'utg002923l_pilon', 'utg003514l_pilon', 'utg005428l_pilon'
]
list30 = [
    'utg000108l_pilon', 'utg000240l_pilon', 'utg001307l_pilon',
    'utg001333l_pilon', 'utg001422l_pilon', 'utg002527l_pilon',
    'utg002959l_pilon'
]
list31 = [
    'utg000115l_pilon', 'utg000117l_pilon', 'utg000138l_pilon',
    'utg000165l_pilon', 'utg000179l_pilon', 'utg000203l_pilon',
    'utg000342l_pilon', 'utg000395l_pilon', 'utg000423l_pilon',
    'utg000498l_pilon', 'utg000597l_pilon', 'utg000716l_pilon',
    'utg000737l_pilon', 'utg000894l_pilon', 'utg001014l_pilon',
    'utg001432l_pilon', 'utg001465l_pilon', 'utg001742l_pilon',
    'utg001988l_pilon', 'utg002266l_pilon', 'utg002483l_pilon',
    'utg002601l_pilon', 'utg002962l_pilon', 'utg003424l_pilon',
    'utg003626l_pilon', 'utg004146l_pilon', 'utg004320l_pilon'
]
list32 = [
    'utg000124l_pilon', 'utg000633l_pilon', 'utg000885l_pilon',
    'utg000908l_pilon', 'utg001057l_pilon', 'utg001151l_pilon',
    'utg001169l_pilon', 'utg001191l_pilon', 'utg001373l_pilon',
    'utg001493l_pilon', 'utg001628l_pilon', 'utg001661l_pilon',
    'utg001670l_pilon', 'utg001836l_pilon', 'utg002711l_pilon'
]
list33 = [
    'utg000126l_pilon', 'utg000180l_pilon', 'utg000327l_pilon',
    'utg000405l_pilon', 'utg000746l_pilon', 'utg000863l_pilon',
    'utg001058l_pilon', 'utg001096l_pilon', 'utg001281l_pilon',
    'utg001437l_pilon', 'utg001459l_pilon', 'utg001461l_pilon',
    'utg002016l_pilon', 'utg002454l_pilon', 'utg002805l_pilon',
    'utg004215l_pilon', 'utg004218l_pilon', 'utg004424l_pilon',
    'utg006403l_pilon'
]
list34 = [
    'utg000127l_pilon', 'utg000505l_pilon', 'utg000591l_pilon',
    'utg000694l_pilon', 'utg000794l_pilon', 'utg000831l_pilon',
    'utg000841l_pilon', 'utg000870l_pilon', 'utg001499l_pilon',
    'utg001982l_pilon', 'utg002014l_pilon', 'utg002159l_pilon',
    'utg002245l_pilon', 'utg002287l_pilon', 'utg002413l_pilon'
]
list35 = [
    'utg000136l_pilon', 'utg000278l_pilon', 'utg000813l_pilon',
    'utg000822l_pilon', 'utg000973l_pilon', 'utg001396l_pilon',
    'utg001491l_pilon', 'utg001595l_pilon', 'utg002165l_pilon',
    'utg002199l_pilon', 'utg002687l_pilon', 'utg002691l_pilon'
]
list36 = [
    'utg000139l_pilon', 'utg000160l_pilon', 'utg000247l_pilon',
    'utg000322l_pilon', 'utg000368l_pilon', 'utg000594l_pilon',
    'utg000901l_pilon', 'utg000925l_pilon', 'utg001323l_pilon',
    'utg001615l_pilon', 'utg001807l_pilon', 'utg001919l_pilon',
    'utg002330l_pilon', 'utg002347l_pilon', 'utg002587l_pilon',
    'utg002721l_pilon', 'utg003571l_pilon', 'utg007303l_pilon'
]
list37 = [
    'utg000146l_pilon', 'utg000153l_pilon', 'utg000195l_pilon',
    'utg000248l_pilon', 'utg000301l_pilon', 'utg000334l_pilon',
    'utg000496l_pilon', 'utg000524l_pilon', 'utg000529l_pilon',
    'utg000559l_pilon', 'utg000628l_pilon', 'utg000639l_pilon',
    'utg000658l_pilon', 'utg000765l_pilon', 'utg000886l_pilon',
    'utg000891l_pilon', 'utg001069l_pilon', 'utg001128l_pilon',
    'utg001132l_pilon', 'utg001265l_pilon', 'utg001428l_pilon',
    'utg001457l_pilon', 'utg002427l_pilon', 'utg002534l_pilon',
    'utg002575l_pilon', 'utg003035l_pilon', 'utg003234l_pilon',
    'utg003683l_pilon', 'utg004178l_pilon', 'utg004877l_pilon'
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
    'utg002430l_pilon', 'utg002666l_pilon', 'utg006881l_pilon'
]
list40 = [
    'utg000223l_pilon', 'utg000282l_pilon', 'utg000349l_pilon',
    'utg000640l_pilon', 'utg000996l_pilon', 'utg001068l_pilon',
    'utg001494l_pilon', 'utg001540l_pilon', 'utg001685l_pilon',
    'utg001780l_pilon', 'utg002407l_pilon', 'utg002702l_pilon',
    'utg003955l_pilon', 'utg004716l_pilon', 'utg005920l_pilon',
    'utg006711l_pilon'
]
list41 = [
    'utg000274l_pilon', 'utg000316l_pilon', 'utg000377l_pilon',
    'utg000399l_pilon', 'utg000525l_pilon', 'utg000526l_pilon',
    'utg000572l_pilon', 'utg000575l_pilon', 'utg000585l_pilon',
    'utg000625l_pilon', 'utg000645l_pilon', 'utg000660l_pilon',
    'utg000909l_pilon', 'utg000944l_pilon', 'utg001118l_pilon',
    'utg001314l_pilon', 'utg001626l_pilon', 'utg002000l_pilon',
    'utg002320l_pilon', 'utg002798l_pilon', 'utg005892l_pilon'
]
list42 = [
    'utg000287l_pilon', 'utg000428l_pilon', 'utg000624l_pilon',
    'utg000677l_pilon', 'utg001027l_pilon', 'utg001469l_pilon'
]
list43 = [
    'utg000298l_pilon', 'utg000398l_pilon', 'utg000517l_pilon',
    'utg000739l_pilon', 'utg000752l_pilon', 'utg000774l_pilon',
    'utg000872l_pilon', 'utg000883l_pilon', 'utg001037l_pilon',
    'utg001044l_pilon', 'utg001109l_pilon', 'utg001177l_pilon',
    'utg001223l_pilon', 'utg001331l_pilon', 'utg001449l_pilon',
    'utg001526l_pilon', 'utg001681l_pilon', 'utg001743l_pilon',
    'utg001806l_pilon', 'utg001993l_pilon', 'utg002004l_pilon',
    'utg002011l_pilon', 'utg002020l_pilon', 'utg002130l_pilon',
    'utg002514l_pilon', 'utg002668l_pilon', 'utg002785l_pilon',
    'utg003331l_pilon', 'utg003467l_pilon', 'utg003782l_pilon'
]
list44 = [
    'utg000311l_pilon', 'utg000546l_pilon', 'utg000768l_pilon',
    'utg000776l_pilon', 'utg000844l_pilon', 'utg000931l_pilon',
    'utg001042l_pilon', 'utg001072l_pilon', 'utg001148l_pilon',
    'utg001188l_pilon', 'utg001240l_pilon', 'utg001253l_pilon',
    'utg003516l_pilon'
]
list45 = [
    'utg000396l_pilon', 'utg000485l_pilon', 'utg000518l_pilon',
    'utg000579l_pilon', 'utg000840l_pilon', 'utg001256l_pilon',
    'utg001541l_pilon', 'utg001713l_pilon', 'utg001820l_pilon',
    'utg002186l_pilon', 'utg004975l_pilon'
]
list46 = [
    'utg000538l_pilon', 'utg000564l_pilon', 'utg000796l_pilon',
    'utg001409l_pilon', 'utg001558l_pilon', 'utg001656l_pilon',
    'utg002148l_pilon', 'utg002221l_pilon', 'utg002789l_pilon',
    'utg003262l_pilon', 'utg003288l_pilon', 'utg003561l_pilon'
]
list47 = [
    'utg001028l_pilon', 'utg002305l_pilon', 'utg002806l_pilon',
    'utg002834l_pilon'
]
list48 = [
    'utg000071l_pilon', 'utg000109l_pilon', 'utg000130l_pilon',
    'utg000189l_pilon', 'utg000207l_pilon', 'utg000210l_pilon',
    'utg000256l_pilon', 'utg000480l_pilon', 'utg000486l_pilon',
    'utg000688l_pilon', 'utg000702l_pilon', 'utg000733l_pilon',
    'utg000748l_pilon', 'utg000846l_pilon', 'utg000921l_pilon',
    'utg000995l_pilon', 'utg001063l_pilon', 'utg001089l_pilon',
    'utg001159l_pilon', 'utg001289l_pilon', 'utg001318l_pilon',
    'utg001356l_pilon', 'utg001390l_pilon', 'utg001439l_pilon',
    'utg001539l_pilon', 'utg001563l_pilon', 'utg001607l_pilon',
    'utg001676l_pilon', 'utg001724l_pilon', 'utg001774l_pilon',
    'utg001866l_pilon', 'utg001899l_pilon', 'utg001969l_pilon',
    'utg002012l_pilon', 'utg002105l_pilon', 'utg002151l_pilon',
    'utg002280l_pilon', 'utg002357l_pilon'
]


# ————————————————————————————————————————————————————————————————————————————————————————
# 将需要聚类的utg存储{utg000005l_pilon_1_10000:[10000,hap]}
def getWillUtg(mainFile):
    willUtgDict = {}
    with open(mainFile, 'r', encoding='utf_8') as f:
        for line in f:
            splits = line.strip().split()
            if splits[0] not in willUtgDict:
                willUtgDict[splits[0]] = [splits[1], splits[2]]
        return willUtgDict


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


def filterUtgRelation(willUtg_file,unikmerResult_file,alreadyCluster1071_file,hic_result_file):
    listId_list = [
        'list1', 'list2', 'list3', 'list4', 'list5', 'list6', 'list7', 'list8', 'list9', 'list10',
        'list11', 'list12', 'list13', 'list14', 'list15', 'list16', 'list17', 'list18', 'list19',
        'list20', 'list21', 'list22', 'list23', 'list24', 'list25', 'list26', 'list27', 'list28',
        'list29', 'list30', 'list31', 'list32', 'list33', 'list34', 'list35', 'list36', 'list37',
        'list38', 'list39', 'list40', 'list41', 'list42', 'list43', 'list44', 'list45', 'list46',
        'list47', 'list48'
    ]

    willUtgDict = getWillUtg(willUtg_file)  # 需要聚类的{utg:[size,type]}
    mySplit = '`?`'
    utgRelationDict = {}
    # utgUnikmerDict = {}
    with open(unikmerResult_file, 'r') as fr1:
        lines = fr1.readlines()
        for line in lines:
            splitArr = line.split(' ')
            lstTmp = [splitArr[0], splitArr[1]]
            utgRelationDict[mySplit.join(lstTmp)] = splitArr[2]
            # 将result.integrate.log存入utgRelationDict

    
    selectClusterSize_1071 = {}
    with open(alreadyCluster1071_file,'r') as fr3:
            lines = fr3.readlines()
            for line in lines:
                splits = line.strip().split()
                selectClusterSize_1071[splits[0]] = splits[1]
                # fr3存储所有聚类好的utg {1071InteUtg:size}

    willUtgRelationDict = {}
    willutgList = defaultdict(set)  # <————————————————————————————————look look
    

    with open(unikmerResult_file, 'r') as fr,\
        open(hic_result_file, 'w') as fw:
        for line in fr:
            splits = line.strip().split()
            willutgList[splits[0]].add(splits[1])
            willutgList[splits[1]].add(splits[0])
            willUtgRelationDict[mySplit.join(splits[:2])] = splits[2]
        for willUtgId in willUtgDict.keys():

            utgList = willutgList['@' + willUtgId]
            relation = 0
            sizeSum = 0
            
            i = 0
            for listid in listId_list:  # list1 ——> list48
            # for listid in listId:
                for suppId in utgList:
                    lstTmp = ['@' + willUtgId, suppId]
                    lstTmp.sort()

                    if suppId[1:][:16] in listId[i]:
                    # if suppId[1:] in listid:
                        if mySplit.join(lstTmp) in willUtgRelationDict.keys():
                            relation += int(
                                willUtgRelationDict[mySplit.join(lstTmp)])
                            # suppId是有@的
                            if suppId[1:][:16] in selectClusterSize_1071:
                                sizeSum += int(selectClusterSize_1071[suppId[1:][:16]])
                
                listid_tmp = re.findall(r"\d+\.?\d*", listid)

                if sizeSum != 0:
                    fw.write(
                        willUtgId + '  in  list' + str(listid_tmp)[2:-2] + ' 的uni_kmer数目:  ' +
                        str(round(float((100000000 * relation) /
                                        sizeSum), 4)) + '\n')
                else:
                    fw.write(willUtgId + '  in  list' + str(listid_tmp)[2:-2] + ' 的uni_kmer数目:  ' +
                             '0' + '\n')
                i+=1


# 按照每个UtgId对48个组的关系从大到小排序 —————— 很慢
def newSorted(hic_result_file,hic_sorted_file):
    lineData = []
    with open(hic_result_file, 'r') as f2, open(hic_sorted_file, 'w') as f3:
        lines2 = f2.readlines()
        # 对每48行排序
        for i in range(0, len(lines2), 48):
            for line in lines2:
                # splits = line.strip().split()
                # lineData.append(line)
                lineData=lines2[i:i + 48]
            lineData.sort(key=lambda line: round(float(line.strip().split()[-1]), 4), reverse=True)
            for line in lineData:
                f3.write(line)
            lineData = []


# 归一化 
def normalized(single_List_file, single_tmpList_file, single_lastList_file):
    group_size = 48

    with open(single_List_file, 'r', encoding='utf-8') as f, \
            open(single_tmpList_file, 'w', encoding='utf-8') as fw:
        lines = f.readlines()

        data_list = []
        weight_list = []
        normalized_weight = []

        for i, line in enumerate(lines):
            data, weight = line.strip().split()[:-1], float(
                line.strip().split()[-1])
            data_list.append([x for x in data])
            weight_list.append(weight)

            # print(data_list)
            # print(weight_list)

            if (i + 1) % group_size == 0:
                if weight_list[0] != 0:
                    normalized_weight = [round(float(weight) / float(weight_list[0]),16) for weight in weight_list]
                else:
                    normalized_weight = [float(weight) for weight in weight_list]

                for j, weight in enumerate(normalized_weight):
                    row = []
                    row.append(data_list[j])

                    row.append(weight)
                    row_str = ' '.join([str(x) for x in row]) + '\n'
                    fw.write(row_str)

                data_list = []
                weight_list = []

    with open(single_tmpList_file, 'r', encoding='utf-8') as f, \
            open(single_lastList_file, 'w', encoding='utf-8') as fw:
        lines = f.readlines()
        for line in lines:
            # 去除不需要的字符
            line = line.replace("[","").replace("]","").replace(",","").replace("'", "")
            fw.write(line)


# 这个函数很慢很慢很慢很慢... ...
def data_normal_48_new(hic_sorted_file, hic_normal_file):
    with open(hic_sorted_file, 'r') as fr, \
            open(hic_normal_file, 'w') as fw:
        lines = fr.readlines()
        for i in range(0, len(lines), 48):
            for line in lines:
                splits = line.strip().split()
                lineData = lines[i:i + 48]
            line_max = lineData[0]
            line_maxNum = round(float(line_max.strip().split(':')[1]))

            for line in lineData:
                splits = line.strip().split(':')
                aa=float(splits[1])
                if line_maxNum != 0:
                    fw.write(splits[0] + ':' + str(round(float(aa / line_maxNum),10)) + '\n')
                else:
                    fw.write(splits[0] + ':' + str(0) + '\n')


if __name__ == '__main__':
    unikmerResult_file='result.50k.log'
    willUtg_file='310.utgType.will.split50k.txt'
    alreadyCluster1071_file='310.selectClusterSize_1071.txt'
    hic_result_file='hic_result.new.txt'
    hic_sorted_file='hic_sorted.new.txt'
    hic_normal_tmp_file,hic_normal_last_file='hic_normal.tmp.txt','hic_normal.txt'
    # hic_normal_file = 'hic_normal.txt'

    result_filePath1, result_filePath2 = 'result.tmp0.txt' , 'result.tmp1.txt'
    # 1
    filterUtgRelation(willUtg_file,unikmerResult_file,alreadyCluster1071_file,hic_result_file)
    newSorted(hic_result_file,hic_sorted_file)
    # 2
    # sort -k1,1 -k5,5nr hic_result.new.txt > hic_sorted.new.txt # 快但是可能有点问题
    # 3
    normalized(hic_sorted_file, hic_normal_tmp_file, hic_normal_last_file) 
    # data_normal_48_new(hic_sorted_file, hic_normal_file) # 巨慢
    # 4 这没有用到
    # selectGroup(filePath, filePath1, filePath2)
    # readTmp0Sorted(filePath1, filePath2)
        

