Feature: en tant que visiteur je peux voir les clubs et leurs points restants

Scenario: je vais directement voir le tableau de points

  Given le club 'first' ayant 5 points
  And le club 'second' ayant 12 points
  And le club 'third' ayant 7 points

  When je consulte le tableau de points

  Then je vois dans le tableau que 'first' a 5 points
  And je vois dans le tableau que 'second' a 12 points
  And je vois dans le tableau que 'third' a 7 points


Scenario: je vais voir le tableau de points après réservation

  Given le club 'first' ayant 5 points
  And le club 'second' ayant 12 points
  And le club 'third' ayant 7 points

  When je réserve 4 places pour 'second'
  And je consulte le tableau de points

  Then je vois dans le tableau que 'first' a 5 points
  And je vois dans le tableau que 'second' a 8 points
  And je vois dans le tableau que 'third' a 7 points