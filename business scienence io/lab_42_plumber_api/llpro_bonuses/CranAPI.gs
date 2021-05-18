/*

CRAN API CONNECTION INSTRUCTIONS:
- Change your AWS EC2 Server URL in the awsURL() function below
- Pay attention to the cells used in your sheet

*/

// Get URL
function awsURL() {
  return("http://ec2-18-218-97-62.us-east-2.compute.amazonaws.com")
}

// Tests
function testInput() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();

  var start = sheet.getRange(5,2).getValue();
  var end = sheet.getRange(6,2).getValue();

  Logger.log(Utilities.formatDate(date = start, timeZone = Session.getScriptTimeZone(), format = "YYYY-MM-dd"))
  Logger.log(Utilities.formatDate(date = end, timeZone = Session.getScriptTimeZone(), format = "YYYY-MM-dd"))
}

// Tests
function removeCharts() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();

  var n = sheet.getCharts().length;
  for (var i = n-1; i >= 0; i--) {
    var chart = sheet.getCharts()[i];
    sheet.removeChart(chart);
  }
}

// function to call CRAN API
function callCranAPI(package, start, end, by) {

  // Convert inputs to text
  var start_text = Utilities.formatDate(date = start, timeZone = Session.getScriptTimeZone(), format = "YYYY-MM-dd")
  var end_text = Utilities.formatDate(date = end, timeZone = Session.getScriptTimeZone(), format = "YYYY-MM-dd")

  var response = UrlFetchApp.fetch(awsURL() + ":8000/cran?package=" + package + "&start=" + start_text + "&end=" + end_text + "&by=" + by);

  // Parse the JSON reply
  var json = response.getContentText();
  var data = JSON.parse(json);

  // Logger.log(data);

  return(data)

}

// custom menu
function onOpen() {
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('CRAN Downloads')
      .addItem('Get Package Data','displayCranData')
      .addToUi();
}

function displayCranData() {

  // pick up the search term from the Google Sheet
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getActiveSheet();

  removeCharts()

  var package = sheet.getRange(4,2).getValue();
  var start   = sheet.getRange(5,2).getValue();
  var end     = sheet.getRange(6,2).getValue();
  var by      = sheet.getRange(7,2).getValue();

  var cran_data = callCranAPI(package, start, end, by);
  // var cran_data = callCranAPI(package, start, end, by);


  var results = cran_data["data"];

  var output = []

  results.forEach(function(elem,i) {
    output.push([elem["package"],elem["date"],elem["count"]]);
  });

  var len = output.length;

  // clear any previous content
  sheet.getRange(15,1,len,3).clearContent();

  // paste in the values
  sheet.getRange(15,1,len,3).setValues(output);

  createEmbeddedLineChart(15,2,len,3, package)

}

/**
 * Creates and inserts an embedded
 * line chart into the active sheet.
 */
function createEmbeddedLineChart(r1, c1, r2, c2, package) {
  var sheet = SpreadsheetApp.getActiveSheet();
  var chartDataRange = sheet.getRange(r1,c1,r2,c2);
  var hAxisOptions = {
    slantedText: true,
    slantedTextAngle: 60,
    gridlines: {
      count: 12
    }
  };

  var lineChartBuilder = sheet.newChart().asLineChart();
  var chart = lineChartBuilder
    .addRange(chartDataRange)
    .setPosition(5, 5, 0, 0)
    .setTitle('CRAN Package Downloads: ' + package)
    .setNumHeaders(1)
    .setLegendPosition(Charts.Position.RIGHT)
    .setOption('hAxis', hAxisOptions)
    .build();

  sheet.insertChart(chart);
}
