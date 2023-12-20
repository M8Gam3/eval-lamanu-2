<?php

trait Magician {

    private int $magic = 1;

    public function setMagic($magic){
        $this->magic = $magic;
    }

    public function castSpell($target) {
        $target->health -= $this->magic;
    }

}