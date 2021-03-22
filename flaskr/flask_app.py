import os
import json
import random
from flask_session import Session
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, send_from_directory
import pickle

from flask_cors import CORS


# from flaskr.backend_files.scene_extraction import main_scene_extraction
from backend_files.scene_extraction import main_scene_extraction

app = Flask(__name__, static_url_path='/static')
sess = Session()
CORS(app)

app.secret_key = 'imaya"s secret'
app.config['SESSION_TYPE'] = 'filesystem'


sess.init_app(app)

app.config["CLIENT_PDF"] = "/app/flaskr/generated_storyboard_pdfs"
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


global base_urls
global content_dict_for_timeline_page
# global content_dict_list_for_timeline


event = {}
event_key = 0

base_url = "http://0.0.0.0:5000/"
content_dict_for_timeline_page = []

camera_shot_list =["Long Shot", "Extreme Long Shot", "Mid Long Shot", "Mid Shot/Bust Shot", "Mid Closeup", "Extreme Closeup", "High Angle", "Low Angle", "Over The Shoulder", "Point Of View", "Dutch Angle"]
camera_movement_list = ["Pan Left", "Pan Right", "Tilt Up", "Tilt Down", "Zoom In", "Zoom Out", "Dolly In", "Dolly Out", "Custom"]
############################################################################################################
#place holder for all read/write function
############################################################################################################
def read_time_line_content(scene):

    content_dict_list = []
    for i, split_values in enumerate(scene):
        content_dict = {}
        content_dict["count_var"] = i
        content_dict["frame"] = "Frame - "+str(split_values[0]+1)
        content_dict["background"] = " ".join(split_values[1].split()[:3])+" ..."
        content_dict["all_background"] = split_values[1]
        content_dict["characters"] = " ,".join(split_values[2].split(" ,")[:3])+" ..." 
        content_dict["all_characters"] = split_values[2]
        content_dict["short_desc"] = " ".join(split_values[3].split()[:5])+" ..."
        content_dict["camera_shot"] = "Long Shot"
        # content_dict["camera_movement"] = random.choice(camera_movement_list)
        content_dict["camera_movement"] = "Pan Left"
        content_dict["long_desc"] = split_values[3]
        content_dict_list.append(content_dict)
    return content_dict_list

############################################################################################################
#placeholder for ui render page
############################################################################################################

@app.route("/")
def login():
    return render_template("login_page/index.html")

@app.route('/upload_page')
def upload_page():
    print("here -------------")
    print(os.getcwd())
    print("\n\n")
    return render_template("grease_pencil_upload_page_ui.html")

@app.route("/timeline")
def timeline():
    val = request.form.get("success")
    pickle.dump(session["content_dict_list"], open("content_dict_list.pkl","wb"))
    if val == "success":
        return render_template('timeline_page/index.html', content_dict_list= session["content_dict_list"], scene_updation_message=True)
    else:
        return render_template("timeline_page/index.html", content_dict_list= session["content_dict_list"])

@app.route("/key_for_edit_time_line")
def key_for_edit_time_line():
    print(request.args)
    key = request.args.get("key" , default=0, type=int)
    print(key)
    session["edit_time_line_key"] = key
    return  {"status": "Success"}

@app.route("/timelineEdit")
def timelineEdit():
    print("after updating the session came to timelineEdit render template route")
    return render_template("timeline_editor_page/index.html", display_frame_values=  session["content_dict_list"][session["edit_time_line_key"]])

@app.route("/updateFrameInfo", methods= ['GET', 'POST'])
def updateFrameInfo(methods= ['GET', 'POST']):
    print(session["edit_time_line_key"])
    if request.method == 'POST':
        print(request.form)
        if request.form.get("all_background"):
            session["content_dict_list"][session["edit_time_line_key"]]["all_background"] = request.form.get("all_background")
        else:
            None

        if request.form.get("all_characters"):
            session["content_dict_list"][session["edit_time_line_key"]]["all_characters"] = request.form.get("all_characters")
        else:
            None

        if request.form.get("camera_shot"):
            session["content_dict_list"][session["edit_time_line_key"]]["camera_shot"] = request.form.get("camera_shot")
        else:
            None

        if request.form.get("camera_movement"):
            session["content_dict_list"][session["edit_time_line_key"]]["camera_movement"] = request.form.get("camera_movement")
        else:
            None

        if request.form.get("long_desc"):
            session["content_dict_list"][session["edit_time_line_key"]]["long_desc"] = request.form.get("long_desc")
        else:
            None

    print(session["content_dict_list"][session["edit_time_line_key"]])
    return render_template("timeline_page/index.html", content_dict_list= session["content_dict_list"])


@app.route("/storyboardViewer")
def storyboardViewer():
    return render_template("storyboard_viewer_page/index_static.html")


@app.route("/download")
def download():
    print("inside download call")
    pdf_name = "Grease_Pencil_Generated.pdf"
    print("\n\n\n",pdf_name,"\n\n\n")
    return send_from_directory(app.config["CLIENT_PDF"], filename="Grease_Pencil_Generated.pdf", as_attachment=True)
############################################################################################################
# placeholder for backend files
############################################################################################################
# Write backend api functions here


# @app.route("/send_data_to_spacy", methods=['POST'])
# def send_data_to_spacy(methods = ['GET', 'POST']):
#     # val = json.loads(request.form.getlist("data"))
#     print("here", type(request.form))
#     print("\n\n")
#     print(request.form)
#     print("\n\n")
#     request_data_bck = request.form
#     request_data_bck_dict = {}
#     print(len(request_data_bck))
#     print("Request---",request_data_bck_dict.keys(), "\n\n")

#     if request_data_bck["results"]:
#         scene_info = main_scene_extraction(request_data_bck["results"])
#         if scene_info["status_code"] == 200:
#             content_dict_for_timeline_page = read_time_line_content(scene_info["scene_info_dict"])

#     print("here")
#     return redirect("timeline_page/index.html", content_dict_list = content_dict_for_timeline_page)


########################## akshay bro flask approach ###########################################
# @app.route("/send_data_to_spacy", methods=['GET','POST'])
# def send_data_to_spacy(methods = ['GET', 'POST']):
#     global content
#     if request.method=="GET":
#         return render_template("timeline_page/index.html", content_dict_list = content)
#     # val = json.loads(request.form.getlist("data"))
#     # print("here", type(request.form))
#     print("\n\n")
#     # print(request.form)
#     print("\n\n")
#     request_data_bck = request.form

#     if request_data_bck["results"]:
#         scene_info = main_scene_extraction(request_data_bck["results"])
#         if scene_info["status_code"] == 200:
#             content_dict_for_timeline_page = read_time_line_content(scene_info["scene_info_dict"])
#     print("here")
#     print(content_dict_for_timeline_page)
    
#     # return jsonify(content_dict_for_timeline_page)
#     # return redirect(url_for("timeline_page", content_dict_list=jsonify(content_dict_for_timeline_page)))
#     template =  render_template("timeline_page/index.html", content_dict_list = content_dict_for_timeline_page)
#     if request.method=="POST":
#         content = content_dict_for_timeline_page
#         return {"status": "Success", "template": template}

########################## my flask approach ###########################################
@app.route("/send_data_to_spacy", methods=['POST'])
def send_data_to_spacy(methods = ['GET', 'POST']):

    print(os.getcwd())
    global content_dict_for_timeline_page
    # val = json.loads(request.form.getlist("data"))
    # print("here", type(request.form))
    if request.method == "POST":
        request_data_bck = request.form

        if request_data_bck["results"]:
            scene_info = main_scene_extraction(request_data_bck["results"])
            if scene_info["status_code"] == 200:
                content_dict_for_timeline_page = read_time_line_content(scene_info["scene_info_dict"])
        # return jsonify(content_dict_for_timeline_page)
        # return redirect(url_for("timeline_page", content_dict_list=jsonify(content_dict_for_timeline_page)))
        session["content_dict_list"] = content_dict_for_timeline_page
        

        return  {"status": "Success"}
    else:
        print("inside else")
        return render_template("timeline_page/index.html", content_dict_list = content_dict_for_timeline_page)




# if __name__ == '__main__':

#     app.secret_key = 'imaya"s secret'
#     app.config['SESSION_TYPE'] = 'filesystem'

#     sess.init_app(app)

#     app.run(host= '127.0.0.1', debug= True)
