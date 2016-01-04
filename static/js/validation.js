function validate(){
	var n=document.forms["register"]["username"].value;
	var e=document.forms["register"]["email"].value;
	var atpos=e.indexOf("@");
	var dotpos=e.lastIndexOf(".");
	var fn=document.forms["register"]["first_name"].value;
	var ln=document.forms["register"]["last_name"].value;
	var pas1=document.forms["register"]["password1"].value;
	var pas2=document.forms["register"]["password2"].value;
	var k=0;
	var symb = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
	var digits = "0123456789";
	var is_d=false;
	var is_s=false;
	document.getElementById('username').innerHTML = '';
	document.getElementById('email').innerHTML = '';
	document.getElementById('first_name').innerHTML = '';
	document.getElementById('last_name').innerHTML = '';
	document.getElementById('password1').innerHTML = '';
	document.getElementById('password2').innerHTML = '';
	if(n==null || n=="") {
		document.getElementById('username').innerHTML = 'Це поле обов\'язкове для заповнення!';
		k=1;
	}
	else{
		if (n.length<5) {
			document.getElementById('username').innerHTML = 'Логін повинен містити більше 5 символів!';
			k=1;
		}
	}
	if(e==null || e=="") {
		document.getElementById('email').innerHTML = 'Це поле обов\'язкове для заповнення!';
		k=1;
	}
	else{
		if(atpos<1 || dotpos<atpos+2 || dotpos+2>=e.length){
			document.getElementById('email').innerHTML = 'Непрвильний E-mail!';
			k=1;
		}
	}
	if(fn==null || fn=="") {
		document.getElementById('first_name').innerHTML = 'Це поле обов\'язкове для заповнення!';
		k=1;
	}
	if(ln==null || ln=="") {
		document.getElementById('last_name').innerHTML = 'Це поле обов\'язкове для заповнення!';
		k=1;
	}
	if(pas1==null || pas1=="") {
		document.getElementById('password1').innerHTML = 'Це поле обов\'язкове для заповнення!';
		k=1;
	}
	else{
		if (pas1.length<8) {
			document.getElementById('password1').innerHTML = 'Пароль повинен містити більше 8 символів!';
			k=1;
		}
		else{
			 for (var i = 0; i < pas1.length; i++) {
				 if (!is_s && symb.indexOf(pas1[i]) != -1){
					is_s=true; 
				 }
				 if (!is_d && digits.indexOf(pas1[i]) != -1){
					 is_d=true;
				 }
			    }
			 if(is_s==false || is_d==false){
				 document.getElementById('password1').innerHTML = 'Пароль повинен містити букви і цифри!';
				 k=1;
			    } 
		}
	}
	if(pas2==null || pas2=="") {
		document.getElementById('password2').innerHTML = 'Це поле обов\'язкове для заповнення!';
		k=1;
	}
	else {
		if(pas1!=pas2){
			document.getElementById('password2').innerHTML = 'Паролі не співпадають!';
			k=1;
		}
	}
	if(k==1){
		return false;	
	}
}
function validateForm(){
	var ln=document.forms["forma"]["last_name"].value;
	var fn=document.forms["forma"]["first_name"].value;
	var date=document.forms["forma"]["date"].value;
	var time=document.forms["forma"]["time"].value;
	var ta=document.forms["forma"]["problem"].value;
	var cn = document.getElementById("id_car_name").options.selectedIndex;
	var txt = document.getElementById("id_car_name").options[cn].text;
	var k=0;
	var symb = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
	var is_s=false;
	document.getElementById('first_name').innerHTML = '';
	document.getElementById('last_name').innerHTML = '';
	document.getElementById('datetime').innerHTML = '';
	document.getElementById('car_name').innerHTML = '';
	document.getElementById('problem').innerHTML = '';
	if(ln==null || ln=="") {
		document.getElementById('last_name').innerHTML = 'Це поле обов\'язкове для заповнення!';
		k=1;
	}
	if(fn==null || fn=="") {
		document.getElementById('first_name').innerHTML = 'Це поле обов\'язкове для заповнення!';
		k=1;
	}
	if(date==null || date==""||time==null || time==""){
		document.getElementById('datetime').innerHTML = 'Ці поля обов\'язкові для заповнення!';
		k=1;
	}
	else{
		for (var i = 0; i < time.length; i++) {
				 if (!is_s && symb.indexOf(time[i]) != -1){
					is_s=true; 
				 }
	    }
		if(time[2]!=":" ||is_s==true){
			document.getElementById('datetime').innerHTML = 'Непрвильний формат часу!';
			k=1;
		}
	}
	if(txt=="---------"){
		document.getElementById('car_name').innerHTML = 'Оберіть авто!';
		k=1;
	}
	if(ta==null || ta=="") {
		document.getElementById('problem').innerHTML = 'Це поле обов\'язкове для заповнення!';
		k=1;
	}
	if(k==1){
		return false;	
	}
}
