import BDD

base = BDD.BDD("test")

base.requetesql("CREATE TABLE IF NOT EXISTS Test1 (id INTEGER, question TEXT, reponse TEXT)")
base.requetesql("CREATE TABLE IF NOT EXISTS Test2 (id INTEGER, question TEXT, reponse TEXT)")
base.requetesql("CREATE TABLE IF NOT EXISTS Test3 (id INTEGER, question TEXT, reponse TEXT)")
print(base.get_tables())
