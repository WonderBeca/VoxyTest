function isEmpty(str) {
	// Guarantee that the user cannot send a text with empty spaces
	return !str.trim().length;
}

function readMyText() {
	text = document.getElementById('myWords').value

	var myWords = {
		"message": text
	};

	return myWords;
}

function check_text(params) {
	if( isEmpty(document.getElementById('myWords').value) ) {
		document.getElementById("empty-error").className = 'bar-error-show';
		// Guarantee that the outputs will be empty after more than one usage
		document.getElementById('characterCount').textContent = '';
		document.getElementById('wordCount').textContent = '';
		document.getElementById('sentenceCount').textContent = '';
		document.getElementById('paragraphCount').textContent = '';
		return false
	} else {
		document.getElementById("empty-error").className = 'bar-error-hidden';
	return true
	}
}

async function postMyWords() {
	if (check_text() == true ){
	const myWords = readMyText();

	const response = await fetch('/word_counter/', {
		method: 'POST',
		headers :{
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(myWords)
	})
	.then(response => response.json())
	.then(data => {
		console.log('Sucess:', data);
		console.log(data.character);
		// Update values after every sucessfull request
		document.getElementById('characterCount').textContent = data.characters;
		document.getElementById('wordCount').textContent = data.words;
		document.getElementById('sentenceCount').textContent = data.sentences;
		document.getElementById('paragraphCount').textContent = data.paragraphs;
	})
	.then((error) => {
		console.error('Error:', error);
	});
}}