<?php

class Human extends Character {
    use Magician;
    
    private string $sentence;
    private string $name;
    private int $health;
    private array|int $position;
    private int $speed;
    private int $coins;

    public function __construct($values) {
        parent::__construct($values);

        $this->magic = 2;

        $this->speed = 5;
        $this->sentence = "Bonjour, je suis " . $this->name;
    }

    public function talk() {
        echo ($this->sentence);
    }



}