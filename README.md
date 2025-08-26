# mermaid-demo

Some Readme text
about something..

<h1> How to use ...</h1>
asdk aslkd jaslkdjasl j
</br>
klasjdlkasjkd kasdl kaslaskd jlakj
</br>
askldj lsaksd jkasdk jak
</br>
asdsad asd asd qwe sad asd
</br>
asd qwe asd qwe asd qwd asd
</br>
asd qwe asd qwe sad qwd
</br>
asd qwe sad qwdadasd


<h1> Class Diagram </h1>

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +String species
        +eat()
        +sleep()
        +makeSound()
    }
    
    class Dog {
        +String breed
        +boolean isTrained
        +bark()
        +fetch()
    }
    
    class Cat {
        +String color
        +boolean isIndoor
        +meow()
        +purr()
    }
    
    class Owner {
        +String name
        +String email
        +feedPet()
        +walkPet()
    }
    
    Animal <|-- Dog
    Animal <|-- Cat
    Owner "1" --> "1..*" Animal : owns
    
    note for Animal "Base class for all animals"
    note for Owner "Can own multiple pets"
```
