import reports
import pprint


def reports_answers_prints(file_name, title):
    pp = pprint.PrettyPrinter(indent=1, compact=False)
    print("The most played game is: {}".format(reports.get_most_played(file_name)))
    print("The total number of the copies have been sold is: {}".format(reports.sum_sold(file_name)))
    print("The average selling is: {}".format(reports.get_selling_avg(file_name)))
    print("The longest title cosists of {} characters.".format(reports.count_longest_title(file_name)))
    print("The average of the release dates is: {}".format(reports.get_date_avg(file_name)))
    print("The properties of the game is: {}".format(reports.get_game(file_name, title)))
    print("The number of games sorted by genre: ")
    pp.pprint(reports.count_grouped_by_genre(file_name))
    print("Date ordered list of the games: ")
    pp.pprint(reports.get_date_ordered(file_name))
    return

reports_answers_prints("game_stat.txt", "Terraria")
