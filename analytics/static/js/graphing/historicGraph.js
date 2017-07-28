

$(document).ready(function() {

    // DATA FROM DATABASE
    var historicData = [
        {"datetime": "01/01/2017 00:00:00", "metric": -80},
        {"datetime": "01/01/2017 00:01:00", "metric": -79},
        {"datetime": "01/01/2017 00:02:00", "metric": -80},
        {"datetime": "01/01/2017 00:03:00", "metric": -78},
        {"datetime": "01/01/2017 00:04:00", "metric": -78},
        {"datetime": "01/01/2017 00:05:00", "metric": -77},
        {"datetime": "01/01/2017 00:06:00", "metric": -79},
        {"datetime": "01/01/2017 00:07:00", "metric": -80},
        {"datetime": "01/01/2017 00:08:00", "metric": -79},
        {"datetime": "01/01/2017 00:09:00", "metric": -80},
        {"datetime": "01/01/2017 00:10:00", "metric": -79},
        {"datetime": "01/01/2017 00:11:00", "metric": -77},
        {"datetime": "01/01/2017 00:12:00", "metric": -76},
        {"datetime": "01/01/2017 00:13:00", "metric": -78},
        {"datetime": "01/01/2017 00:14:00", "metric": -80},
        {"datetime": "01/01/2017 00:15:00", "metric": -80},
        {"datetime": "01/01/2017 00:16:00", "metric": -80},
        {"datetime": "01/01/2017 00:17:00", "metric": -70},
        {"datetime": "01/01/2017 00:18:00", "metric": -78},
        {"datetime": "01/01/2017 00:19:00", "metric": -78},
        {"datetime": "01/01/2017 00:20:00", "metric": -80},
        {"datetime": "01/01/2017 00:21:00", "metric": -80},
        {"datetime": "01/01/2017 00:22:00", "metric": -79},
        {"datetime": "01/01/2017 00:23:00", "metric": -79},
        {"datetime": "01/01/2017 00:24:00", "metric": -78},
        {"datetime": "01/01/2017 00:25:00", "metric": -80},
        {"datetime": "01/01/2017 00:26:00", "metric": -80},
        {"datetime": "01/01/2017 00:27:00", "metric": -76},
        {"datetime": "01/01/2017 00:28:00", "metric": -78},
        {"datetime": "01/01/2017 00:29:00", "metric": -79},
        {"datetime": "01/01/2017 00:30:00", "metric": -80},
    ];


    // set the dimensions and margins of the graph
    var margin = {top: 20, right: 20, bottom: 30, left: 50};
    var width = $("#historicGraphContainer").width() - margin.top - margin.bottom;
    var height = $("#historicGraphContainer").height() - margin.left - margin.right;


    // parse the date / time
    var parseTime = d3.timeParse("%d/%m/%Y %H:%M:%S");


    // set the ranges
    var x = d3.scaleTime().range([0, width]);
    var y = d3.scaleLinear().range([height, 0]);


    // define the line
    var valueline = d3.line()
        .x(function(d) { return x(d.datetime); })
        .y(function(d) { return y(d.metric); });

        
    // add svg to div
    var svg = d3.select("#historicGraphContainer").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");


    // convert data to correct types
    historicData.forEach(function(d) {
        d.datetime = parseTime(d.datetime);
        d.metric = +d.metric;
    });


    // Scale the range of the data
    x.domain(d3.extent(historicData, function(d) { return d.datetime; }));
    y.domain([-100, 100]);


    // Add the valueline path.
    svg.append("path")
        .data([historicData])
        .attr("class", "line")
        .attr("id", "historicTemperatureLine")
        .attr("d", valueline);


    // Add the X Axis
    svg.append("g")
        .attr("transform", "translate(0," + y(0) + ")")
        .attr("class", "historicGraphAxis")
        .attr("id", "historicGraph_xAxis")
        .call(d3.axisBottom(x));


    // Add the Y Axis
    svg.append("g")
        .attr("class", "historicGraphAxis")
        .attr("id", "historicGraph_yAxis")
        .call(d3.axisLeft(y));

});