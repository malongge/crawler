$('#request').click(function() {
	var num = $('#number').val();
	$.ajax({
		type:"GET", 
		url:"http://47.52.164.88/test3.php", 
		data:{"id": num}, 
		success:function(data) { 
		    $('#num').text(data.classnum); 
		    $('#price').text(data.price);
		}, 
		error:function(e,t,v) {
			// alert('Load error：' + t); 
		} 
	}); 
})
