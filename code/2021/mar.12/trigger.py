from randomtext import RandomText
from randomsentence import RandomSentence

rt = RandomText("config/rt_test.json", "config/letter_frequency.json")
rt.speak(200)
rt.save_to_file()

rs = RandomSentence("config/rs_test.json")
rs.speak(200)
rs.save_to_file()
