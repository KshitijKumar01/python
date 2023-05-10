from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name", ["aditi", "kinjal", "kshitij"])
table.add_column("type", ["fire", "fire","water"])

table.align = "l"
print(table)