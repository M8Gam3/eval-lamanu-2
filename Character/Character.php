<?php

abstract class Character {

    private string $name;
    private int $health;
    private array|int $position;
    private int $speed;
    private int $coins;

    /**
     * [Description for __construct]
     *
     * @param array $values
     * 
     */
    public function __construct(array $values) {
        $this->name = $values['name'];
        $this->health = $values['health'];
        $this->position = $values['position'];
        $this->coins = 0;
    }

    /**
     * [Description for setName]
     *
     * @param string $name
     * 
     * @return [type]
     * 
     */
    public function setName(string $name) {
        $this->validateStr($name);
        $this->name = $name;
        return $this;
    }
    /**
     * [Description for setHealth]
     *
     * @param int $health
     * 
     * @return [type]
     * 
     */
    public function setHealth(int $health) {
        $this->validateInt($health);
        $this->health = $health;
        return $this;
    }
    /**
     * [Description for setPosition]
     *
     * @param array $position
     * 
     * @return [type]
     * 
     */
    public function setPosition(array $position) {
        if (!isset($position['x']) && !isset($position['y'])) {
            throw new Exception("Error Processing Request", 1);
        }
        $this->validateInt($position['x']);
        $this->validateInt($position['y']);
        $this->position = $position;
        return $this;
    }
    /**
     * [Description for setSpeed]
     *
     * @param int $speed
     * 
     * @return [type]
     * 
     */
    public function setSpeed(int $speed) {
        $this->validateInt($speed);
        $this->speed = $speed;
        return $this;
    }
    /**
     * [Description for setCoins]
     *
     * @param int $coins
     * 
     * @return [type]
     * 
     */
    public function setCoins(int $coins) {
        $this->validateInt($coins);
        $this->coins = $coins;
        return $this;
    }



    /**
     * [Description for getName]
     *
     * @return [type]
     * 
     */
    public function getName() {
        return $this->name;
    }
    /**
     * [Description for getHealth]
     *
     * @return [type]
     * 
     */
    public function getHealth() {
        return $this->health;
    }
    /**
     * [Description for getPosition]
     *
     * @return [type]
     * 
     */
    public function getPosition() {
        return $this->position;
    }
    /**
     * [Description for getSpeed]
     *
     * @return [type]
     * 
     */
    public function getSpeed() {
        return $this->speed;
    }
    /**
     * [Description for getCoins]
     *
     * @return [type]
     * 
     */
    public function getCoins() {
        return $this->coins;
    }
    
    /**
     * [Description for validateStr]
     *
     * @param mixed $string
     * 
     * @return [type]
     * 
     */
    private function validateStr($string){
        if(strlen($string) == 0 || !preg_match("/^[A-z]+$/", $string)) {
            throw new Exception("Error Processing Request", 1);
        }
    }
    
    /**
     * [Description for validateInt]
     *
     * @param int $int
     * 
     * @return [type]
     * 
     */
    public static function validateInt(int $int) {
        if(strlen($int) == 0 || !preg_match("/^[0-9]+$/", $int)) {
            throw new Exception("Error Processing Request", 1);
        }
    }

    /**
     * [Description for talk]
     *
     * @return [type]
     * 
     */
    abstract protected function talk();

}