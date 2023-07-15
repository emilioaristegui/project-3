//console.log("whatever")

// Create the trace

// Aquí estoy seguro de que algo está mal, porque se genera un bucle infinito y no carga el plot
// hbaría que revisar si el url está bien o algo...
d3.json('http://127.0.0.1:5000/data').then(d=>{
    let trace1={
        x:d.region,
        y:d.emissions,
        type:'bar'
    }
    let data = [trace1]
    
    Plotly.newPlot('plot', data)
    let trace2={
        x:d.country,
        y:d.emissions,
        type:'bar'
    }
    let data2 = [trace2]

    Plotly.newPlot('plot2', data2)
})

d3.json('http://127.0.0.1:5000/data').then(d=>{

    var data5 = [{
        values: d.year,
        labels: 'Year',
        type: 'pie'
      }];
      
      var layout = {
        height: 400,
        width: 500
      };
      
      Plotly.newPlot('myDiv', data5, layout);
})