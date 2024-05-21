""" Role game.
This program checks to see if you reach the next level
after killing a monster.
"""


# pylint: disable=invalid-name
def will_reach_next_level(experience, threshold, reward):
    """This function checks for experience, threshold and reward
     after killing a monster.
     """
    # Проверяем, достаточно ли текущего опыта для достижения следующего уровня
    return experience + reward >= threshold


# Пример 1: Уровень достигнут, вернет True
experience1 = 10
threshold1 = 15
reward1 = 5
print(f"experience:{experience1}, threshold:{threshold1}, reward:{reward1},"
      f" result:", will_reach_next_level(experience1, threshold1, reward1))

# Пример 2: Уровень достигнут, вернет False
experience2 = 10
threshold2 = 15
reward2 = 4
print(f"experience:{experience1}, threshold:{threshold1}, reward:{reward1},"
      f" result:", will_reach_next_level(experience2, threshold2, reward2))
