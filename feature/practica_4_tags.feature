

Feature: Primer Demo

    Background: 
        Given Navegar al sitio web
                

    Scenario Outline: Scenario Outline name: Probando otro inicio de sesión con parámetros
        When Ingresa el nombre de "<nombre>"
        And Ingresa la "<contraseña>"
        Then dar click al boton de aceptar
        Examples:
            | nombre | contraseña | 
            | Isabel | 12345      | 
            | Carlos | abcdse     | 
            | Daniela| asdfcvs    | 

    
        
    