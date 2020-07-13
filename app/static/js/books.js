const range = document.querySelector('#range'),
	progressbar = document.querySelector('.progress-bar');
  
  
range.addEventListener('input', function(){
	const value = range.value;
  progressbar.style.setProperty('--progress', value)
})