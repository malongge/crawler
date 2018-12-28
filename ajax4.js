$('#request').click(function() {
	var b = new Base64();
	var num = $('#number').val();
	$.ajax({
		type:"GET", 
		url:"http://47.52.164.88/test4.php", 
		data:{"id": num}, 
		success:function(data) { 
		    $('#num').text(b.decode(data.classnum)); 
		    $('#price').text(b.decode(data.price));
		}, 
		error:function(e,t,v) {
			// alert('Load error：' + t); 
		} 
	}); 
})
