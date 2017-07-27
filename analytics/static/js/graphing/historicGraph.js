

$(document).ready(function() {

    // DATA FROM DATABASE
    var historicData;

    // set the dimensions and margins of the graph
    var margin = {top: 20, right: 20, bottom: 30, left: 50},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;


    // parse the date / time
    var parseTime = d3.timeParse("%d-%b-%y");


    // set the ranges
    var x = d3.scaleTime().range([0, width]);
    var y = d3.scaleLinear().range([height, 0]);


    // define the line
    var valueline = d3.line()
        .x(function(d) { return x(d.datetime); })
        .y(function(d) { return y(d.metric); });


    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
            .append("g")
                .attr("transform",
                    "translate(" + margin.left + "," + margin.top + ")");


    // Scale the range of the data
    x.domain(d3.extent(historicData, function(d) { return d.datetime; }));
    y.domain([0, d3.max(historicData, function(d) { return d.metric; })]);


    // Add the valueline path.
    svg.append("path")
        .data([historicData])
        .attr("class", "line")
        .attr("d", valueline);


    // Add the X Axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));


    // Add the Y Axis
    svg.append("g")
        .call(d3.axisLeft(y));

});