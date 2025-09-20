from pathlib import Path
import jaconv
import bz2

def is_hiragana(text):
    hira_list = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔ"
    for i in range( len(text)):
        if text[i] not in hira_list:
            return False
        
    return True

path_list = (

    (
        Path("th-dic-r13-google/thdic-r13-1-作品名.txt"),
        Path("./build/jtalkdic-ud-thdic-sakuhin-ipadic.csv"),
        Path("./build/jtalkdic-ud-thdic-sakuhin-noacc.csv"),
    ),
    (
        Path("th-dic-r13-google/thdic-r13-2-キャラクター名.txt"),
        Path("./build/jtalkdic-ud-thdic-character-ipadic.csv"),
        Path("./build/jtalkdic-ud-thdic-character-noacc.csv"),
    ),
    (
        Path("th-dic-r13-google/thdic-r13-4-用語.txt"),
        Path("./build/jtalkdic-ud-thdic-word-ipadic.csv"),
        Path("./build/jtalkdic-ud-thdic-word-noacc.csv"),
    ),
    (
        Path("th-dic-r13-google/thdic-r13-3-曲名.txt"),
        Path("./build/jtalkdic-ud-thdic-music-ipadic.csv"),
        Path("./build/jtalkdic-ud-thdic-music-noacc.csv"),
    ),
    (
        Path("th-dic-r13-google/thdic-r13-5-スペルカード.txt"),
        Path("./build/jtalkdic-ud-thdic-spelcard-ipadic.csv"),
        Path("./build/jtalkdic-ud-thdic-spelcard-noacc.csv"),
    ),
)
for paths in path_list:
    source_file = paths[0]
    ipadic_file = paths[1]
    noacc_file = paths[2]

    data = source_file.read_text(encoding="utf-8") 
    data = data.split("\n")

    out = []
    surface_list = []
    for line in data:
        if line != "" and line[0] != "#":
            
                
            split_line = line.split("\t")
            surface = split_line[1]
            yomi_hira = split_line[0]
            yomi = jaconv.hira2kata(yomi_hira)

            if  is_hiragana(yomi_hira):
                if surface not in surface_list:
                    new_line = f"{surface},1345,1345,8000,名詞,一般,*,*,*,*,{surface},{yomi},{yomi}"
                    out.append((new_line))
                    surface_list.append(surface)

    ipadic_file.write_text("\n".join(out), encoding="utf-8")


    out = []
    surface_list = []
    for line in data:

        if line != "" and line[0] != "#":
            
            split_line = line.split("\t")
            surface = split_line[1]
            yomi_hira = split_line[0]
            yomi = jaconv.hira2kata(yomi_hira)

            if  is_hiragana(yomi_hira):
                if surface not in surface_list:
                    new_line = f"{surface},1345,1345,8000,名詞,一般,*,*,*,*,{surface},{yomi},{yomi},*/*,*"
                    out.append((new_line))
                    surface_list.append(surface)

    noacc_file.write_text("\n".join(out), encoding="utf-8")