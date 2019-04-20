console.log('Hello World!')

function toggleForm(){
  let id = $(this).attr('id')
  let button = $('#sub-data')

  if(id == 'signup'){
    $(button).text('SIGN UP')
    let confirmPassword = $('#confirm-pw-template').html()
    $(confirmPassword).insertBefore($('#sub-data'))
  }

  if(id == 'signin'){
    $(button).text('SIGN IN')
    $('#confirm-password-group').remove()
  }
}


$('.btn').on('click', toggleForm)
