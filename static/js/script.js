// Set default background on load
$(document).ready(function () {
  $('body').addClass('diabetes-bg');

  if ($('.result-card').length) {
    $('html, body').animate({
      scrollTop: $('.result-card').offset().top - 80
    }, 600);
  }
});

// Show correct form + change background
function showForm(disease) {
  $('#diabetes-form').addClass('d-none');
  $('#heart-form').addClass('d-none');
  $('#btn-diabetes').removeClass('active-disease');
  $('#btn-heart').removeClass('active-disease');

  if (disease === 'diabetes') {
    $('#diabetes-form').removeClass('d-none');
    $('#btn-diabetes').addClass('active-disease');
    $('body').removeClass('heart-bg').addClass('diabetes-bg');
  } else {
    $('#heart-form').removeClass('d-none');
    $('#btn-heart').addClass('active-disease');
    $('body').removeClass('diabetes-bg').addClass('heart-bg');
  }
}

// Form validation for Diabetes
$('#form-diabetes').on('submit', function (e) {
  let valid = true;
  $(this).find('input[type="number"]').each(function () {
    if ($(this).val() === '') {
      $(this).addClass('is-invalid');
      valid = false;
    } else {
      $(this).removeClass('is-invalid');
    }
  });
  if (!valid) {
    e.preventDefault();
    alert('⚠️ Please fill in all fields before predicting!');
  } else {
    $('#form-diabetes button[type="submit"]').text('Analyzing... ⏳').prop('disabled', true);
  }
});

// Form validation for Heart Disease
$('#form-heart').on('submit', function (e) {
  let valid = true;
  $(this).find('input[type="number"]').each(function () {
    if ($(this).val() === '') {
      $(this).addClass('is-invalid');
      valid = false;
    } else {
      $(this).removeClass('is-invalid');
    }
  });
  if (!valid) {
    e.preventDefault();
    alert('⚠️ Please fill in all fields before predicting!');
  } else {
    $('#form-heart button[type="submit"]').text('Analyzing... ⏳').prop('disabled', true);
  }
});