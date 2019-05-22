console.log('Hello World!')

$.fn.exists = function () {
    return this.length !== 0;
}

function toggleForm(){
  let id = $(this).attr('id')
  let button = $('#sub-data')

  if(id == 'signup' && !$('#confirm-password-group').exists()){
    $(button).text('SIGN UP')
    let confirmPassword = $('#confirm-pw-template').html()
    $(confirmPassword).insertBefore($('#sub-data'))
    $('#authForm').attr('action', '/signup')
  }

  if(id == 'signin' && $('#confirm-password-group').exists()){
    $(button).text('SIGN IN')
    $('#authForm').attr('action', '/signin')
    $('#confirm-password-group').remove()
  }
}


$('.btn').on('click', toggleForm)
