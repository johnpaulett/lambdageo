(function() {


    var postLocation = function(position) {
        $("#location-results").show()
            .html("<pre>" + JSON.stringify(position) + "</pre>");

        $.post("/upload/", JSON.stringify({
            "type":"Point", 
            "coordinates": [
                position.coords.longitude,
                position.coords.latitude
            ]
        }));
    }

    var locationError = function(error) {
        console.log(error);
    }

    $(document).ready(function() {
        // Geolocation API
        $("#share-location").click(function(){
            navigator.geolocation.getCurrentPosition(
                postLocation,
                locationError,
                {
                    maximumAge: 600000, 
                    enableHighAccuracy: true
                }
            );
        });
    });
    

    window.displayMap = function(buildingGeo, measurements){
        // Create the map
        var latlng = new google.maps.LatLng(38.565116, -90.402347);
        var options = {
            zoom: 16,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map-container"),
                                      options);

        // place the building overlay
        var buildingCoords = [];
        for (i in buildingGeo.coordinates[0]) {
            buildingCoords.push(
                new google.maps.LatLng(
                    buildingGeo.coordinates[0][i][1],
                    buildingGeo.coordinates[0][i][0]
                )
            );
        }
        var building = new google.maps.Polygon({
            paths: buildingCoords,
            strokeColor: "#FF0000",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#FF0000",
            fillOpacity: 0.35
        })
        building.setMap(map);

        // show all the measurements

        for (i in measurements) {
            var point = measurements[i]
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(
                    point[0].coordinates[1], 
                    point[0].coordinates[0]
                ),
                title: point[1]
            });
            marker.setMap(map);
        }
    }
})();