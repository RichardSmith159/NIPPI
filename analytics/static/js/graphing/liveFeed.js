var LIVE_DATA = [];

function generateDataPoint() {
    
    var now = new Date();

    var randomNumber = Math.random() * ((-80) - (-70)) + (-70);
    
    return {"datetime": now, "metric": randomNumber}

}

function getNewData() {
    // get cache data via ajax
}


function drawGraph() {

    
    // set the dimensions and margins of the graph
    var margin = {top: 20, right: 20, bottom: 30, left: 50};
    var width = $("#liveGraphContainer").width() - margin.top - margin.bottom;
    var height = $("#liveGraphContainer").height() - margin.left - margin.right;


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
    var svg = d3.select("#liveGraphContainer").append("svg")
        .attr("id", "liveFeedGraph")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");

    
    // convert data to correct types
    // (will need to convert datetime when using cache data)
    LIVE_DATA.forEach(function(d) {
        d.datetime = d.datetime;
        d.metric = +d.metric;
    });


    // Scale the range of the data
    x.domain(d3.extent(LIVE_DATA, function(d) { return d.datetime; }));
    y.domain([-100, 50]);
    

    // Add the valueline path.
    svg.append("path")
        .data([LIVE_DATA])
        .attr("class", "line")
        .attr("id", "historicTemperatureLine")
        .attr("d", valueline);


    // Add the X Axis
    svg.append("g")
        .attr("transform", "translate(0," + height/2 + ")")
        .attr("class", "historicGraphAxis")
        .attr("id", "historicGraph_xAxis")
        .call(d3.axisBottom(x));


    // Add the Y Axis
    svg.append("g")
        .attr("class", "historicGraphAxis")
        .attr("id", "historicGraph_yAxis")
        .call(d3.axisLeft(y));

}


function updateGraph() {
    
    if (LIVE_DATA.length == 15) {
        LIVE_DATA.pop()
    }

    LIVE_DATA.unshift(generateDataPoint());

    $("#liveFeedGraph").remove();

    drawGraph();

}


$(document).ready(function() {

    setInterval(updateGraph, 1000);

});