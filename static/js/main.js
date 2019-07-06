var timer = 8000,
    objtimer = false;


// 自动翻页
// setInterval(function () {
//     if (objtimer === false) {
//         objtimer = true;
//         objtimer = setInterval(function () {
//             $.fn.fullpage.moveSlideRight();
//             objtimer = false;
//         }, timer);
//     }
// }, 1000);

// objtimer = setInterval(function () {
//     $.fn.fullpage.moveSlideRight();
// }, timer);

var flag = true;
// 鼠标移入移出点击事件
function mouseEvent(e) {
    e.addClass("liactive").siblings(
    ).removeClass("liactive");
}

$(".bottom .nav li").mouseover(function () {
    $(this).addClass("over")
}).mouseleave(function () {
    $(this).removeClass("over")
}).on("click", function () {
    clearInterval(objtimer);
    var objId = "#" + $(this).children("a").attr("data-attr");
    // 获取ID 添加类名
    $(objId).addClass("active");
    var $index = $(objId).index();
    flag = false;
    $.fn.fullpage.moveTo(1, $index);
    mouseEvent($(".navbar .nav li:eq(" + $index + ")"));

});

// 鼠标滑轮事件 js处理
if (window.addEventListener)//FF,火狐浏览器会识别该方法
    window.addEventListener('DOMMouseScroll', wheel, false);
window.onmousewheel = document.onmousewheel = wheel;//W3C
//统一处理滚轮滚动事件
function wheel(event){
    var delta = 0;
    if (!event) event = window.event;
    if (event.wheelDelta) {//IE、chrome浏览器使用的是wheelDelta，并且值为“正负120”
        delta = event.wheelDelta/120;
        if (window.opera) delta = -delta;//因为IE、chrome等向下滚动是负值，FF是正值，为了处理一致性，在此取反处理
    } else if (event.detail) {//FF浏览器使用的是detail,其值为“正负3”
        delta = -event.detail/3;
    }
    if (delta)
        handle(delta);
}
//上下滚动时的具体处理函数
function handle(delta) {
    clearInterval(objtimer);
    var $active = $(".nav .liactive"),
        $index = $active.index();
    if (delta <0){
        //向下滚动
        $index ++;
        $index = $index === 5 ? 0: $index;
        if($active.next("li").html() !== undefined){
            $active.removeClass("liactive").next("li").addClass("liactive");
        }else{
            $active.removeClass("liactive");
            $("ul.nav li:first-child").addClass("liactive")
        }
        flag = false;
        $.fn.fullpage.moveTo(1, $index);

    }else{
        //向上滚动
        $index --;
        $index = $index === -1 ? 4: $index;
        if($active.prev("li").html() !== undefined){
            $active.removeClass("liactive").prev("li").addClass("liactive");
        }else{
            $active.removeClass("liactive");
            $("ul.nav li:last-child").addClass("liactive");
        }
        flag = false;
        $.fn.fullpage.moveTo(1, $index);
    }
}





