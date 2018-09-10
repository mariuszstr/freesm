
from engine.db.person import Person
def test_constructor():
    person = Person("Tony", "Rickardsson")
    assert person.first_name == "Tony"
    assert person.last_name == "Rickardsson" 
    
