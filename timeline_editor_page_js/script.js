var items = document.querySelectorAll(".timeline li");



var base_url = "file:///Users/disprz/Projects/IMAYA/GP_FILES/timeline_page_final/timeline/dist/"

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



// $("#timeLineEditorModal").modal("hide");


function move_to_time_line_page() {
    console.log("inside click button function")
    document.getElementById("route_to_timeline").click()
}
//     $("#timeLineEditorModal").modal("show")
// }
// $(document).ready(function() {
//     console.log("inside document")
//     $("#timeLineEditorModal").modal("show");
//     $("#timeLineEditorModal").modal("hide");
// });
// fucntion()
// $("#timeLineEditorModal").click(function() {
//     console.log("here")
//     var a = 4;
//     if (a == 5) {
//         alert("if");
//         $('#timeLineEditorModal').modal('show');
//     } else {
//         alert("else");
//         $('#timeLineEditorModal').modal('hide');
//     }
// });