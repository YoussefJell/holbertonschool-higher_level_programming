function ToggleClass (sender) {
  if ($(sender).hasClass('green')) {
    $(sender).removeClass('green');
    $(sender).addClass('red');
  } else {
    $(sender).removeClass('red');
    $(sender).addClass('green');
  }
}

$('DIV#toggle_header').click(function () {
  ToggleClass('DIV#toggle_header');
});
