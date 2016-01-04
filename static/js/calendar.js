$.datetimepicker.setLocale('uk');
function DiffArrays(A,B)
{
    var M = A.length, N = B.length, c = 0, C = [];
    for (var i = 0; i < M; i++)
     { var j = 0, k = 0;
       while (B[j] !== A[ i ] && j < N) j++;
       while (C[k] !== A[ i ] && k < c) k++;
       if (j == N && k == c) C[c++] = A[ i ];
     }
   return C;
}
$('#datetimepicker2').datetimepicker({
     onGenerate:function( ct ){
    jQuery(this).find('.xdsoft_date')
      .toggleClass('xdsoft_enabled');
  },
	timepicker:false,
	format:'Y-m-d',
	formatDate:'Y-m-d',
	minDate:'0',
    onChangeDateTime :function() {
    var date = $("#datetimepicker2").val();
        $.ajax({
            type: 'GET',
            url: "/date_from_ajax/",
            data: {
                "data": date
            },
            dataType: 'json',
            success: function (dat) {
                var allow = ['08:00', '10:00', '12:00', '14:00', '16:00'];
                var a0;
                a0=DiffArrays(allow,dat['time_list']);
                $('#disableTimeRangesExample').datetimepicker({
                    datepicker: false,
                    timepicker: true,
                    format: 'H:i',
                    allowTimes:a0
                });

            }
        });

    }
});