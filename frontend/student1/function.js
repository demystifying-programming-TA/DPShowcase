
// InitializeGraph
function InitializeGraph() {

	// Make a client-side API call to obtain the user's location
	$.getJSON("http://ip-api.com/json", function (data, status) {
		// Inspect the data returned from the API
		console.log(data)

		// Extract the user's longitude and latitude from the data that the API returns
		user_longitude = data.lon;
		user_latitude  = data.lat;

		// Log the longitude and latitude to the console
		console.log("Longitude: " + user_longitude)
		console.log("Latitude: " + user_latitude)

		// Update the interface the user sees with their location
		document.getElementById("location").innerHTML = "<br>Your location (dark line):<br><br> Latitude: " + user_latitude + "<br>Longitude: " + user_longitude;

		lat2 = document.getElementById("lat1").value
		long2 = document.getElementById("long1").value

		console.log("Longitude2: " + long2)
		console.log("Latitude2: " + lat2)

		lat3 = document.getElementById("lat2").value
		long3 = document.getElementById("long2").value

	
		
		// Make API call to backend & draw graph
		$.getJSON("/student1/update_country", {longitude1: user_longitude, latitude1:user_latitude,
			longitude2:long2, latitude2:lat2,
			longitude3:long3, latitude3:lat3}, 
			function (data, status) {

				// Inspect the data returned from the API
				//console.log(typeof data)
				//console.log(data.Location)

				// Draw graph
				DrawGraph(data.Location,data.Data);
			}
		)
	})

}


// DrawGraph
function DrawGraph(location, aqdata) {

/*  // Generate and format the data
  var plot = [['a','b','c'],{aqdata}]
  console.log(plot)*/
  console.log(aqdata)
  console.log(location)

  
  var data = new google.visualization.DataTable();

  /*var data = google.visualization.arrayToDataTable([
  	aqdata[1]

    	//["A","B","C"],
    	['2020-02-10', 1, 1.0],
		 ['2020-02-11', 4, 3.0],
		 ['2020-02-12', 3, 2.67],
		 ['2020-02-13', 10, 5.67]
  ]);
*/
console.log(location)
data.addColumn('string', 'Date');
data.addColumn('number', location[0]);
data.addColumn('number', location[1]);
data.addColumn('number', location[2]);
console.log(aqdata)
console.log(data)
var row;
for (var i = 0; i < aqdata.length; i++) {
    row = aqdata[i];
    console.log(row)
    try {
    	data.addRow([row[0], row[2], row[4],row[6]]);
    }
    catch{
    	console.log("error")
    }
}


   console.log(data)


  // Customize the graph
  var options = {
    colors: ['#34495e', '#c8f7c5','#89c4f4'],
    chartArea: {width: '50%'},
    title: '10 day rolling average for air quality - PM25',
  };

  var view = new google.visualization.DataView(data);
  view.setColumns([0,1,2,3]);

  // Generate the graph
  var chart = new google.visualization.LineChart(document.getElementById('chart'));

  // Display the graph
  chart.draw(view, options);

}


function updateInputA(lat1){
    document.getElementById("lat1").value = lat1;
}

function updateInputB(long1){
    document.getElementById("long1").value = long1;
}

function updateInputC(lat2){
    document.getElementById("lat2").value = lat2;
}

function updateInputD(long2){
    document.getElementById("long2").value = long2;
}

