




$(document).ready(function() {

    $(".timescaleOption").click(function() {
        var selectedTimescaleFlag = $(this).attr("id");
        
        var nipPk = $(".nipPK").attr("id");
        
        selectTimescaleOption(nipPk, selectedTimescaleFlag);

    });


    function selectTimescaleOption(nipPK, timescaleString) {
        $.ajax({
            url: "/analytics/get_historical_data/" + nipPK + "/" + timescaleString,
            success: function(data) {
                
                function sortByDateAscending(a, b) {
                    return b.datetime - a.datetime;
                }

                // data_sorted = data["data"].sort(sortByDateAscending);

                $("#historicGraph").remove();
                drawGraph(data["data"], "temperature");

            }
        });
    }
    
    function drawGraph(data, metric) {
        
        // set the dimensions and margins of the graph
        var margin = {top: 20, right: 20, bottom: 30, left: 50};
        var width = $("#historicGraphContainer").width() - margin.top - margin.bottom;
        var height = $("#historicGraphContainer").height() - margin.left - margin.right;

        for (var i = 0; i < data.length; i++) {
            console.log(data[i].datetime);
        }

        // parse the date / time
        var parseTime = d3.timeParse("%Y-%m-%d %H:%M:%S");


        // set the ranges
        var x = d3.scaleTime().range([0, width]);
        var y = d3.scaleLinear().range([height, 0]);


        // define the line
        var valueline = d3.line()
            .x(function(d) { return x(d.datetime); })
            .y(function(d) { return y(d[metric]); });

            
        // add svg to div
        var svg = d3.select("#historicGraphContainer").append("svg")
            .attr("id", "historicGraph")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
                .append("g")
                    .attr("transform",
                        "translate(" + margin.left + "," + margin.top + ")");


        // convert data to correct types
        data.forEach(function(d) {
            d.datetime = parseTime(d.datetime);
            d[metric] = +d[metric];
        });


        // Scale the range of the data
        x.domain(d3.extent(data, function(d) { return d.datetime; }));
        y.domain([-100, 50]);


        // Add the valueline path.
        svg.append("path")
            .data([data])
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

    }

});