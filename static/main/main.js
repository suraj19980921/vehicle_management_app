
function vehicleDetail(vehicleId){

        $.ajax({
            type: "get",
            url: '/vehicle_detail/'+vehicleId,
            data: vehicleId,
            success: function (response) {
                $('#addUpdateForm').attr('action','/update_vehicle/'+vehicleId);
                $('#addUpdateModalLabel').text('Update Vehicle Form');
                $('#addUpdateButton').text('Update');
                $('#addUpdateForm #id_name').val(response.vehicle[0].fields.name);
                $('#addUpdateForm #id_speed').val(response.vehicle[0].fields.speed);
                $('#addUpdateForm #id_average_speed').val(response.vehicle[0].fields.average_speed);
                $('#addUpdateForm #id_temperature').val(response.vehicle[0].fields.temperature);
                $('#addUpdateForm #id_fuel_level').val(response.vehicle[0].fields.fuel_level);
                $('#addUpdateForm #id_engine_status').val(response.vehicle[0].fields.engine_status);
            }
        });
}

$('#addVehicle').click(function(){
    $('#addUpdateForm').attr('action','/add_vehicle/');
    $('#addUpdateModalLabel').text('Add Vehicle Form');
    $('#addUpdateButton').text('Add');
    $('#addUpdateForm').find("input").not("input['type=hidden']").val("");
});

function deleteVehicle(vehicleId) {

    $('#deleteForm').attr('action','/delete_vehicle/'+vehicleId);
    
}
    
$('#on-switch').click(function(){
    $(this).css({'background-color':'lightgreen','color':'white'});
    $('#off-switch').css({'background-color':'white','color':'red'});
})

$('#off-switch').click(function(){
    $(this).css({'background-color':'red','color':'white'});
    $('#on-switch').css({'background-color':'white','color':'lightgreen'});
})

$('.toggle-button').click(function(){
    
    $('.side-navbar').show();
});

$('.close-button').click(function(){
    $('.side-navbar').hide();
})


$(window).resize(function() {
   
    if($(window).width() > 1080)
     {
        $('.side-navbar').show();
     }
     else{
        $('.side-navbar').hide();
     }
   
});



$('#camera1-btn').click(function(){

    $('#camera1-image').css({'display':'block'});
    $('#camera2-image').css({'display':'none'});

});

$('#camera2-btn').click(function(){
   
    $('#camera2-image').css({'display':'block'});
    $('#camera1-image').css({'display':'none'});

});





