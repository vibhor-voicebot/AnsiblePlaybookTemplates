$(".icon").click(function () {
    $(".main").css('visibility', 'visible');
    setTimeout(function () {
        $(".top").css("visibility", "visible")
    }, 1500);

    setTimeout(function () {
        $(".card").css("visibility", "visible")
        $(".droid").css("visibility", "visible")
    }, 3000);

    setTimeout(function () {
        $("#card-content").css("visibility", "visible")
    }, 4500);

    setTimeout(function () {
        $(".card1").css("visibility", "visible")
    }, 6000);

    setTimeout(function () {
        $(".card2").css("visibility", "visible")
    }, 7500);

    setTimeout(function () {
        $(".card3").css("visibility", "visible")
    }, 9000);

    setTimeout(function () {
        $(".card4").css("visibility", "visible")
    }, 10500);

    setTimeout(function () {
        $(".card5").css("visibility", "visible")
    }, 12000)
})

