$(document).ready(function() {

    $("#uploadAnimationID").click(function() {
        console.log("inside jquery")
        var btn = $(this).parent().parent();
        var loadSVG = btn.children("a").children(".load");
        var loadBar = btn.children("div").children("span");
        var checkSVG = btn.children("a").children(".check");

        btn.children("a").children("span").fadeOut(200, function() {
            btn.children("a").animate({
                width: 56
            }, 100, function() {
                loadSVG.fadeIn(300);
                btn.animate({
                    width: 320
                }, 200, function() {
                    btn.children("div").fadeIn(200, function() {
                        loadBar.animate({
                            width: "100%"
                        }, 2000, function() {
                            loadSVG.fadeOut(200, function() {
                                checkSVG.fadeIn(200, function() {
                                    setTimeout(function() {
                                        btn.children("div").fadeOut(200, function() {
                                            loadBar.width(0);
                                            checkSVG.fadeOut(200, function() {
                                                btn.children("a").animate({
                                                    width: 150
                                                });
                                                btn.animate({
                                                    width: 150
                                                }, 300, function() {
                                                    btn.children("a").children("span").fadeIn(200);

                                                });

                                            });
                                        });
                                    }, 2000);
                                    console.log("at the end");
                                    // window.location.href = "./timeline_page_final/timeline/dist/index.html";
                                });
                            });
                        });
                    });
                });
            });
        });

    });

});


var base_url = "http://localhost:5000/";
console.log(base_url);
var calling_api_function = "send_data_to_spacy"
var timeline_page_route = "timeline"
var response_data = "";

// function timelinepagefunction(event) {
//     console.log("here")
//     var inputField = document.getElementById('file_upload_id');
//     var selectedFiles = inputField.files[0];

//     console.log("clicked", selectedFiles);
//     const data = new FormData();
//     //Please replace this with HTML File object
//     data.append("filePath", selectedFiles);

//     const xhr = new XMLHttpRequest();
//     //Please disable this when testing in local
//     // xhr.withCredentials = true; commented as said

//     xhr.addEventListener("readystatechange", function() {
//         if (this.readyState === this.DONE) {
//             // console.log(this.responseText);
//             response_data = this.responseText;
//             // console.log(typeof(response_data))
//             json_data_conv = JSON.parse(response_data)
//             json_data = {
//                 "status": json_data_conv["status"],
//                 "results": json_data_conv["results"]
//             }
//             console.log(json_data)
//             $.ajax({
//                 type: "POST",
//                 url: "/" + calling_api_function,
//                 data: json_data,
//                 dataType: "json",
//                 success: function(response) {
//                     console.log("success")
//                         // $("route_to_timeline").click();
//                     console.log("Link Access")
//                     window.location.replace("http://localhost:5000/" + calling_api_function);

//                 }
//             });
//             console.log("here after post call");
//         }
//     });
//     xhr.open("POST", "https://apis.sentient.io/microservices/utility/docconversion/v1.0/getresults");
//     xhr.setRequestHeader("x-api-key", "8C388562FC1D45D48F07");
//     xhr.send(data);


//     document.getElementById("uploadAnimationID").click();

// }



function timelinepagefunction(event) {
    console.log("here")
    var inputField = document.getElementById('file_upload_id');
    var selectedFiles = inputField.files[0];

    console.log("clicked", selectedFiles);
    const data = new FormData();
    //Please replace this with HTML File object
    data.append("filePath", selectedFiles);

    const xhr = new XMLHttpRequest();
    //Please disable this when testing in local
    // xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function() {
        if (this.readyState === this.DONE) {
            // console.log(this.responseText);
            response_data = this.responseText;
            // console.log(typeof(response_data))
            json_data_conv = JSON.parse(response_data)
            json_data = {
                "status": json_data_conv["status"],
                "results": json_data_conv["results"]
            }
            console.log(json_data)
            $.ajax({
                type: "POST",
                url: "/" + calling_api_function,
                data: json_data,
                dataType: "json",
                success: function(response) {
                    console.log("success");
                    click_form_submit_button()
                }
            });
            console.log("here after post call");
        }
    });
    //https://apis.sentient.io/microservices/utility/docconversion/v1.0/getresults
    xhr.open('POST','https://apis.sentient.io/microservices/utility/docconversion/v1.0/getresults');
    xhr.setRequestHeader("x-api-key", "9930F160E8AC45D29293");
    xhr.send(data);
    document.getElementById("uploadAnimationID").click();
}

function click_form_submit_button() {
    console.log("inside click button function")
    document.getElementById("route_to_timeline").click()
}