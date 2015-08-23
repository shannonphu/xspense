var c1 = document.getElementById("c1");
var parent = document.getElementById("p1");
c1.width = parent.offsetWidth - 40;
c1.height = parent.offsetHeight - 40;

var data1 = {
  labels : ["M","T","W","T","F","S","S"],
  datasets : [
    {
      fillColor : "rgba(255,255,255,.1)",
      strokeColor : "rgba(255,255,255,1)",
      pointColor : "#123",
      pointStrokeColor : "rgba(255,255,255,1)",
      data : [50,20,95,40,32,70,150]
    }
  ]
}

var options1 = {
  scaleFontColor : "rgba(255,255,255,1)",
  scaleLineColor : "rgba(255,255,255,1)",
  scaleGridLineColor : "transparent",
  bezierCurve : true,
  scaleOverride : false,
  scaleSteps : 5,
  scaleStepWidth : 10,
  scaleStartValue : 0
}

new Chart(c1.getContext("2d")).Line(data1,options1)