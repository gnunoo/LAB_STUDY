        var canvas=document.getElementById("myCanvas");
        var context=canvas.getContext("2d");
        //성적 정보
        var colors=["blue","green","yellow","magenta","red"];
        var grades=["A","B","C","D","F"];
        function draw(){
            //전체 인원수 구하기
            var total=0;
            for(var i=0; i<grades.length; i++){
                total+= parseInt(document.getElementById(grades[i]).value);
            }
            //학점 별 비율
            percent=new Array();
            var sum=0;
            for(var i=0; i<grades.length; i++){
                var temp=parseInt(document.getElementById(grades[i]).value)/total;
                sum=sum+temp;
                percent[i]=sum;
            }
            //비율 확인
            document.getElementById('div').innerHTML=percent;
            //그리기
            for(var i=0; i<grades.length; i++){
                context.beginPath();
                context.moveTo(280,300);
                //처음 그릴때
                if(i==0)    context.arc(280,300,150,0,percent[0]*2*Math.PI);
                //마지막 그릴떄
                else if(i==grades.length-1)  context.arc(280,300,150,percent[i-1]*2*Math.PI,2*Math.PI);
                //그외 그릴때
                else    context.arc(280,300,150,percent[i-1]*2*Math.PI,percent[i]*2*Math.PI);
                context.closePath();

                context.fillStyle=colors[i];
                context.fill();
            }
            
            
        }
        // 차트 지우기
        function erase() {
            context.clearRect(0, 0, canvas.width, canvas.height);
        }