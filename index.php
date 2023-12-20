<?php

require_once('./Character/Character.php');

require_once('./Character/filles/Dwarf.php');
require_once('./Character/filles/Human.php');
require_once('./Character/traits/Thief.php');
require_once('./Character/traits/Warrior.php');


$values['name'] = 'midir';
$values['health'] = 8;
$position ['x'] = 1;
$position ['y'] = 3;
$values['position'] = $position;

$unNain = new Dwarf($values);

$unNain->setCoins(10);

$values['name'] = 'Joseph';
$values['health'] = 5;
$position ['x'] = 2;
$position ['y'] = 4;
$values['position'] = $position;

$unHumain = new Human($values);


$unHumain->talk();
$unNain->talk();


$unHumain->setCoins(100);


$unNain->steal($unHumain);


$unHumain->castSpell($unNain);


$unNain->attack($unHumain);