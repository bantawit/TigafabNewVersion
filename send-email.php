<?php
require 'PHPMailer/PHPMailerAutoload.php';

// Configuración SMTP de DinaHosting
$smtp_host = 'tigafab-traductores-com.correoseguro.dinaserver.com';
$smtp_port = 465;
$smtp_username = 'web@tigafab-traductores.com';
$smtp_password = 'LQlz9b7$5*?6';
$smtp_secure = 'ssl';

// Configuración del correo
$from_email = 'web@tigafab-traductores.com';
$from_name = 'TIGAFAB - Traductores Jurados';
$to_email = 'fatima@tigafab-traductores.com';
$subject = 'Nuevo contacto desde web TIGAFAB';

// Procesar formulario
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = htmlspecialchars(isset($_POST['name']) ? $_POST['name'] : '');
    $email = htmlspecialchars(isset($_POST['email']) ? $_POST['email'] : '');
    $phone = htmlspecialchars(isset($_POST['phone']) ? $_POST['phone'] : '');
    $language = htmlspecialchars(isset($_POST['language']) ? $_POST['language'] : '');
    $message = htmlspecialchars(isset($_POST['message']) ? $_POST['message'] : '');
    
    // Validar campos requeridos
    if (empty($name) || empty($email) || empty($message)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'Por favor completa todos los campos requeridos']);
        exit;
    }
    
    // Validar email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'Por favor ingresa un email válido']);
        exit;
    }
    
    try {
        $mail = new PHPMailer;
        
        // Configuración SMTP
        $mail->isSMTP();
        $mail->Host = $smtp_host;
        $mail->SMTPAuth = true;
        $mail->Username = $smtp_username;
        $mail->Password = $smtp_password;
        $mail->SMTPSecure = $smtp_secure;
        $mail->Port = $smtp_port;
        
        // Configuración del correo
        $mail->setFrom($from_email, $from_name);
        $mail->addAddress($to_email);
        $mail->addReplyTo($email, $name);
        
        // Asunto
        $mail->Subject = $subject;
        
        // Cuerpo del correo en HTML
        $mail->isHTML(true);
        $mail->Body = "
            <html>
            <head>
                <style>
                    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
                    .container { max-width: 600px; margin: 0 auto; padding: 20px; }
                    .header { background: #c2a35d; color: white; padding: 20px; text-align: center; }
                    .content { background: #f9f9f9; padding: 20px; border-radius: 5px; margin-top: 20px; }
                    .field { margin-bottom: 15px; }
                    .label { font-weight: bold; color: #c2a35d; }
                    .value { margin-top: 5px; }
                    .footer { text-align: center; margin-top: 20px; color: #666; font-size: 12px; }
                </style>
            </head>
            <body>
                <div class='container'>
                    <div class='header'>
                        <h2>Nuevo Contacto desde Web TIGAFAB</h2>
                    </div>
                    <div class='content'>
                        <div class='field'>
                            <div class='label'>Nombre Completo:</div>
                            <div class='value'>$name</div>
                        </div>
                        <div class='field'>
                            <div class='label'>Correo Electrónico:</div>
                            <div class='value'>$email</div>
                        </div>
                        <div class='field'>
                            <div class='label'>Teléfono:</div>
                            <div class='value'>$phone</div>
                        </div>
                        <div class='field'>
                            <div class='label'>Idioma de Traducción:</div>
                            <div class='value'>$language</div>
                        </div>
                        <div class='field'>
                            <div class='label'>Mensaje:</div>
                            <div class='value'>$message</div>
                        </div>
                    </div>
                    <div class='footer'>
                        <p>Este correo fue enviado desde el formulario de contacto de tigafab-traductores.com</p>
                        <p>Fecha: " . date('d/m/Y H:i') . "</p>
                    </div>
                </div>
            </body>
            </html>
        ";
        
        // Versión texto plano
        $mail->AltBody = "Nuevo Contacto desde Web TIGAFAB\n\nNombre: $name\nEmail: $email\nTeléfono: $phone\nIdioma: $language\nMensaje: $message";
        
        // Manejar archivos adjuntos (múltiples)
        if (isset($_FILES['attachments']) && is_array($_FILES['attachments']['name'])) {
            $files = $_FILES['attachments'];
            $max_files = 5; // Máximo 5 archivos
            $file_count = 0;
            
            for ($i = 0; $i < count($files['name']); $i++) {
                if ($files['error'][$i] === UPLOAD_ERR_OK) {
                    $file_count++;
                    if ($file_count > $max_files) {
                        http_response_code(400);
                        echo json_encode(['success' => false, 'message' => 'Máximo 5 archivos permitidos']);
                        exit;
                    }
                    
                    $file_tmp = $files['tmp_name'][$i];
                    $file_name = $files['name'][$i];
                    $file_size = $files['size'][$i];
                    
                    // Validar tamaño (máximo 10MB)
                    if ($file_size > 10 * 1024 * 1024) {
                        http_response_code(400);
                        echo json_encode(['success' => false, 'message' => 'El archivo ' . $file_name . ' es demasiado grande (máximo 10MB)']);
                        exit;
                    }
                    
                    // Validar tipo MIME
                    $allowed_types = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/zip', 'application/x-zip-compressed'];
                    $file_type = $files['type'][$i];
                    
                    if (!in_array($file_type, $allowed_types)) {
                        http_response_code(400);
                        echo json_encode(['success' => false, 'message' => 'Tipo de archivo no permitido: ' . $file_name]);
                        exit;
                    }
                    
                    // Validar extensión de archivo
                    $allowed_extensions = ['pdf', 'doc', 'docx', 'zip'];
                    $file_ext = strtolower(pathinfo($file_name, PATHINFO_EXTENSION));
                    
                    if (!in_array($file_ext, $allowed_extensions)) {
                        http_response_code(400);
                        echo json_encode(['success' => false, 'message' => 'Extensión de archivo no permitida: ' . $file_name]);
                        exit;
                    }
                    
                    // Sanitizar nombre de archivo (eliminar caracteres peligrosos)
                    $safe_name = preg_replace('/[^a-zA-Z0-9._-]/', '_', $file_name);
                    
                    // Validar que el archivo sea realmente del tipo que dice ser
                    $finfo = finfo_open(FILEINFO_MIME_TYPE);
                    $real_type = finfo_file($finfo, $file_tmp);
                    finfo_close($finfo);
                    
                    if (!in_array($real_type, $allowed_types)) {
                        http_response_code(400);
                        echo json_encode(['success' => false, 'message' => 'El archivo ' . $file_name . ' no es válido']);
                        exit;
                    }
                    
                    $mail->addAttachment($file_tmp, $safe_name);
                }
            }
        }
        
        // Enviar correo
        if ($mail->send()) {
            // Devolver JSON de éxito en lugar de redirección
            echo json_encode(['success' => true, 'redirect' => 'gracias.html']);
            exit;
        } else {
            http_response_code(500);
            echo json_encode(['success' => false, 'message' => 'Error al enviar el correo: ' . $mail->ErrorInfo]);
            exit;
        }
        
    } catch (phpmailerException $e) {
        http_response_code(500);
        echo json_encode(['success' => false, 'message' => 'Error PHPMailer: ' . $e->errorMessage()]);
        exit;
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['success' => false, 'message' => 'Error: ' . $e->getMessage()]);
        exit;
    }
} else {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Método no permitido']);
    exit;
}
