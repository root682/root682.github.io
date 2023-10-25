<?php
// Establecer la conexión a la base de datos
$servername = "root682.github.io"; // Cambia a la dirección de tu servidor MySQL
$username = "Hackvenom"; // Cambia a tu nombre de usuario de MySQL
$password = "Isaac_2005"; // Cambia a tu contraseña de MySQL
$dbname = "mydatabase.sql"; // Cambia al nombre de tu base de datos

$conn = new mysqli($servername, $username, $password, $dbname);

// Comprobar la conexión
if ($conn->connect_error) {
    die("La conexión a la base de datos falló: " . $conn->connect_error);
}

// Comprobar si se ha enviado el formulario de registro
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $newUsername = $_POST["newUsername"];
    $newPassword = password_hash($_POST["newPassword"], PASSWORD_BCRYPT); // Almacenar contraseñas de forma segura

    // Insertar los datos en la base de datos (debes realizar más validaciones en una aplicación real)
    $sql = "INSERT INTO usuarios (username, password) VALUES (?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ss", $newUsername, $newPassword);

    if ($stmt->execute()) {
        echo "Registro exitoso. Bienvenido, " . $newUsername;
    } else {
        echo "Error al registrar el usuario: " . $stmt->error;
    }

    $stmt->close();
}

// Cerrar la conexión a la base de datos
$conn->close();
?>
