	console.log("¡Hola, mundo!"); // Imprime "¡Hola, mundo!" en la consola

	document.addEventListener('DOMContentLoaded', function () {
		const registroForm = document.getElementById('seleccion-form');
		const procesandoDiv = document.getElementById('procesando');
		console.log('Entre a script')

		registroForm.addEventListener('submit', function (event) {
			event.preventDefault(); // Evita que el formulario se envíe de inmediato
	
			// Muestra la imagen de "procesando"
			procesandoDiv.style.display = 'block';
			console.log('Imprimio block')
	
			// Simula un proceso de grabación (puedes reemplazar esto con tu lógica real)
			setTimeout(function () {
				// Aquí iría la lógica para enviar el registro al servidor (por ejemplo, mediante una petición AJAX)
				// Por ahora, simplemente ocultamos la imagen de "procesando"
				//procesandoDiv.style.display = 'none';
				alert('Auditoria importada correctamente.');
			}, 20000000); // Simulamos un proceso de 2 segundos
		});
	});
	
