function animateValue(id) {
    var obj = document.getElementById(id);
    var end = obj.innerHTML;
    var start = end-900;
    var timer = setInterval(function() {
        start += 1;
        obj.innerHTML = start;
        if (start == end) {
            clearInterval(timer);
        }
    }, 1);
}

animateValue("data_confirmed");
animateValue("data_recovered");
animateValue("data_deaths");
animateValue("data1_confirmed");
animateValue("data1_recovered");
animateValue("data1_deaths");