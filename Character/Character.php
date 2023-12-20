<?php

abstract class Character {

    private string $name;
    private int $health;
    private array|int $position;
    private int $speed;
    private int $coins;

    public function __construct(array $values) {
        $this->name = $values['name'];
        $this->health = $values['health'];
        $this->position = $values['position'];
        $this->coins = 0;
    }

    public function setName(string $name) {
        $this->validateStr($name);
        $this->name = $name;
        return $this;
    }
    public function setHealth(int $health) {
        $this->validateInt($health);
        $this->health = $health;
        return $this;
    }
    public function setPosition(array $position) {
        if (!isset($position['x']) && !isset($position['y'])) {
            throw new Exception("Error Processing Request", 1);
        }
        $this->validateInt($position['x']);
        $this->validateInt($position['y']);
        $this->position = $position;
        return $this;
    }
    public function setSpeed(int $speed) {
        $this->validateInt($speed);
        $this->speed = $speed;
        return $this;
    }
    public function setCoins(int $coins) {
        $this->validateInt($coins);
        $this->coins = $coins;
        return $this;
    }



    public function getName() {
        return $this->name;
    }
    public function getHealth() {
        return $this->health;
    }
    public function getPosition() {
        return $this->position;
    }
    public function getSpeed() {
        return $this->speed;
    }
    public function getCoins() {
        return $this->coins;
    }
    
    private function validateStr($string){
        if(strlen($string) == 0 || !preg_match("/^[A-z]+$/", $string)) {
            throw new Exception("Error Processing Request", 1);
        }
    }
    
    public static function validateInt(int $int) {
        if(strlen($int) == 0 || !preg_match("/^[0-9]+$/", $int)) {
            throw new Exception("Error Processing Request", 1);
        }
    }

    abstract protected function talk();

}