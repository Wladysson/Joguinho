<?php

class CasinoController {
    private $db;

    public function __construct($database) {
        $this->db = $database;
    }

    public function placeBet($userId, $betAmount) {
        // Obtém o saldo do usuário
        $stmt = $this->db->prepare("SELECT money FROM users WHERE id = :id");
        $stmt->execute(['id' => $userId]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        
        if (!$user) {
            return ['error' => 'Usuário não encontrado.'];
        }

        $currentMoney = $user['money'];
        
        // Verifica se o usuário tem saldo suficiente
        if ($betAmount > $currentMoney) {
            return ['error' => 'Saldo insuficiente.'];
        }

        // Deduz a aposta do saldo
        $newMoney = $currentMoney - $betAmount;
        $updateStmt = $this->db->prepare("UPDATE users SET money = :money WHERE id = :id");
        $updateStmt->execute(['money' => $newMoney, 'id' => $userId]);
        
        // Simula um resultado (exemplo: 50% de chance de ganhar o dobro)
        $win = rand(0, 1) === 1;
        if ($win) {
            $newMoney += $betAmount * 2;
            $updateStmt->execute(['money' => $newMoney, 'id' => $userId]);
            return ['success' => true, 'message' => 'Você ganhou!', 'new_balance' => $newMoney];
        }

        return ['success' => false, 'message' => 'Você perdeu.', 'new_balance' => $newMoney];
    }
}

// Exemplo de uso
try {
    $pdo = new PDO('pgsql:host=localhost;dbname=casino', 'user', 'password');
    $casino = new CasinoController($pdo);
    
    $response = $casino->placeBet(1, 50); // Apostando 50
    echo json_encode($response);
} catch (PDOException $e) {
    echo json_encode(['error' => 'Erro no banco de dados: ' . $e->getMessage()]);
}