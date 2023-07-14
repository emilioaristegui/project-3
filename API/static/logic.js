//console.log("whatever")

// Create the trace

// Aquí estoy seguro de que algo está mal, porque se genera un bucle infinito y no carga el plot
// hbaría que revisar si el url está bien o algo...
d3.json('http://127.0.0.1:5000/data').then(d=>{
    let trace1={
        x:d.country,
        y:d.region,
        type:'bar'
    }
    
    let data = [trace1]
    
    Plotly.newPlot('plot', data)
})
