<?php

class User {
    private $id;
    private $username;
    private $money;

    public function __construct($id, $username, $money) {
        $this->id = $id;
        $this->username = $username;
        $this->money = $money;
    }

    public function getId() {
        return $this->id;
    }

    public function getUsername() {
        return $this->username;
    }

    public function getMoney() {
        return $this->money;
    }

    public function setMoney($amount) {
        $this->money = $amount;
    }
}

class Bet {
    private $id;
    private $userId;
    private $amount;
    private $result;
    private $timestamp;

    public function __construct($id, $userId, $amount, $result, $timestamp) {
        $this->id = $id;
        $this->userId = $userId;
        $this->amount = $amount;
        $this->result = $result;
        $this->timestamp = $timestamp;
    }

    public function getId() {
        return $this->id;
    }

    public function getUserId() {
        return $this->userId;
    }

    public function getAmount() {
        return $this->amount;
    }

    public function getResult() {
        return $this->result;
    }

    public function getTimestamp() {
        return $this->timestamp;
    }
}