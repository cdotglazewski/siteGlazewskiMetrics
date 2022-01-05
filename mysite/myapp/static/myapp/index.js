

$(function() {
    //Get all total values, sort and remove duplicates
    let totalList = $(".effMargin")
      .map(function() {return $(this).text()})
      .get()
      .sort(function(a,b){return a - b })
      .reduce(function(a, b) {if (b != a[0]) a.unshift(b);return a}, [])
  
    //Assign rank
    totalList.forEach((v, i) => {
      $('.effMargin').filter(function() {return $(this).text() == v;}).next().text(i + 1);
    })
  });

// function sortTable(table_id, sortColumn){
//     var tableData = document.getElementById(table_id).getElementsByTagName('tbody').item(0);
//     var rowData = tableData.getElementsByTagName('tr');            
//     for(var i = 0; i < rowData.length - 1; i++){
//         for(var j = 0; j < rowData.length - (i + 1); j++){
//             if(Number(rowData.item(j).getElementsByTagName('td').item(sortColumn).innerHTML.replace(/[^0-9\.]+/g, "")) < Number(rowData.item(j+1).getElementsByTagName('td').item(sortColumn).innerHTML.replace(/[^0-9\.]+/g, ""))){
//                 tableData.insertBefore(rowData.item(j+1),rowData.item(j));
//             }
//         }
//     }
// }

