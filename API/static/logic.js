//console.log("whatever")

// Create the trace

// First plot
d3.json('http://127.0.0.1:5000/data_emissions').then(d=>{
d3.select("#selectregion")
.selectAll("option")
.data(d.index)
.enter()
.append("option") 
.attr("value", d=>d)
.text(d=>d)  
let trace1={
        x:d.index,
        y:d.data,
        type:'bar'
    }
    let data = [trace1]

    var layout = {
        title: "CO2 Emissions by Region", 
        yaxis: {title: "CO2 Emissions", showgrid: false},
        font: {
            color: "white", 
            family: "'Courier New', Courier, monospace",
            size: 12
        },
        paper_bgcolor:"rgba(0,0,0,0)",
        plot_bgcolor:"rgba(234,247,161,0.8)",
        marker: {
            color: 'rgba(0,0,0,1)',
        }
    };

    Plotly.newPlot('plot1', data, layout)
    d3.selectAll("#selectregion").on("change", updatePlotly);
    function updatePlotly() {
        // Use D3 to select the dropdown menu
        let dropdownMenu = d3.select("#selectregion");
        // Assign the value of the dropdown menu option to a variable
        let dataset = dropdownMenu.property("value");
        if (dataset == "global"){
            Plotly.restyle("plot1", "x", [d.index]);
            Plotly.restyle("plot1", "y", [d.data]); 
        }else{let index = d.index.indexOf(dataset)
            let x = [d.index[index]];
            let y = [d.data[index]];
            
            // Note the extra brackets around 'x' and 'y'
            Plotly.restyle("plot1", "x", [x]);
            Plotly.restyle("plot1", "y", [y]);}
        } 
})

d3.json('http://127.0.0.1:5000/country_emissions').then(d=>{
d3.select("#selectcountry")
.selectAll("option")
.data(d.index)
.enter()
.append("option") 
.attr("value", d=>d)
.text(d=>d)  
let trace1={
        x:d.index,
        y:d.data,
        type:'bar'
    }
    let data = [trace1]
    
    var layout = {
        title: "CO2 Emissions by Country", 
        yaxis: {title: "CO2 Emissions", showgrid: false},
        font: {
            color: "white", 
            family: "'Courier New', Courier, monospace",
            size: 12
        },
        paper_bgcolor:"rgba(0,0,0,0)",
        plot_bgcolor:"rgba(234,247,161,0.8)",
    };

    Plotly.newPlot('plot2', data, layout)

    d3.selectAll("#selectcountry").on("change", updatePlotly);
    function updatePlotly() {
        // Use D3 to select the dropdown menu
        let dropdownMenu = d3.select("#selectcountry");
        // Assign the value of the dropdown menu option to a variable
        let dataset = dropdownMenu.property("value");
        if (dataset == "global"){
            Plotly.restyle("plot2", "x", [d.index]);
            Plotly.restyle("plot2", "y", [d.data]); 
        }else{let index = d.index.indexOf(dataset)
            let x = [d.index[index]];
            let y = [d.data[index]];
            
            // Note the extra brackets around 'x' and 'y'
            Plotly.restyle("plot2", "x", [x]);
            Plotly.restyle("plot2", "y", [y]);}
        } 
})

d3.json('http://127.0.0.1:5000/industry_emissions').then(d=>{
d3.select("#selectindustry")
.selectAll("option")
.data(d.index)
.enter()
.append("option") 
.attr("value", d=>d)
.text(d=>d)  
let trace1={
        x:d.index,
        y:d.data,
        type:'bar'
    }
    let data = [trace1]

    var layout = {
        title: "CO2 Emissions by Industry", 
        yaxis: {title: "CO2 Emissions", showgrid: false},
        font: {
            color: "white", 
            family: "'Courier New', Courier, monospace",
            size: 12
        },
        paper_bgcolor:"rgba(0,0,0,0)",
        plot_bgcolor:"rgba(234,247,161,0.8)",
    };

    Plotly.newPlot('plot3', data, layout)
    d3.selectAll("#selectindustry").on("change", updatePlotly);
    function updatePlotly() {
        // Use D3 to select the dropdown menu
        let dropdownMenu = d3.select("#selectindustry");
        // Assign the value of the dropdown menu option to a variable
        let dataset = dropdownMenu.property("value");
        if (dataset == "global"){
            Plotly.restyle("plot3", "x", [d.index]);
            Plotly.restyle("plot3", "y", [d.data]); 
        }else{let index = d.index.indexOf(dataset)
            let x = [d.index[index]];
            let y = [d.data[index]];
            
            // Note the extra brackets around 'x' and 'y'
            Plotly.restyle("plot3", "x", [x]);
            Plotly.restyle("plot3", "y", [y]);}
        } 
})
