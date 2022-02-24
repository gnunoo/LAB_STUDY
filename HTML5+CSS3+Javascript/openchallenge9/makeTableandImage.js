var num=Math.floor((Math.random()*100));
function init(){
// table의 행과 열을 만듬(10*10)
    var table = document.getElementById("table");

    for(var i = 0; i < 10; i++){
        var row = document.createElement("tr");

        for(var j = 0; j < 10; j++){
                var col = document.createElement("td");
                col.innerHTML = "<img src=''>";
                row.appendChild(col);
            }
        table.appendChild(row);
    }
    //랜덤하게 이미지 불러옴
    document.images[num].src="789.jpg";
    // 이미지에 대한 이벤트 추가
    for(var i=0; i<100; i++){
        document.images[i].onclick=clickRandImage;
    }
}
function clickRandImage(){
	document.images[num].src=" ";
    num=Math.floor((Math.random()*100));
    document.images[num].src="789.jpg";
}