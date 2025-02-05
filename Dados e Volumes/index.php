<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mensagem</title>
</head>
<body>
    <h1>Envie sua mensagem</h1>
    <form action="processa.php" method="POST">
        <label for="mensagem">Mensagem:</label>
        <input type="text" name="mensagem" id="mensagem" required>
        <input type="submit" value="Enviar mensagem">
    </form>
</body>
</html>
d