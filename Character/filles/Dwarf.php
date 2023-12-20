<?php

class Dwarf extends Character {
    use Thief;
    use Warrior;

    private string $sentence;
    private string $name;
    private int $health;
    private array|int $position;
    private int $speed;
    private int $coins;

    public function __construct($values) {
        parent::__construct($values);

        $this->dexterity = 50;
        $this->strenght = 3;

        $this->speed = 2;
        $this->sentence = "Groumpf";
    }
    public function talk() {
        echo ($this->sentence);
    }



}