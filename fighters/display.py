from prettytable import PrettyTable
import fighters

fighter_table = PrettyTable(['Stats', fighters.f1.N, fighters.f2.N])
fighter_table.add_row(["Wins", fighters.f1.W, fighters.f2.W])
fighter_table.add_row(["Losses", fighters.f1.L, fighters.f2.L])
fighter_table.add_row(["Draws", fighters.f1.D, fighters.f2.D])
print(fighter_table)