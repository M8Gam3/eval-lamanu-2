<?php

trait Thief {

    private int $dexterity = 1;

    public function setStrenght($dexterity){
        if (!($dexterity > 0) || !($dexterity <= 100)) {
            throw new Exception("Error Processing Request", 1);
        }
        $this->dexterity = $dexterity;
    }

    public function steal($target) {
        if ($this->dexterity > rand(1, 100))
        parent::$coins += $target->coins;
        $target->coins = 0;
    }

}