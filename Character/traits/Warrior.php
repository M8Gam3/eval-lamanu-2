<?php

trait Warrior {

    private int $strenght = 1;

    public function setStrenght($strenght){
        $this->strenght = $strenght;
    }

    public function attack($target) {
        $target->health -= $this->strenght;
    }

}