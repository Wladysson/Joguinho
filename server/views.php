<?php
$user = [
    'money' => 1000.00  // Exemplo de saldo do usuário
];

// Verificar se foi enviado um valor de aposta
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $betAmount = floatval($_POST['bet_amount']);
    
    if ($betAmount <= 0) {
        echo "Valor da aposta inválido!";
    } elseif ($betAmount > $user['money']) {
        echo "Você não tem saldo suficiente para essa aposta!";
    } else {
        // Chama a função de processamento da aposta
        processBet($betAmount, $user);
    }
}

function processBet($betAmount, $user) {
    // Simula o resultado da aposta (exemplo simples)
    $result = rand(0, 1) == 0 ? 'perdeu' : 'ganhou';
    
    // Atualiza o saldo de acordo com o resultado
    if ($result == 'ganhou') {
        $user['money'] += $betAmount;  // O usuário ganha
    } else {
        $user['money'] -= $betAmount;  // O usuário perde
    }
    
    // Exibe o resultado
    echo "Resultado da aposta: Você {$result}! Saldo atual: R$ " . number_format($user['money'], 2, ',', '.');
}
?>
