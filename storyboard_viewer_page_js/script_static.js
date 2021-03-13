// $(window).on('load', function() {
//     setTimeout(removeLoader, 3000); //wait for page load PLUS two seconds.
// });

var counter = 0

function removeLoader() {
    "here"
    console.log("counter from timeline page for loading time setting", counter)
    if (counter == 0) {
        console.log("inside if timeline loader", counter)
        $("#loading").fadeOut(2000, function() {
            // fadeOut complete. Remove the loading div
            $("#loadingDiv").remove(); //makes page more lightweight
            $('section').show()
                // $("control_logo_id").css("display", "")
        });
    } else {
        console.log("else inside timeline loader", counter)
        $("#loading").fadeOut(2000, function() {
            // fadeOut complete. Remove the loading div
            $("#loadingDiv").remove(); //makes page more lightweight
            $('section').show()

        });
    }

}



var gallery = (function() {

    'use strict';

    // vars
    var gal_item = $('.gallery_item'),
        gal_img = $('.gallery_item_preview a img'),
        gal_full = $('.gallery_item_full'),
        gal_box = $('.box'),
        gal_top = $('.gallery_top');


    return {
        // this.js(obj)
        js: function(e) { return $("[data-js=" + e + "]"); },
        // this.lk(obj)
        lk: function(e) { return $("[data-lk=" + e + "]"); },
        // Ready functions
        ready_: function() { this.events(); },
        //  functions
        events: function() {
            var self = this;
            // add close link
            gal_full.append('<a href="#" data-js="cl" class="cl">X</a>');
            // Get all data js and add clickOn function
            var k = $('a[data-js]');
            k.each(function(i, v) {
                i = i + 1;
                self.clickOn(i);
            });
            // close on click
            self.js('cl').on("click", function(e) {
                e.preventDefault();
                self.fx_out(gal_full);
                self.fx_out(gal_box);
            });

            // list style
            self.js('list').on("click", function(e) {
                e.preventDefault();
                // toggle class
                gal_item.toggleClass('gallery_item_list');
                gal_img.toggleClass('gallery_line');
                // window.location.href = "../../../"


                // change icon style
                if (gal_item.hasClass('gallery_item_list')) {
                    $(this).addClass('icon_list_open')
                        .html('<span>•••</span>' +
                            '<span>•••</span>' +
                            '<span>•••</span>');
                    gal_top.attr("class", "gallery_top gallery_hide_top");
                } else {
                    $(this).removeClass('icon_list_open')
                        .html('<span>• -</span>' +
                            '<span>• -</span>' +
                            '<span>• -</span>');
                    gal_top.attr("class", "gallery_top");
                }
            });
        },
        // Show on click
        clickOn: function(i) {
            var self = this;
            this.js(i).on('click', function(e) {
                e.preventDefault();
                self.fx_in(self.lk(i));
                self.fx_in(gal_box);
            });
        },
        // out function
        fx_out: function(el) {
            el.addClass('efOut')
                .delay(500)
                .fadeOut('fast')
                .removeClass('efIn');
            // show scroll
            $('body').css({ overflow: 'auto' });
            return false;
        },
        // in function
        fx_in: function(el) {
            el.removeClass('efOut')
                .show(200)
                .addClass('efIn');
            // hide scroll
            // $('body').css({ overflow: 'hidden' });
            return false;
        }
    };
})();
// ready function of gallery
gallery.ready_();

$(document).ready(function() {

    setTimeout(removeLoader, 4000);
    console.log("indid");
    setTimeout(removeLoader, 4000);
    setTimeout(trigger, 2000);

});

function trigger() {
    $("#for-trigger").trigger('click');
}

function downloadStoryboard() {
    console.log("inside download button function storyboard page");
    document.getElementById("route_to_story_board_viewer").click();
}