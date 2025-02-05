<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $mensagem = $_POST['mensagem'] ?? null;

    if (!$mensagem) {
        die("Mensagem não pode estar vazia.");
    }

    $files = scandir("./");
    $num_files = count($files) - 2;

    $fileName = "msg-{$num_files}.txt";

    $file = fopen("./messages/{$fileName}", "x");

    if ($file) {
        fwrite($file, $mensagem);
        fclose($file);
        header("Location: index.php");
        exit();
    } else {
        die("Erro ao criar o arquivo.");
    }
} else {
    die("Método de requisição inválido.");
}
?>
