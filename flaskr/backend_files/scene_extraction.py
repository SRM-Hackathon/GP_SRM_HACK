import os
import re
import requests
# import spacy



master_pos_tag_list = ["VERB", "VB", "MD", "NOUN", "PROPN", "ADJ", "JJ", "AUX",  "MD", "PRP$", "PRP", "POS", "ADV", "RB", "DET", "DT", "CONJ", "CC"]
custom_stop_word_list = ["END APPENDIX", "CONTINUED", "APPENDIX", "(CONTINUED)", "CONTINUED:"]
custom_stop_word_regex = re.compile("|".join(custom_stop_word_list))
remove_brackets_regex = re.compile("\((\s|\S)+?\)")


def form_title_word_pool(scene_list):
    title = []
    for i,sc in enumerate(scene_list):
        if "cast list" in sc.lower():
            break
        else:
            if sc:
                title.append(sc)
    return (i,title)
            
def get_cast_list(i, scene_list, title_list):
    cast_list = []
    title_pool = [y for x in title_list for y in x.split()]
    for sf in scene_list[i+1:]:
        check_title_flag = [x for x in sf.split() if x in title_pool]
        if check_title_flag:
            break
        else:
            cast_list.append(sf)
            
    return cast_list


def get_scene_desc(stripped_scene_list, cast_list):
    
    scene_info_list = []
    scene_index_list = [(i, scene) for i,scene in enumerate(stripped_scene_list) if  scene.startswith("EXT") or scene.startswith("INT")]
    
    for i,scene_index in enumerate(scene_index_list):
        complete_scene_info_from_stripped_text = ""
        each_scene_start_index, each_scene_stop_index = 0,0
        if i< len(scene_index_list)-1:

            each_scene_start_index, each_scene_stop_index = scene_index_list[i][0], scene_index_list[i+1][0]
            complete_scene_info_from_stripped_text = stripped_scene_list[each_scene_start_index : each_scene_stop_index]
            complete_scene_info_from_stripped_text = [x for x in complete_scene_info_from_stripped_text if x != ""]
            characters = extract_character( cast_list, " ".join(complete_scene_info_from_stripped_text))
            scene_info_list.append((i, complete_scene_info_from_stripped_text[0].replace("EXT.", "").replace("INT.", "").replace("EXT./INT.","").strip(), characters, " ".join(complete_scene_info_from_stripped_text[1:])))

        else:
            each_scene_start_index = scene_index_list[i][0]
            complete_scene_info_from_stripped_text = stripped_scene_list[each_scene_start_index : -1]
            complete_scene_info_from_stripped_text = [x for x in complete_scene_info_from_stripped_text if x != ""]
            characters = extract_character( cast_list, " ".join(complete_scene_info_from_stripped_text))
            scene_info_list.append((i, complete_scene_info_from_stripped_text[0].replace("EXT.", "").replace("INT.", "").strip(), characters, " ".join(complete_scene_info_from_stripped_text[1:])))
            
    return scene_info_list

def frame_extraction(scene_desc):
    
    # doc = nlp(scene_desc)
    doc = ""
    parsed_tokens = [(token.pos_, token.text) for token in doc]
    frame_list = []
    check_frame = []
    index_list = []
    for index, pos_tag in enumerate(parsed_tokens):
        if (pos_tag[0] != "PUNCT" and pos_tag[1] != "." ) or pos_tag[1] == "," or pos_tag[1]== "-":
            if pos_tag[0] != "SPACE":
#                 print("here")
                check_frame.append(pos_tag[0])
                index_list.append(index)
            else:
                if index < len(parsed_tokens):
                    
                    print("here", pos_tag[index+1])
                else:
                    print(parsed_tokens[index:])
        else:
            val = [tg for tg in set(check_frame) if tg in master_pos_tag_list]
            if len(val) >=6:

                frame_list.append(index_list)
                check_frame = []
                index_list = []
            else:
                continue
#     logger.debug("Inside frame extraction function : \n Frame List Given Below: \n"+ str(frame_list) + "\n----Document for the above frame list is below : \n"+str(doc)+ "\n\n")
    return (frame_list, doc)         
                

def extract_dialogues_and_play_separetly(scene_list, cast_list):
    
    cleaned_scene_list = []
    indexes_lines_removed_from_scene = []
    
    #for cleaning the scene lines with custom stop words and remove bracketted words from title
    remove__custom_stop_words = ""
    check_title_flag = []
    dialogues,play = [],[]
    continue_for_dialogue = False
    
    for index, sc in enumerate(scene_list):
        remove__custom_stop_words = custom_stop_word_regex.sub("",sc)
        if remove__custom_stop_words:
            remove__bracket_ = remove_brackets_regex.sub("", remove__custom_stop_words)
            check_title_flag = [x for x in remove__bracket_.split() if x.strip() in cast_list and len(x.split()) == 1]
            if check_title_flag or continue_for_dialogue:
                if check_title_flag == title_formed:
                    print("Inside Title IF : ", check_title_flag)
                    title_formed = check_title_flag
                    continue_for_dialogue = True
                    dialogues.append((index, remove__bracket_))
                else:
                    continue_for_dialogue = False
                    
            else:
                print("considering this as play : ", sc)
                play.append("")
                cleaned_scene_list.append((index, remove__custom_stop_words))
        else:
            indexes_lines_removed_from_scene.append((index, "its removed because after custom stop words there is no informaion left"))
            
    return None


def extract_character(cast_list, scene):
    check_odd_one_word_title = ["THE"]
    cast_list = [x for x in cast_list if re.sub("[^a-zA-Z.-\/\']","",x) != ""]
    separated_cast_list = [y for x in cast_list for y in x.split() if bool(re.search("[a-zA-Z.-\/]+", y)) if y not in check_odd_one_word_title]
    complete_cast_list = separated_cast_list+cast_list
    cast_list_rege= re.compile(r"(?=(\b" + '\\b|\\b'.join(set(complete_cast_list)) + r"\b))")

    characters = cast_list_rege.findall(scene)
    if characters:
        return " ,".join(set(characters))
    else:
        return "None"


def main_scene_extraction(scene_desc):

    if scene_desc:
        
        scene_list_ = scene_desc.splitlines()
#         scene_list = " ".join(scene_list_).split(".")
        stripped_scene_list_ = [scene.strip().lstrip("0123456789.-").rstrip("0123456789.-").lstrip("--").rstrip("--") for scene in scene_list_]
        
        #getting cast and title info
        title_words_pool_index, title_words_pool = form_title_word_pool(stripped_scene_list_)
        cast_list = get_cast_list(title_words_pool_index, stripped_scene_list_, title_words_pool)
        
        #stripping 
        stripped_scene_list = [x for x in stripped_scene_list_ if not bool(re.search("\s{5,}\S+\d\.", x))]
#         scene_info_dict = get_scene_desc(stripped_scene_list, cast_list)
        scene_info_list = get_scene_desc(stripped_scene_list, cast_list)
        return {"msg": "scene extraction complete",
                "status_code": 200,
                "stripped_scene_list": stripped_scene_list,
                "scene_info_dict": scene_info_list,
                "return_fucntion": "scene_extraction_function"}
        

    else:
        return {"msg": "scene list is empty",
                "status_code": 500,
                "return_function": "scene_extraction_function",
                    "stripped_scene_list": [("No scenes Found", "No scenes Found", "No scenes Found", "No scenes Found")]
               }