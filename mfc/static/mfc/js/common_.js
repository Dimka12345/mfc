$(document).ready(function() {

	//Таймер обратного отсчета
	//Документация: http://keith-wood.name/countdown.html
	//<div class="countdown" date-time="2015-01-07"></div>
	var austDay = new Date($(".countdown").attr("date-time"));
	$(".countdown").countdown({until: austDay, format: 'yowdHMS'});


	//Навигация по Landing Page
	//$(".top_mnu") - это верхняя панель со ссылками.
	//Ссылки вида <a href="#contacts">Контакты</a>
	$(".top_mnu").navigation();

    //Добавляет классы дочерним блокам .block для анимации
	//Документация: http://imakewebthings.com/jquery-waypoints/
	$(".block").waypoint(function (direction) {
		if (direction === "down") {
			$(".class").addClass("active");
		} else if (direction === "up") {
			$(".class").removeClass("deactive");
		}
		;
	}, {offset: 100});

    //Плавный скролл до блока .div по клику на .scroll
	//Документация: https://github.com/flesler/jquery.scrollTo
	$("a.scroll").click(function () {
		$.scrollTo($(".div"), 800, {
			offset: -90
		});
	});

    //Каруселька
	//Документация: http://owlgraphic.com/owlcarousel/
	var owl = $(".carousel");
	owl.owlCarousel({
		items: 2,
        autoHeight: true,
	});
	//owl.on("mousewheel", ".owl-wrapper", function (e) {
	//	if (e.deltaY > 0) {
	//		owl.trigger("owl.prev");
	//	} else {
	//		owl.trigger("owl.next");
	//	}
	//	e.preventDefault();
	//});
	$(".next_button").click(function () {
		owl.trigger("owl.next");
	});
	$(".prev_button").click(function () {
		owl.trigger("owl.prev");
	});

	//Кнопка "Наверх"
	window.onload = function() { // после загрузки страницы

	var scrollUp = document.getElementById('scrollup'); // найти элемент

	scrollUp.onmouseover = function() { // добавить прозрачность
		scrollUp.style.opacity=0.8;
		scrollUp.style.filter  = 'alpha(opacity=80)';
	};

	scrollUp.onmouseout = function() { //убрать прозрачность
		scrollUp.style.opacity = 0.4;
		scrollUp.style.filter  = 'alpha(opacity=40)';
	};

	scrollUp.onclick = function() { //обработка клика
		window.scrollTo(0,0);
	};

// show button

	window.onscroll = function () { // при скролле показывать и прятать блок
		if ( window.pageYOffset > 0 ) {
			scrollUp.style.display = 'block';
		} else {
			scrollUp.style.display = 'none';
		}
	};
};

})
