for (i=0; i<100; i++){
  var request = new XMLHttpRequest();
  request.open ('GET', 'https://github.com/devngc/repo/blob/gh-pages/data.txt', false);
  request.send();
  if (request.status == 200){
    console.log(request);
    document.writeln(request.responseText);
  }
}
