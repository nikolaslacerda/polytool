$(document).ready(function() {

	$('#poly_1').on('keyup', function() {
		if($('#poly_1').val().length !=0){
			$('#btn_root_1').attr('disabled', false)
			$('#btn_graph_1').attr('disabled', false)
			if($('#poly_2').val().length != 0){
				$('#btn_sum').attr('disabled', false)
				$('#btn_sub').attr('disabled', false)
				$('#btn_mul').attr('disabled', false)
				$('#btn_div').attr('disabled', false)     
			}
		}
        else{
			$('#btn_sum').attr('disabled',true);
			$('#btn_sub').attr('disabled',true);
			$('#btn_mul').attr('disabled',true);
			$('#btn_div').attr('disabled',true);
			$('#btn_root_1').attr('disabled', true)
			$('#btn_graph_1').attr('disabled', true)
		}
	});

	$('#poly_2').on('keyup', function() {
		if($('#poly_2').val().length !=0){
			$('#btn_root_2').attr('disabled', false)
			$('#btn_graph_2').attr('disabled', false)
			if($('#poly_1').val().length != 0){
				$('#btn_sum').attr('disabled', false)
				$('#btn_sub').attr('disabled', false)
				$('#btn_mul').attr('disabled', false)
				$('#btn_div').attr('disabled', false)     
			}
		}
        else{
			$('#btn_sum').attr('disabled',true);
			$('#btn_sub').attr('disabled',true);
			$('#btn_mul').attr('disabled',true);
			$('#btn_div').attr('disabled',true);
			$('#btn_root_2').attr('disabled', true)
			$('#btn_graph_2').attr('disabled', true)
		}
	});


	$('#btn_mul').click( function(event) {

		$.ajax({
			data : {
				name : $('#poly_1').val(),
				email : $('#poly_2').val()
			},
			type : 'POST',
			url : '/mul'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#poly_result').val(data.name);
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

	$('#btn_sum').click( function(event) {

		$.ajax({
			data : {
				name : $('#poly_1').val(),
				email : $('#poly_2').val()
			},
			type : 'POST',
			url : '/sum'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#poly_result').val(data.name);
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

	$('#btn_sub').click( function(event) {

		$.ajax({
			data : {
				name : $('#poly_1').val(),
				email : $('#poly_2').val()
			},
			type : 'POST',
			url : '/sub'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#poly_result').val(data.name);
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

	$('#btn_div').click( function(event) {

		$.ajax({
			data : {
				name : $('#poly_1').val(),
				email : $('#poly_2').val()
			},
			type : 'POST',
			url : '/div'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#poly_result').val(data.name);
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});