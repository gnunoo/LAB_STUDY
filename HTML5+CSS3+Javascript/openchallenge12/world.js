function message(){
    if(!window.localStorage) {
        alert("지원하지 않습니다.");
        return;
    }
}
function store() {
    message();
    var engWord = document.getElementById("eng").value;
    engWord = engWord.trim();
    var korWord = document.getElementById("kor").value;
    korWord = korWord.trim();

    // 단어가 이미 있는지 확인
    if(localStorage.getItem(engWord) != null) {
        var ret = confirm(engWord + "가 이미 있습니다. 수정하시겠습니까?");
        if(ret == false) // 수정을 원치 않으면 그냥 리턴
            return;
    }

    // 로컬 스토리지에 저장(혹은 수정)
    var ret = localStorage.setItem(engWord, korWord);

    // 저장 후 <input>에 입력된 단어 지우기
    document.getElementById("eng").value = "";
    document.getElementById("kor").value = "";
}

function search() {
    message();
    var engWord = document.getElementById("eng").value;
    if(engWord == "")
        return; // 입력된 것이 없음

    engWord = engWord.trim(); // 앞 뒤 빈칸 삭제
    var korWord = localStorage.getItem(engWord);
    if(korWord == null) {
        alert(engWord + "는 없는 단어입니다.");
        document.getElementById("kor").value = "";
        return;
    }
    //입력창에 단어 추가
    var korObj = document.getElementById("kor");
    korObj.value = korWord;
}

function remove() {
    message();
    var engWord = document.getElementById("eng").value;
    if(engWord == "")
        return; // 입력된 것이 없음

    // 단어가 있는지 확인
    engWord = engWord.trim(); // 앞 뒤 빈칸 삭제
    if(localStorage.getItem(engWord) == null) {
        alert(engWord + "가 없습니다.");
        return;
    }

    // 단어 삭제
    var korWord = localStorage.removeItem(engWord);

    // 사용자 입력 칸 지우기
    document.getElementById("eng").value = "";
    document.getElementById("kor").value = engWord + " 삭제됨";
}

function viewAll() {
    var win = window.open("worldlist.html");
}