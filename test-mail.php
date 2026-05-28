<?php
// Script de prueba para mail()
if (function_exists('mail')) {
    echo "mail() está disponible<br>";
    
    $to = 'fatima@tigafab-traductores.com';
    $subject = 'Prueba de correo';
    $message = 'Este es un correo de prueba desde el servidor.';
    $headers = 'From: web@tigafab-traductores.com';
    
    if (mail($to, $subject, $message, $headers)) {
        echo "Correo enviado exitosamente";
    } else {
        echo "Error al enviar correo";
    }
} else {
    echo "mail() NO está disponible";
}
