var items = document.querySelectorAll(".timeline li");
var calling_api_function = "key_for_edit_time_line"

// $('body').append('<div style="" id="loadingDiv"><div class="loader"><img src="../../../svg_gif_elements/ner_loader.gif"></div></div>');
$(window).on('load', function() {
    setTimeout(removeLoader, 3000); //wait for page load PLUS two seconds.
});

var counter = 0

function removeLoader() {
    console.log("counter from timeline page for loading time setting", counter)
    if (counter == 0) {
        console.log("inside if timeline loader", counter)
        $("#loading").fadeOut(2000, function() {
            // fadeOut complete. Remove the loading div
            $("#loadingDiv").remove(); //makes page more lightweight
            $('section, logo').show()
                // $("control_logo_id").css("display", "")
        });
    } else {
        console.log("else inside timeline loader", counter)
        $("#loading").fadeOut(2000, function() {
            // fadeOut complete. Remove the loading div
            $("#loadingDiv").remove(); //makes page more lightweight
            $('section, logo').show()

        });
    }

}



function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    // console.log("herr")
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function callbackFunc() {
    for (var i = 0; i < items.length; i++) {
        if (isElementInViewport(items[i])) {
            if (!items[i].classList.contains("in-view")) {
                items[i].classList.add("in-view");
            }
        } else if (items[i].classList.contains("in-view")) {
            items[i].classList.remove("in-view");
        }
    }
}

window.addEventListener("load", callbackFunc);
window.addEventListener("scroll", callbackFunc);


function editTimeLine(dict_rec) {
    console.log("edit time line")

    console.log(dict_rec)

    console.log("edit time line function", typeof(dict_rec));
    console.log("")
    console.log("")
    console.log("")

    console.log("/" + calling_api_function + "?key=" + dict_rec)
    console.log("")
    console.log("")
    console.log("")
    console.log("")
    console.log("")
    console.log("")
    console.log("")
    console.log("")
    console.log("")
    console.log("")
    console.log("")
    console.log("")
    setTimeout('', 10000);

    $.ajax({
        type: "GET",
        url: "/" + calling_api_function + "?key=" + parseInt(dict_rec),
        success: function(response) {
            console.log("success");
            click_form_submit_button()
        }
    });

}

// #############################################################
// these functions functions are for edit time line model page
//
// document.getElementById("submit-button").onclick = function() {
//     console.log("here")
//     location.href = base_url + "index.html";
// };

// function cancel() {
//     console.log("edit time line function")
//     window.location.href = base_url + "index.html";
// }
// #############################################################


function generate_storyboard() {
    console.log("Clicked generate storyboard");
    document.getElementById("route_to_story_board_viewer").click();
}

function click_form_submit_button() {
    console.log("inside click button function");
    document.getElementById("route_to_timeline").click();
}