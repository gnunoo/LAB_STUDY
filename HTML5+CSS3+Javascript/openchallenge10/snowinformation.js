var body = document.getElementById("body");
var count = 0;
function addSnow(){
    var snow=document.createElement("span");
    snow.setAttribute("class","snow");
    //눈을 왼쪽에서 랜덤으로 출력하고
    snow.style.left=`${Math.random() * (window.innerWidth - 1) + 1}px`;
    // 애니메에션 상영 시간
    snow.style.animationDuration=`${Math.random() * (20 - 8) + 8}s`;
    //애니메이션 딜레이
    snow.style.animationDelay=`${Math.random() * (10 - 1) + 1}s`;
    //불투명도
    snow.style.opacity=`${Math.random()}`;
    body.appendChild(snow)
    //300번 반복
    if (count < 300) {
        window.requestAnimationFrame(addSnow);
        count++;
    }
};

addSnow();
