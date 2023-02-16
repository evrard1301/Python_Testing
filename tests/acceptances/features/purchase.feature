Feature: en tant que club je peux dépenser mes points afin de réserver de place pour une compétition donnée


Scenario: je possède assez de points et la compétition possède assez de places

  Given mon club ayant 5 points
  And une compétition ayant 15 places

  When je réserve 3 places

  Then il me reste 2 points
  And il reste 12 places à la compétition


Scenario: je possède assez de points et la compétition possède assez de places pour deux achats

  Given mon club ayant 5 points
  And une compétition ayant 15 places

  When je réserve 3 places
  And je réserve 2 places

  Then il me reste 0 point
  And il reste 10 places à la compétition


Scenario: je ne possède pas assez de points

  Given mon club ayant 5 points
  And une compétition ayant 15 places

  When je réserve 6 places

  Then il me reste 5 points
  And il reste 15 places à la compétition
  And je vois 'not enough point'



Scenario: il ne reste pas assez de place pour la compétition

  Given mon club ayant 5 points
  And une compétition ayant 3 places

  When je réserve 4 places

  Then il me reste 5 points
  And il reste 3 places à la compétition
  And je vois 'not enough places'


Scenario: je veux réserver plus de 12 places en une fois

  Given mon club ayant 30 points
  And une compétition ayant 50 places

  When je réserve 13 places

  Then il me reste 30 points
  And il reste 50 places à la compétition
  And je vois 'cannot purchase more than 12 places'


Scenario: je veux réserver plus de 12 places en deux fois

  Given mon club ayant 30 points
  And une compétition ayant 50 places

  When je réserve 8 places
  And je réserve 5 places

  Then il me reste 22 points
  And il reste 42 places à la compétition
  And je vois 'cannot purchase more than 12 places'


Scenario: la compétition est déjà terminée

  Given mon club ayant 5 points
  And une compétition ayant 15 places
  And la compétition se déroule le '2000-1-1 00:00:00'
  
  When je réserve 3 places

  Then il me reste 5 points
  And il reste 15 places à la compétition
  And je vois 'cannot purchase a terminated competition'