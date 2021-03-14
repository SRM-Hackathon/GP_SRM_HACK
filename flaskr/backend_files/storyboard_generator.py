# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer as Summarizer
# from sumy.nlp.stemmers import Stemmer
# from sumy.utils import get_stop_words

# #importing and loading spacy model
# import spacy
# nlp = spacy.load("en_core_web_lg")

# #package for google image download
# from google_images_download import google_images_download


# #function for downloading images from google
# def downloadimages(query): 
#     response = google_images_download.googleimagesdownload() 
#     # keywords is the search query 
#     # format is the image file format 
#     # limit is the number of images to be downloaded 
#     # print urs is to print the image file url 
#     # size is the image size which can 
#     # be specified manually ("large, medium, icon") 
#     # aspect ratio denotes the height width ratio 
#     # of images to download. ("tall, square, wide, panoramic") 
#     arguments = {"keywords": query, 
#                  "format": "png", 
#                  "limit":1, 
#                  "print_urls":True, 
#                  "size": "medium"} 
#     try: 
#         response.download(arguments) 
      
#     # Handling File NotFound Error     
#     except FileNotFoundError:  
#         arguments = {"keywords": query, 
#                      "format": "jpg", 
#                      "limit":1, 
#                      "print_urls":True,  
#                      "size": "medium"} 
                       
#         # Providing arguments for the searched query 
#         try: 
#             # Downloading the photos based 
#             # on the given arguments 
#             response.download(arguments)  
#         except: 
#             pass



# # for extracting top 3 sentences from a scene
# def return_top_3_sentences(long_desc):
    
#     LANGUAGE = "english"

#     SENTENCES_COUNT = 10

#     considered_pos_list = ["NOUN", "ADV", "ADJ", "VERB"]

#     parser = PlaintextParser.from_string(long_desc, Tokenizer(LANGUAGE))

#     stemmer = Stemmer(LANGUAGE)

#     summarizer = Summarizer(stemmer)

#     summarizer.stop_words = get_stop_words(LANGUAGE)
#     sentences = [str(sentence) for sentence in summarizer(parser.document, SENTENCES_COUNT)]

#     sentences.sort(key = len)


#     for sent in sentences:
#         print(sent)
#         tokens_ = nlp(sent)
#         tags = [token.pos_ for token in tokens_]
#         intersect_tags = set(tags).intersection(considered_pos_list)
#         if len(intersect_tags) == len(considered_pos_list):
#             form_sent = [token.text for token in tokens_ if token.pos_ in considered_pos_list]
#             clean = re.sub(r"[,.;@#?!&$]+\ *", " ", " ".join(form_sent))
#             print(clean)
#             downloadimages(clean)


# #     return sentences


# # {'count_var': 0,
# #  'frame': 'Frame1',
# #  'background': 'HAWKINS - SKY ...',
# #  'all_background': 'HAWKINS - SKY - NIGHT 1',
# #  'characters': 'None ...',
# #  'all_characters': 'None',
# #  'short_desc': 'FADE UP on the night ...',
# #  'camera_shot': 'Long Shot',
# #  'camera_movement': 'Pan Left',
# #  'long_desc': 'FADE UP on the night sky.  Dark clouds swallow the stars. WE TILT DOWN to find an IMPOSING BUILDING, sitting alone in a dense woods.  Superimpose titles: HAWKINS NATIONAL LABORATORY U.S. DEPARTMENT OF ENERGY'}
# def main_story_board_generator(content_dict_list):
#     for dict_l in content_dict_list:
#         background = dict_l["all_background"]
#         characters = dict_l["all_characters"]
#         desc_ = dict_l["long_desc"]
        
#         lines_considered_for_frame = return_top_3_sentences(desc_)
#         break

    








