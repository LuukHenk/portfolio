window.addEventListener("DOMContentLoaded", function(){

	var menu = document.getElementById("menu");
	var menu_objs = document.getElementById("menu_objs");
	var menu_display_style = "grid"

	menu.addEventListener("click", function(ev) {
		var current_display = menu_objs.style.display;
		if (menu_objs.style.display === menu_display_style) {
			menu_objs.style.display = "none";
		} else {
			menu_objs.style.display = menu_display_style;
		};
	});
	window.addEventListener("resize", function(){
		if (screen.width >= 600) {
			menu_objs.style.display = "none";
		}
	})
})
