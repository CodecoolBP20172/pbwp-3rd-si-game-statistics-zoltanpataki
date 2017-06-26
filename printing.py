import reports
import pprint


def reports_answers_prints(file_name, year, genre, title):
    print("The number of games in the file: {}".format(reports.count_games(file_name)))
    print("There is a game from a given year: {}".format(reports.decide(file_name, year)))
    print("The latest game is: {}".format(reports.get_latest(file_name)))
    print("The number of games we have by the given genre: {}".format(reports.count_by_genre(file_name, genre)))
    print("The line number of the given game is: {}".format(reports.get_line_number_by_title(file_name, title)))
    pp = pprint.PrettyPrinter(indent=1, compact=False)
    print("The alphabetical ordered list of the titles is: ")
    pp.pprint(reports.sort_abc(file_name))
    print("The genres are: ")
    pp.pprint(reports.get_genres(file_name))
    print("The release date of the top sold First-person shooter game is: {}".format(reports.when_was_top_sold_fps(file_name)))
    return

reports_answers_prints("game_stat.txt", 2004, "First-person shooter", "Terraria")

