/** @format */
function changeMode() {
	changeClasses();
	changeText();
}

function changeClasses() {
	buttonLightDark.classList.toggle(darkModeClass);
	// h1.classList.toggle(darkModeClass);
	body.classList.toggle(darkModeClass);
	// footer.classList.toggle(darkModeClass);
}

function changeText() {
	const lightMode = 'Light Mode';
	const darkMode = 'Dark Mode';

	if (body.classList.contains(darkModeClass)) {
		buttonLightDark.innerHTML = lightMode;
		// h1.innerHTML = darkMode + ' ON';
		// titulo.innerHTML = darkMode;

		return;
	}

	buttonLightDark.innerHTML = darkMode;
	// h1.innerHTML = lightMode + ' ON';
	// titulo.innerHTML = lightMode;
}

const darkModeClass = 'dark-mode';
const buttonLightDark = document.getElementById('mode-selector');
const h1 = document.getElementById('page-title');
const body = document.getElementsByTagName('body')[0];
const footer = document.getElementsByTagName('footer')[0];
const titulo = document.getElementById('titulo');

buttonLightDark.addEventListener('click', changeMode);
