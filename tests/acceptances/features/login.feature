Feature: en tant que secrétaire d'un club, je peux
saisir mon adresse email afin de me connecter


Scenario: mon adresse email est valide
  Given mon adresse email est 'hello@world.com'
  
    When je me connecte avec 'hello@world.com'

    Then je vois 'Welcome, hello@world.com'


Scenario: mon adresse email n'est pas valide
  Given mon adresse email est 'hello@world.com'
  
    When je me connecte avec 'another@email.com'
    
    Then je vois 'wrong credentials'