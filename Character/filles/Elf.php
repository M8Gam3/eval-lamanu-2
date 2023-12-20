<?php

class Elf extends Character {

    private string $sentence;
    private string $name;
    private int $health;
    private array|int $position;
    private int $speed;
    private int $coins;

    public function __construct($values) {
        parent::__construct($values);

        $this->speed = 7;
        $this->sentence = "Eldarie";
    }

    public function talk() {
        echo ($this->sentence);
    }



}