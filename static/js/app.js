var vocalnessSlider = $("#vocalnessSlider").slider();
var intelligenceSlider = $("#intelligenceSlider").slider();
var energySlider = $("#energySlider").slider();


// Click handler for sidebar minimization/expansion
$("#menu-toggle").click(function(e) {
    if ($("#menu-toggle").html() === "Hide Settings")
        $("#menu-toggle").html("Show Settings");
    else
        $("#menu-toggle").html("Hide Settings");

    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});


// "Find a Match" click handler
$("#findPartner").click(function(e) {

    // Update the catfact every time they click the find a (new) match
    $.ajax({
        url: "<serverURL>/catFact",
        success: function(catFact){
            $("#catFact").html("Complimentary Cat Fact: " + catFact);
        },
        dataType: "text"
    });


    // Set loading gif while a match is found
    $("#catPic").attr("src", "/static/img/avatar-cat.gif");


    // Hide the sidebar
    if (!$("#wrapper").hasClass("toggled")) {
        $("#wrapper").toggleClass("toggled");
        $("#menu-toggle").html("Show Settings");
    }

    // Get reference to sliders
    var vocalnessSlider = $("#vocalnessSlider").slider();
    var intelligenceSlider = $("#intelligenceSlider").slider();
    var energySlider = $("#energySlider").slider();

    // Get reference to slider values
    var vocalnessSliderVal = vocalnessSlider.slider('getValue');
    var intelligenceSliderVal = intelligenceSlider.slider('getValue');
    var energySliderVal = energySlider.slider('getValue');

    $("#tmp").empty();
    $("#tmp").append("<div id=\"localVideo\" muted></div>");
    $("#tmp").append("<div id=\"remoteVideo\"></div>");

    var webrtc = new SimpleWebRTC({
        localVideoEl: 'localVideo',
        remoteVideosEl: 'remoteVideo',
        autoRequestMedia: true
    });

    webrtc.on('readyToCall', function() {

        // POST slider values to recieve an appropriate room/roomName 
        $.ajax({
            type: "POST",
            url: "urlHERE...herokuServer?",
            data: {
                vocalness: vocalnessSliderVal,
                intelligence: intelligenceSliderVal,
                energy: energySliderVal
            },

            // response callback
            success: function(roomName) {
                webrtc.joinRoom(roomName); // Join the specified room name
                $("#catPic").hide(); // Hide the loading gif
                $("#findPartner").html("Find a new match"); // "Find a Match" --> "Find Next Match"
            },
            dataType: "text"
        });
    });

    webrtc.on('joinedRoom', function() {
        alert("joinedRoom - Works! - play a greeting cat sound?");
        var audio = new Audio('./audio/meow.mp3');
        audio.play();
    });

    webrtc.on('localMediaError', function() {
        alert("localMediaError - camera/mic access was probably denied");
    });

    webrtc.on('error', function() {
        alert("error - idk yet");
    });

    webrtc.on('createdPeer', function() {
        alert("createdPeer - idk yet");
    });

    webrtc.on('localScreenAdded', function() {
        alert("localScreenAdded - idk yet");
    });

});