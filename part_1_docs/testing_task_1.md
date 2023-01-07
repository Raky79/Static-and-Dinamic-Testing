### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  # missing the __init__ method to initialize the state of our object
  #  def __init__(self, value):
  #  self.value = value
   

  def check_for_ace(self, card):
    if card.value = 1:  # Should be == instead of =
      return True 
    else             #the colon is missing from this line 23, should be "else: "
      return False
   

  dif highest_card(self, card1 card2):     #Instead of dif should be "def "/ There is also a comma missing after card1
  if card1.value > card2.value:
    return card                            # In the line 29, should be "return card1"
  else:                                    # the indentation is wrong in the lines 28 and 30
    return card2
  


def cards_total(self, cards):
  total                      # instead of just total, should be "total = 0" 
  for card in cards:
    total += card.value
    return "You have a total of" + total    # the indentation on this line is wrong, the format is also wrong, total should be injected ,(f"You have a total of {total}")  
  
```
