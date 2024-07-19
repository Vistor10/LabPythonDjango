document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registerform');
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password1 = document.getElementById('password1');
    const password2 = document.getElementById('password2');
    const rol = document.getElementById('rol');
    const fecha = document.getElementById('fecha');
    const certform = document.getElementById('certificado');

    form.addEventListener('submit', e => {
        e.preventDefault();
        if (validateInputs()) {
            form.submit();  // Envía el formulario si la validación es exitosa
            window.location.href = homeUrl;  // Redirige al usuario a la página de inicio
        }
    });

    const setError = (element, message) => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.error');

        errorDisplay.innerText = message;
        inputControl.classList.add('error');
        inputControl.classList.remove('success');
    };

    const setSuccess = element => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.error');

        errorDisplay.innerText = '';
        inputControl.classList.add('success');
        inputControl.classList.remove('error');
    };

    const isValidEmail = email => {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    };

    const validateDateOfBirth = () => {
        const fechaValue = new Date(fecha.value);

        if (isNaN(fechaValue.getTime()) || fechaValue.getFullYear() < 1900 || fechaValue.getFullYear() > new Date().getFullYear()) {
            setError(fecha, 'Por favor ingrese una fecha de nacimiento válida');
            return false;
        } else {
            setSuccess(fecha);
            return true;
        }
    };

    const validateInputs = () => {
        const usernameValue = username.value.trim();
        const emailValue = email.value.trim();
        const password1Value = password1.value.trim();
        const password2Value = password2.value.trim();
        const rolValue = rol.value;
        const fechaValue = fecha.value;
        const certformValue = certform.value;

        let isValid = true;

        if (usernameValue === '') {
            setError(username, 'Se requiere que ingrese un nombre');
            isValid = false;
        } else {
            setSuccess(username);
        }

        if (emailValue === '') {
            setError(email, 'Se requiere un correo');
            isValid = false;
        } else if (!isValidEmail(emailValue)) {
            setError(email, 'Ingrese un correo electrónico válido');
            isValid = false;
        } else {
            setSuccess(email);
        }

        if (password1Value === '') {
            setError(password1, 'Se requiere una contraseña');
            isValid = false;
        } else if (password1Value.length < 8) {
            setError(password1, 'La contraseña debe tener al menos 8 caracteres.');
            isValid = false;
        } else {
            setSuccess(password1);
        }

        if (password2Value === '') {
            setError(password2, 'Por favor confirma tu contraseña');
            isValid = false;
        } else if (password2Value !== password1Value) {
            setError(password2, 'Las contraseñas no coinciden');
            isValid = false;
        } else {
            setSuccess(password2);
        }

        if (!rolValue) {
            setError(rol, 'Seleccione un rol');
            isValid = false;
        } else {
            setSuccess(rol);
        }

        if (!fechaValue) {
            setError(fecha, 'Seleccione su fecha de nacimiento');
            isValid = false;
        } else {
            if (!validateDateOfBirth()) {
                isValid = false;
            }
        }

        if (rolValue === 'dueño' && !certformValue) {
            setError(certform, 'Por favor adjunte su certificado de dueño');
            isValid = false;
        } else {
            setSuccess(certform);
        }

        return isValid;
    };
});
