<?php

class Hobbit extends Character {

    private string $sentence;
    private string $name;
    private int $health;
    private array|int $position;
    private int $speed;
    private int $coins;

    public function __construct($values) {
        parent::__construct($values);

        $this->speed = 5;
        $this->sentence = "Belle journée ma foi";
    }
    public function talk() {
        echo ($this->sentence);
    }



}